Title: tmux的粘贴复制
Date: 2014-10-15
Category: Blog
Tags: tmux, conf
Slug: CP_of_tmux


电脑打开用的就是终端和浏览器，终端又是tmux掌控，所以不管tmux下cmd各程序或与桌面程序互通有无的时候，把tmux伺候好就OK啦。

### 复制模式

业务部门，又有新特性要开发啦。咦，这个功能点实现似曾相识，找找代码片段啊，打印机模式开启。JJYY一句，肯定有人说vim能粘贴复制要你干嘛，拜托同学们看看，clipboard特性打开没有。没有的同学用tmux先顶着，空了再去倒腾自定义编译。还有屏中某个小窗口程序的输出很有用，需编辑或记录，鼠标一拖，整屏都下来了，愁人。

tmux下凡走过必留痕，copy模式下一览无疑。下边的配置，几个命令都被我作了映射，可以改成自己熟悉的键位。不论一屏分几个窗口，都不会串行啦。one more thing, 我经常用copy-mode当历史模式使用，翻屏棒棒哒。

    # copy mode
    setw -g mode-keys vi              # keymap in copy mode
    bind Escape copy-mode             # enter copy mode (prefix Escape)
    bind ^p pasteb                    # paste buffer (prefix p)
    bind -t vi-copy v begin-selection # select (v)
    bind -t vi-copy y copy-selection  # copy (y)

### 粘贴到系统

哎哟，程序报异常啦，赶紧复制log或者exception到股沟看看爆栈有没有相关信息。

    # copy tmux buffer to system
    if-shell 'test "$(uname -s)" = "Darwin"' 'bind-key y run-shell "tmux show-buffer | pbcopy" \; display-message "Copied tmux buffer to system clipboard"'
    if-shell 'test "$(uname -s)" = "Linux"' 'bind-key y run-shell "tmux show-buffer | xclip -sel clip -i" \; display-message "Copied tmux buffer to system clipboard"'
    
### 不只是分屏

你们呐，naive，以为tmux就代替screen什么的分分屏那么简单？

`status-left/right`可以玩玩咯，配合自己的脚本或者命令，让你想看到跃至眼底。

`command-prompt`更可以玩玩，交叉互动，观看男人页各种手册文档之良品。
