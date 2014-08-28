Title: After New Install
Date: 2014-05-10
Modified: 2014-08-15 19:30
Category: Blog
Tags: OSX, config
Slug: after-new-install
Authors: Chong Yang

升级到10.10的Yosemite第一个感觉是好多app要遭殃了，首先是alfred(虽然重点是workflow，但我很少用)，然后是各种输入法和一票终端。

* 给Terminal选个好看的配色，这货也可以切割面板了，不过我还是喜欢iterm2的全局键呼出。


* change host name，没有好听得名字怎么能行:
```
sudo scutil --set HostName Yosemite
```

* Command Line Tools for Xcode 6找得我好辛苦，没有cmd我怎么活。

* 迅速安装brew and brew cask，没有包管理器我怎么活。

* 迅速安装一票app，tmux vim zsh firefox mou flux

* 各种配置tmux，再也不用担心如何切分窗口，vim再也不要彷徨什么神编辑啦，zsh＝＝oh-my-zsh

* cross the gfw.安装goagentx。 pac and goagent and shadowsocks
```
goagent:
onionisi1986|onionisi1987|onionisi1988|onionisi1989|yangchong198628
```
```
shadowsocks:
198.199.96.65:8388 judy aes-256-cfb
```
* 换个更顺手输入法，系统自带不错，不用啦。

* disable dashboard。
```
defaults write com.apple.dashboard mcx-disabled -boolean YES && killall Dock
```

* way to displace loadavg procfile.
```
sysctl -n vm.loadavg
w | head -n1 | cut -d’:’ -f4
uptime | cut -d’:’ -f4
```

* noatime for the SSD

* add quit to the finder menu
```
defaults write com.apple.Finder QuitMenuItem 1
```

* 更快的国内源
```
npm
$npm --registry http://registry.npm.taobao.org info underscore
```
```
gem
$gem sources --remove https://rubygems.org/
$gem sources -a https://ruby.taobao.org
```
```
pip
Global settings:
Add ~/.pip/pip.conf that includes:
[global]
index-url = http://pypi.tuna.tsinghua.edu.cn/simple
```

* “China Internet Network Information Center EV Certificates Root”，和“CNNIC ROOT”
untrust！！！

* openerDNS: 42.120.21.30，树大招风已死，还是用台湾同胞的61.139.2.69，以及阿里的223.5.5.5与223.6.6.6。另阿里的国内镜像也很快，各位可以换啦。


* 禁止创建.DS_Store文件
```
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
