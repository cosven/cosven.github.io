# unix 网络编程读书笔记

## 第一章 Introduction
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




## 第二章 Transport Layer: TCP/UDP/SCTP

### 小总结

### TCP

- reliability - acknowledgments, retransmit
- sequence numbers (one byte one number)
- RTT estimation
- flow control -> advertised window
- full-duplex -> receive and send in both direction on a given connection at any time

### SCTP

### UDP

- each UDP datagram has a length

### TCP 连接建立和终止

#### 三次握手

1. client -> SYN(synchronize) segment (会告诉 server 一开始的 sequence number)
2. server -> ACK SYN(acknowledge) 发一个 SYN 回去，也会告诉 client 一开始的 sequence number
3. client -> ACK 一下

SYN segment 里面可以包含 TCP Option

- maximum segment size
- window scale option
- timestamp

#### 连接终止

FIN segment

一个相关[中文博客](http://www.cnblogs.com/fczjuever/archive/2013/04/05/3000680.html)详细的讲了 TCP 连接各种状态

TIME_WAIT 状态存在的[意义](http://blog.csdn.net/rain_qingtian/article/details/9977249)



#### socket pair

#### buffer size