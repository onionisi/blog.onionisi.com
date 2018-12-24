Title: ssh转发
Date: 2016-04-20
Category: Blog
Tags: ssh, work
Slug: ssh_forward

#### 替代品（171220更新）

* (ngrok)[https://ngrok.com]通过第三方服务器中转需要注册
* (frp)[https://github.com/fatedier/frp]新一代转发神器

#### ssh portforward

```
C                   S/C                 S
localhost:port <-> SSH hostname <-> remote host:port
if remote==localhost; remote= ssh hostname
```

- SSH连接和应用的连接这两个连接的方向一致，是本地转发。 在本地这台机器上监听一个端口，然后所有访问这个端口的数据都会通过ssh 隧道传输到远端的对应端口上
```
  ssh -L <local port>:<remote host>:<remote port> <SSH hostname>
```

- SSH连接和应用的连接这两个连接的方向不同，是远程转发。 在远端服务器监听一个端口，所有访问远端服务器指定端口都会通过隧道传输到本地的对应端口上
```
  ssh -R <local port>:<remote host>:<remote port> <SSH hostname>
```

- 参数 CfNg
  -C ：压缩数据传输。
  -f ：后台认证用户/密码，通常和-N连用，不用登录到远程主机。
  -N ：不执行脚本或命令，通常与-f连用。
  -g ：在-L/-R/-D参数中，允许远程主机连接到建立的转发的端口，如�不加这个参数，只允许本地主机建立连接

#### ssh with tar

- tar 注意Pp
    * cP : contain absolute name
    * xp : preserve permission
    * --exclude "PATH"(without '/' at the end)

```
    tar czf - data | ssh user@host "tar xf - -C dir"
    ssh user@host "tar czf - data" | tar xvzf - -C dir
```

