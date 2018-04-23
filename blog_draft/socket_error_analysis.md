# 各种各样的 socket error 分析

[这里](https://gist.github.com/gabrielfalcao/4216897)有个 socket error code 参考


### Error 99: Cannot assign requested address

#### 出现的原因

1. 一种可能是端口被占用了或者系统分配不了端口了...


## 配合诊断的一些工具

netstat, lsof

### lsof (list open files)

### netstat (network statistics)

- `netstat -tu` : 查看 TCP/UDP 连接
- `netstat -tunp` : 查看 TCP/UDP 连接，addr 用 IP 表示，并显示对应的 Process ID

### 查看哪些端口可以被程序使用

`sudo cat /proc/sys/net/ipv4/ip_local_port_range`

### HTTP 502 Bad Gateway and 504 Gateway Timeout

> The 504 (Gateway Timeout) status code indicates that the server,
while acting as a gateway or proxy, did not receive a timely response
from an upstream server it needed to access in order to complete the
request.

- [ ] 一个疑问：是不是说可以断定是服务端的问题？

假设链路是 Client -> xxx -> Nginx -> HAProxy -> Server

假设 xxx -> Nginx 这里超时的话？是不是结果应该是 Connection Timeout
而 Nginx -> HAProxy 或者 HAProxy -> Server 超时的话，就是 504 了。

502

### 503 Service Unavailable

服务端超载了，或者拒绝连接

### 哪些情况会导致出现 Connection Reset (by peer)？
Connection Reset 出现的直接原因是一端发送了 RST 包。
常见情况：一端重启了，另一端仍然在发送数据包。因为它们还没有进行三次握手
就开始传数据。

注：如果一端死掉了，错误会是 Connection Refused。此时一端的端口并未被监听。
