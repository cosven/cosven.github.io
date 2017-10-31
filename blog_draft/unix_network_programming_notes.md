# unix 网络编程读书笔记

## 第一章
### 练习

- [ ] 用 asyncio 手写一个 socket echo 程序？
- [x] 子关掩码的含义以及相关计算
    [https://www.zhihu.com/question/21064101/answer/17056026](IP 寻址)
    先找子网，再找主机。找子网就是通过 IP 地址 + 子网掩码来进行的

### 些许总结
网络四层
![image](https://user-images.githubusercontent.com/4962134/32207184-57ec6f32-bdc8-11e7-86af-e4afbd535d51.png)
> Internet (AF_INET) stream (SOCK_STREAM) socket, which is a fancy name for a `TCP socket`.

讲了几个东西：
* socket 的一些概念
* 这本书的一些约定
* 网络模型简介：4 层和 7 层
* POSIX 简介
* 有些关于网络拓扑的简介

