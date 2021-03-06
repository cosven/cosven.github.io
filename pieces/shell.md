# 少折腾命令行

### item2/tmux/neovim true color 支持

-   iterm 设置 term 环境变量为 xterm-256color
-   tmux 设置 ~set-option -ga terminal-overrides ",xterm-256color:Tc"~
-   neovim 不怎么需要设置，如果要的话，就是下面这个

    set termguicolor
    set t_8f=^[[38;2;%lu;%lu;%lum
    set t_8b=^[[48;2;%lu;%lu;%lum

举个例子：[我的配置](https://github.com/cosven/rcfiles/commit/1af74b2352967f0a937a63cb03942b91c0fc7f42)
测试脚本：[链接](https://github.com/cosven/rcfiles/commit/b608261986833bad359d13168229d9e6ccdc1a64#diff-9bf5a2f4d58325ac0e124b2525172d15) -> 如果输出的颜色润滑过度，就代表改环境是支持 true color 的。

### linux 查看已经安装的内核

    dpkg -l | grep linux-image

### ssh 端口映射

本地端口映射： `ssh -L 9000:cosven.dev:8000 cosven.dev`
这时，访问本地 9000 端口，就相当于访问 cosven.dev 的 8000 端口

远程端口映射： `ssh -nNT -R 2222:localhost:22 cosven.dev`
假设我们从本地可以 ssh 到 cosven.dev，但是从 cosven.dev 不能 ssh 到本地
这时，我们可以使用这种方式&#x2026;

`-N` 不登录 `-f` 后台跑

### 替换一个目录下的所有文件中包含某个字符串的文件

=grep -rnw '*path/to/somewhere*' -e 'pattern'=

### 查看一个程序占用了那个端口

`lsof -Pan -p PID -i`


### 重构 - 重命名
tags: refactor, rename

```shell
linux: git grep -l 'original_text' | xargs sed -i 's/original_text/new_text/g'
mac: git grep -l 'original_text' | xargs sed -i '' -e 's/original_text/new_text/g'
```
