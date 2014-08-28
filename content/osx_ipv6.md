Title: OSX ipv6
Date: 2014-08-14
Category: Blog
Tags: OSX, network, ipv6 
Slug: osx-ipv6
Authors: Chong Yang


今天心血来潮想弄把IPv6，因为这PAC让部分网站抽风。不用说只能通过tunnel实现，我大西南地区向来就是敢为人后的代表。之前在Archlinux上配过aiccu和gogoc都挺好，两个都要自行去申请账号哦。其中gogoc需要时间同步，误差太大就连不上啦，之前折腾了半天，注意同步网络时间。

brew里没找见gogoc，直接就上aiccu了，得知需要tuntap依赖，其实就是内核扩展，这里就有个坑（主要是用Yosemite的同学）了，各位注意：**tuntap的ext没法加载[^1]，console日志报错没有签名，10.10的不允许使用未签名kexts[^2]。**解决方式如下：

[^1]:[tuntap does not work on Yosemite 10.10](https://github.com/Homebrew/homebrew/issues/31153)

[^2]:[Unsigned kexts cannot be used on 10.10](https://github.com/Homebrew/homebrew/issues/31164)

1. disable kext signing checks for everything, by doing `sudo nvram boot-args="kext-dev-mode=1" `and rebooting.

2. signed tun/tap.ext in the bundle of tunnelblick, just copy it to /Library/Extensions.

1st我认为还是会有风险将影响整个系统内核的加载，虽然有盆友成功了。2nd还是安全无痛滴，先行安装tunnelblick，然后cp，一load就出现了/dev/tun0等装置。

毕竟是同根生，配置文件都没动，直接从dropbox down下来，`sudo aiccu start /path/config`，当当当当。。。我的ipv6地址：2401:e800:100:bb::2
