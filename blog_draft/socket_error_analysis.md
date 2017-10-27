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