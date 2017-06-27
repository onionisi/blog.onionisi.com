Title: Arch on MBP
Date: 2015-07-24
Modified: 2015-07-30 19:30
Category: Blog
Tags: archlinux, config
Slug: archlinux-on-macbookpro
Authors: Chong Yang

Due to my over optimization, my macbook got crashed caused by the Chromium with
too many tabs. I was so confidence to disable the journal function of hfs+,
obviously it was a big mistake. I could't recovery my OSX, so after bearing a 
long time with hfs+, I choose to back home, the archlinux.

Thanks god, most hardware components already have got a nice compatible.
Especially the Ratina display, Cinnamon desktop have a auto option in DPI.As a
result, you can have a different dpi on diffrerent monitor. That is pretty nice
for me because I always works with my BENQ BL2410, a 24' monitor I bought a few
years ago.

Only wifi driver is in AUR. And I also make a script to control the fan,
just a single fan in MBP 13' late 2013. It's for the flash, damn flash. 

### Install
--------

* gdisk, reserved for sdx1 for EFI.
* efibootmgr, watch the BootOrder
* Loader, grub or rEFInd 
* broadcom-wl, WIFI driver by broadcom in AUR

### After Install
--------

* xinitrc
* IM, ibus doesn't work well with cinnmon-panel, fcitx-rime(insteaded by yong)
* backlight, xbacklight(no need coz cinnamon)
* fan, script
* font, fira-mono, simsum(Mono font I will write another post)
* powersave, modprobe file
* network, netctl can not connect a hidden WIFI(back to network-manager)
* openbox, obconf(not use now)
* cinnamon

Hope you guys all enjoy linux!
