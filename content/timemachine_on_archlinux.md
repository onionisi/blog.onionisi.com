Title: TimeMachine on Archlinux
Date: 2014-05-08
Category: Blog
Tags: OSX, linux, timemachine
Slug: timemachine-on-archlinux
Authors: Chong Yang


## 前因

之前拿到新电脑很是兴奋，捯饬很比较猛，主要还是想目的就是延长SSD使用寿命，于是乎找了各种措施来减少SSD的写入。万恶的是没有任何备份，当我满心欢喜的禁用了磁盘的日志功能时，心想怎么可能意外断电捏。哪里知道就在第二天浏览淘宝时，打开网页太多导致浏览器卡死了系统，任何操作都不灵了。妈蛋滴，果断强制关机，reboot，老有一个进度条过不来，打客服电话，最后把我弄到检查磁盘的时候，发现磁盘损坏根本修复不了。这时才焕然大悟想起自己关闭了日志，天要亡我，奈何啊，可怜我的资料啊。

格式化磁盘的时候那叫个恋恋不舍啊，只能忍痛了，在线安装好Marvicks后，看着才出的Yosemite心痒痒，干脆一横心直接升了，这一来二回把我之前节约的写入全糟践了。心里便想着还是要搞个备份才行，Mac不是Linux，什么东西你都能Control，还是小心谨慎为好。

## 后果
恋恋不忘，必有回响，总算打起精神准备，把重装新系统以来各种资料备份一下，再丢了就只能掩面而泣了。linux世界的geek们不会让我们失望滴，netatalk就是来抢time capsule生意滴。

配置文件位置 /etc/afp.conf

    [Global]
    mimic model = TimeCapsule6,106
    log level = default:warn
    log file = /var/log/afpd.log
    hosts allow = 192.168.1.0/16
    
    [TimeMachine]
    path = /path/of/TimeMachine
    time machine = yes
    
然后systemd使能并启动netatalk和avahi，进入Time Machine设置搞定啦。

## one more thing

以前我挂载其他电脑文件夹习惯性使用sshfs，Mac需要FUSE OSX依赖安装麻烦，但是netatalk还可以使用共享。
配置文件中加入如下

    [Media]
    path = /path/of/media/
    
其他linux也可以把afpfs当NFS挂载

    mount_afp 'afp://username:password@ipaddr/Media' /mount/path/
    
再也不用担心NFS挂载的麻烦啦。
