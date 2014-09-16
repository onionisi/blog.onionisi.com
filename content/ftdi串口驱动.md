Title: FTDI串口驱动
Date: 2014-08-28
Category: Blog
Tags: OSX, driver
Slug: serial_driver

用MAC的同学应该搞应用和设计的居多，什么嵌入式啊，串口啊，定时器的很多同学应该都不感冒的。偶尔自己也玩玩一些硬件，所以串口这个东西还是少不了的。说起驱动，Linux对硬件的支持自不必多说，OS X就得自己动手了。

### FTDI2232

普通的USB转232的芯片不支持热拔插，原来的办公室已经躺尸了很多了，手中的2232其实是上大学的参加ZLG的竞赛发的一块开发版，旁边带的JTAG的调试，我顺手就用来当串口了，很是好使。最近想玩玩好久没碰的毕业论文的小车车了，想当年的巡线和遥控，哈哈，还是很佩服我自己的。

话不多说先上官网下驱动和doc，真的是不看官方的[Install Guide](http://www.ftdichip.com/Support/Documents/AppNotes/AN_134_FTDI_Drivers_Installation_Guide_for_MAC_OSX.pdf)，你还真弄不对。

```
The VCP driver is provided as part of the kernel in OSX 10.9, therefore no driver installation is required to create a virtual COM port in Mavericks. 
```

因为是Yosemite，自己又重新去`/System/Library/Extensions/IOUSBFamily.kext/Contents/Plugins`确认了一下`AppleUSBFTDI.kext`的存在。插上USB接口，查看`/dev/tty.usbserial-xxxxxxxx`是否出现，但是结果是令人失望的。

Troubleshooting里还是解答了我的疑惑

```
If the device does not work after installing the driver, it is likely to be because the PID is not supported by the driver. 
```
因为没有lsusb，只能去系统信息里去确认了一下VID为0x0403，PID为0xbcd8，与原厂0x6001不同，需要调整。

###[Solution](http://www.ftdichip.com/Support/Documents/TechnicalNotes/TN_105%20Adding%20Support%20for%20New%20FTDI%20Devices%20to%20Mac%20Driver.pdf):

```
The Info.plist file contains entries for various FTDI devices in the IOKitPersonalities dictionary. A new entry for an OEM device can be created by copying the personality of the equivalent FTDI device. In the simplest case, only the new device's name and idProduct key have to be provided. FTDI recommends that new OEM device personalities are added to the plist file, and existing FTDI personalities are retained. 
```
重新添加来一条2232D的描述，注意VID与PID即可。

### 串口软件

这个主要看大家口味了，putty，screen大家用的比较多，反正我是minicom的忠实用户了。主要就是波特率的设置了，乱码了什么的除了线接错了，就是波特率不对了，have fun，buddy！

