Title: OSX Launchd
Date: 2014-07-21
Category: Blog
Tags: OSX, init
Slug: osx-launchd
Authors: Chong Yang


习惯了Linux下init，rc或者systemd的方式，来到Mac下想搞个启动项还是要费费脑子重新学习下除了鼠标点击的账户->登录项以及dock上的登陆时打开，毕竟总多的系统级别的程序是在launchd的统治下。

### 文件

cmd总是跟文件脱不了干系的，plist开始登场，下边是他存在的世界，摘自launchctl男人页：

~~~
    ~/Library/LaunchAgents         Per-user agents provided by the user.
    /Library/LaunchAgents          Per-user agents provided by the administrator.
    /Library/LaunchDaemons         System wide daemons provided by the administrator.
    /System/Library/LaunchAgents   OS X Per-user agents.
    /System/Library/LaunchDaemons  OS X System wide daemons.
~~~

~~~
In the launchd lexicon, a “daemon” is, by definition, a system-wide service of which there is one instance for all clients. An “agent” is a service that runs on a per-user basis. Daemons should not attempt to display UI or interact directly with a user’s login session. Any and all work that involves interacting with a user should be done through agents.
~~~
其中LaunchAgents与LaunchDaemons的区别就是启动顺序是在用户登录前还是后的差别。

另外plist的格式各位亲也请查阅launchd.plist相关男人页，话说我最讨厌的就是xml，html这类的标记语言了，为什么还要用来配置系统Mac兄？！

##### Required and recommended property list keys[^1]
[^1]:[苹果开发者中心文档](https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)

Key | Description
:-------- | :------------------------
Label | Contains a unique string that identifies your daemon to launchd. (required)
ProgramArguments | Contains the arguments used to launch your daemon. (required)
inetdCompatibility | Indicates that your daemon requires a separate instance per incoming connection. This causes launchd to behave like inetd, passing each daemon a single socket that is already connected to the incoming client. (required if your daemon was designed to be launched by inetd; otherwise, must not be included)
KeepAlive | This key specifies whether your daemon launches on-demand or must always be running. It is recommended that you design your daemon to be launched on-demand.

### 操刀

其实主要操作就是launchctl load与unload，但是有两种情况需要区分

1. 标记/var/db/launchd.db/com.apple.launchd/overrides.plist，如果没有再查看plist Label是否Disable。
2. mv plist文件使其不出现在上述5个目录。

想要禁用某程序自启动，先找到该文件路径，照上述方式即可搞定。

```
grep -rl name_of_program /Library/Launch* /System/Library/Launch* | xargs wc -l | sort -n | head -n1 | awk '{print $2}'
```

### 多技能get[^2]
[^2]:[launchd is cool](http://paul.annesley.cc/2012/09/mac-os-x-launchd-is-cool/)

* cron，关键属性`StartInterval`，每多少秒执行一次，
`StartCalendarInterval`简直就是cron的复刻版，但提供了更多的控制选项，不用单独再整理crontab了。

* file watcher，`WatchPaths`有任何改动即启动，`QueueDirectories`任务开始文件夹必须为空，监控新文件并处理，网络编程select即视感。


PS: 图形前端[Lingon X](http://sites.fastspring.com/peterborgapps/product/lingonx)可用但要10刀，App Store版本因为提权原因功能不完整。
