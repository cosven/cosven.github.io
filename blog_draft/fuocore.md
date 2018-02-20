# feeluown - music player daemon for human?
_ps: 由于历史太长，所以丢后面去了。_

> Music Player Daemon (MPD) is a flexible, powerful, server-side
application for playing music. Through plugins and libraries it can
play a variety of sound files while being controlled by its network protocol.

`feeluown` is another **lightweight** MPD for human with its own protocol.

**Video demos.（自备梯子）**

1. 大致功能
[![Video Show](http://img.youtube.com/vi/-JFXo0J5D9E/0.jpg)](https://youtu.be/-JFXo0J5D9E)
2. Emacs 客户端
[![video show](http://img.youtube.com/vi/k1C0gCUiJqE/0.jpg)](https://youtu.be/k1C0gCUiJqE)

## features
- 像存储 dotfile 一样保存音乐列表、喜欢的歌手、喜欢的用户等
- 基于 tcp 的播放控制协议，易扩展
  - 使用 netcat 即可进行控制
  - 实时歌词
  - 对 awk, grep, cut 等 Unix 工具友好，方便与 Tmux/vim/Emacs 集成
  - ……
- 其它小特性
  - 网易云音乐、虾米音乐、qq 音乐、本地音乐资源互补
  - 依赖少，一键安装

如果你是个终端重度用户，你或许会喜欢。

（可以对比下 mopidy，或许是目前功能比较丰富的 MPD 了）

| feeluown                    | mopidy                              |
| --------                    | ------                              |
| local, netease, xiami, etc. | local, spotify, google music, etc.  |
| same                        | just a server run in terminal       |
| same                        | Everybody use their favorite client |
| N/A                         | on Raspberry Pi                     |
| same.                       | Easily extend                       |

暂时不知道写啥了，未完待续。




## 历史
想想从 [第一个 Commit](https://gitee.com/zjuysw/NetEaseMusic/commits/90347dfae21c733ddda03662c532bdd152026651)
到现在，也快三年了。

早在 12 年的时候，电脑上用 QQ 音乐，手机上都是用天天动听。
随后 13、14 年，被推荐了多米，songtaste等神器。
接着 2015 年末的时候，被推荐了网易云音乐，随后入了网易云音乐的坑。（此处省略 一万字）

期间，还入了 Ubuntu 的坑。但当时 Ubuntu 上真的找不到一个好用（功能较全）的播放器，
个人认为当时最好用的播放器应该是这个 [xaimi_radio](https://site.douban.com/154202/widget/notes/7942570/note/222709632/) 了。
但它功能真的很少呀。于是，造轮子...更多细节可以见 [链接](https://github.com/cosven/cosven.github.io/issues/41#issue-177624625)。
