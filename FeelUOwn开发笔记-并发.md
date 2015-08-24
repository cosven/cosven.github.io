title: FeelUOwn 并发设计思路记录
date: 2015-07-21 09:52:46
tags: []
---

开发FeelUOwn过程中的笔记

这里主要记录了我是如何上手FeelUOwn 的“并发设计”。

如果这个思路不正确的话，这些记录也会有助于以后吸取教训。

`所有的行为的最终目的还是与人快乐相处 ~ `
<!-- more -->

## 摸着石头过河

不知道从哪开始的时候，那就是 **想想你具体想要什么** ？回答完这个问题，或许就知道该干什么了。

然后我就想起了“软工”课上的东西，需求分析-用例设计-架构设计-程序实现。大概这样一个思路吧，我也想不到其他的办法了... 

> `阻塞`，`非阻塞`，`异步`，`同步`。
非阻塞不一定异步。
`并发`：着重于请求端。
`并行`：着重于处理端。

## 简述
FeelUOwn 是什么？ 参考<https://github.com/cosven/FeelUOwn>，目前，FeelUOwn整个程序基本是单线程，操作都是同步的，也就是说，如果某一次操作需要的时间很长，那么整个程序都会陷入等待之中，这在桌面应用中是不可接受的。所以我想用异步的框架来让程序的体验更好。

异步的目的就是让用户总是可以进行操作，其中就包括终止当前某个操作，让某些操作进入后台。所以这个框架应该能对一些操作的运行状态进行跟踪。

## 简单需求分析

### 哪些地方可能需要用到异步

1. 用户打开软件，一开始加载的东西要尽量少。程序主界面启动后，可以开始慢慢加载其他的东西。

> 加载用户基本信息；加载首页

2. 用户进行了一个需要网络连接的操作，这时，最好让这个操作变为异步。

> 比如说：搜索，搜索歌手，搜索专辑，播放歌曲之类的


用例设计就跳过吧（我已经搞不清用例分析和需求分析的区别了...）

## 几种已有的异步框架的简要对比

基于之前对这些异步框架神马的都没有什么了解，看了一阵子别人的博客、文档什么的，也不明所以，还是自己动动手，先**对其中一个框架有点稍微深入的了解比较好**。

### Twisted, Tornodo, gevent

简要的看了别人对这几个东西的对比分析，我没有得出什么有用的结论。所以我想找`deepin-music`这个开源项目来参考了一下，看它是否用了其中的某个框架，结果... 直接在代码中搜这三个关键词，发现一个也没搜到，倒是搜threading这个词有很多结果。所以得出结论：**上面三个东西可能不是最好的解决方案**

然后我就想把之前使用nodejs的经验套过来，我感觉nodejs的那个异步应该不错，但是我记得nodejs的那个异步没办法对程序的运行状态进行跟踪，貌似也办法终止。

所以我又去google了一番，发现这篇文章或许有帮助: <https://us.pycon.org/2013/schedule/presentation/62/>

[Use Qt threads or Python threads?](http://stackoverflow.com/questions/1595649/threading-in-a-pyqt-application-use-qt-threads-or-python-threads)

所以，之后焦点转移到 `asyncio` 这个东西上面来了。

qt 和 asyncio 怎样组合呢，[github](https://github.com/harvimt/quamash) 上有人给出了解决方案。不知道方案成熟不

最后还是选用了 `quamash`, 目前感觉还挺好用的。


### asyncio 

`asyncio` 通过使用`协程`的并发模型在单线程上进行并发。

1. 它有一个可插拔的事件循环(`event loop`)，这个事件循环可以根据特定的系统实现。比如说，它可以根据Qt本身的事件循环来实现在qt上可用的 `event loop`

2. 它还有很多其他的特性，我暂时都没用到。

> 貌似很多其他很多并发库也都是使用类似 `event loop` 这种模式。

事件循环比较容易理解。就是一个服务员一直在工作，服务员有个_事件循环_，然后某个顾客说你帮我做一下_这件事_，服务员就把_这件事_扔到事件循环，其他顾客也同样的要服务员做事，服务员的_事件循环_中就有很多事要干，服务员就把自己的时间分成很小时间段，每个小的时间段中服务员都为某个顾客服务，这样子，服务员非常迅速的切换，每个顾客都感觉服务员在为他服务。

体现在程序上也非常简单好用。

```
import asyncio
import time

def hello_world(text):
    time.sleep(2)
    print(text)

def stop_event_loop():
    event_loop = asyncio.get_event_loop()
    event_loop.stop()
    

loop = asyncio.get_event_loop()
loop.call_soon(hello_world, "hello")
print("1")
loop.call_soon(hello_world, "world")
print("2")
loop.call_later(10, stop_event_loop)    # 10 秒后调用stop_event_loop函数
loop.run_forever()


# 输出的顺序将会是
1
2
hello
world
```


### 实践过程遇到几个坑

1. python 中一个函数如果有多个`装饰器`, 他们的执行顺序是怎样一定要弄清楚。

> 我自己写了一个装饰器，它能让函数变成并行（就是使用上面的call_soon函数），
> 但是有的函数它本来就有pyqtSlot这个装饰器，我本来没有注意装饰器的顺序，把自己的装饰器放在pyqtSlot的**前面**，导致了一些非常奇葩的问题。

```
@decorator1
@decorator2
def func():
    do something
```

它会先执行decorator2, 在执行decorator1


2. 分析网易云音乐的网页端的加密

用 chrome 或者 firefox 的 js debug，找到加密相关的函数，可以搜一些关键字(encrypt, base64, md5之类的字段) 设置断点，查看变量的值，就能比较容易的发现目标。
