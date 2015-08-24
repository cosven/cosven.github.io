title: D-Bus学习
date: 2015-07-22 09:16:32
tags: [dbus]
categories: linux
---

** 学习目标 **

1. D-Bus 是干什么的，它存在的目的？
2. D-Bus 的一些基本概念和原理。
3. D-Bus 的一些应用示例。


<!-- more -->

### D-Bus 是干什么的

D-Bus 是一个提供简便系统中进程间通信的`消息总线系统`。它包含一个能以全系统或者针对一个用户会话运行的`守护进程`，和一系列提供与 D-Bus `通信的库`。


### D-Bus 的一些基本知识

从架构上来说，D-Bus包含了几层：
1. `libdbus`
2. `message bus daemon`
3. `wrapper libraries or binds`

** 为什么是选用D-Bus**

> D-Bus 专注解决了两件事情
1. 同一个桌面会话的桌面应用程序之间的通信
2. 桌面会话和操作系统之间的通信

** 它相比于其他类似的IPC技术的优点 **

> 

#### 基本概念

不管你通过什么语言，什么框架来使用D-Bus, 下面这写基本概念都是需要了解，都是互通的。

###### Native Objects and Object Paths


###### Methods and Signals


###### Interfaces
Think of an interface as a named group of methods and signals

###### Proxies
A proxy object is a convenient native object created to represent a remote object in another process. 

###### Bus Names

`Bus Names` 一方面可以充当一个应用的标识符。它是独一无二的。一般命名就像`:34-907`这样子。它以冒号开头，后面会有数字，数字没什么含义。

应用也可以要求拥有一个好记的名字。比如说 VLCPlayer

`Bus Names` 还经常被用来跟踪应该用的生命周期。

###### Addresses




Address -> [Bus Name] -> Path -> Interface -> Method


##### Messages

通过在进程之间发送messages，D-Bus得以正常工作。常见的Message的类型有四种。

1. Method call messages ask to invoke a method on an object.
2. Method return messages return the results of invoking a method.
3. Error messages return an exception caused by invoking a method.
4. Signal messages are notifications that a given signal has been emitted (that an event has occurred). You could also think of these as "event" messages.

每个Message都会有一个header，一个body。header就包括fields，body包含arguments。大概跟HTTP的一个请求有些像吧。


##### Calling a Method
D-Bus中一个Method的调用由两个messages组成。
一个Message从进程A发送到进程B，另外一个Message从进程B回复给进程A。

##### Emmitting a Signal
在D-Bus中，一个Signal由一个单独的message组成。一个Signal就是一个没有方向的广播。





### 实战训练

##### 通过py脚本来从外部控制deepin-music的播放

下载安装`d-feet`, 它帮助我查看dbus里面各种信息。它大概长下面这个样子。

![d-feet](http://7viixf.com1.z0.glb.clouddn.com/software/dfeet-usage-caption.png)

从这个图片，我们大概可以看出 `session bus daemon` 中有个`bus name`为 *com.linuxdeepin.DMusic*的应用，它的`object path` 是 */com/linuxdeepin/DMusic*，它有`interfaces`，然后`interfaces`中又分两个小组（图片中只显示了一个），其中一个为 *com.linuxdeepin.Dmusic*, 这个 `interface` 下就有一些`methods` 和 `signal`, 这个例子没有 `signal` 。然后这些`method`貌似都是可以被其他进程调用的。


```python
import dbus

session_bus = dbus.SessionBus()  # get session bus

# try to get deepin_music dbus proxy
dmusic_dbus_object = session_bus.get_object('com.linuxdeepin.DMusic', '/com/linuxdeepin/DMusic')

# get method from a dbus object
next_method = dmusic_dbus_object.get_dbus_method('Next')

# invoke the method
next_method.call_async()  # amazing, dmusic just play next song !

```

> 如果对上面那些dbus的基本概念有了了解之后，写出这个简单而又神奇的脚本也就不难了。黑科技 ！！！装逼神器啊... mac和windows下应该也有类似的东西吧。。。



### 参考资料：
1. <http://dbus.freedesktop.org/doc/dbus-tutorial.html>
