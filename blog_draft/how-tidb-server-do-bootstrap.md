# TiDB 源码阅读 - 启动流程

## 背景

前几天遇到一个问题：我使用 TiDB-Operator 部署了一个 TiDB 集群，部署完毕后，
我使用 `kubectl get pod` 命令看了下各个 Pod 的运行情况，发现都是出于 `Running`
状态，这时，我认为该集群时没有问题的，于是我尝试运行了一个 `create database deploy_check_1;`
的语句来检测集群是否真的没问题，出乎我的意料，这条语句用了 90s，我重复了几次，
发现 DDL 语句都会耗时 90s。

ummm，这么看的话，不是 bug 也算是 issue 把：我用 operator 部署 tidb，
看起来进程都正常，网络也 OK，但是 TiDB 工作不正常，于是我就去群里提了个问题。

提问是个非常难的问题，有很多智慧，回答也是。提问-回答过程中，我遇到了一个常见的问题：
研发认为我提供的信息太少，而我认为研发给我的回答实际上信息量也特别少，这个其实是避免不了的。
所以我又回来默默的排查。

### 排查的一些发现

1. 一个 TiDB 实例一直在重启，不过它是每隔多个小时才会重启，这也是之前我没有发现它进程不正常的原因
2. 这个重启的 TiDB 有一个这样的日志 `["[ddl] init domain failed"]`


于是脑袋里面冒出两个问题：

1. TiDB 启动的时候到底会干些啥事情？
2. domain 到底是个啥？（我之前也好几次碰到过它）

而之前看的论文里面说到，类似 **分布式系统启动新服务** 这样的逻辑往往容易有 bug，
搜了搜资料，实在是没有相关文章和文档，于是我就欢快的来阅读源码了。

当然，除了读源码，咨询开发其实是一个更快速的方法，但这对我来说，不是一个最优的方案。

## 读代码

源码阅读有个技巧是找最老版本的代码来读，因为最老版本的代码对于新手理解是比较友好的，
尽管它可能有些 bug 或者和最新版不一样的地方。
