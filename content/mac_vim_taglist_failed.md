Title: Mac vim taglist failed
Date: 2014-05-13
Category: Blog
Tags: OSX, vim, plugin
Slug: taglist_failed
Authors: Chong Yang


vim的常规插件taglist报错了，妈蛋，没有你我怎么看C code

```
Taglist: Failed to generate tags for /Users/chong/code/redis-3.0-annotated/src/ae.c
/Library/Developer/CommandLineTools/usr/bin/ctags: illegal option -- -^@usage: ctags [-BFadtuwvx] [-f tagsfile] file ...^@
```

出了问题习惯性先看源码，跑到taglist.vim里边找了一圈，4k多行，没有线索，只能发大招Google-fu了，顺带吐槽gfw。

taglist faq原文如下：

```
Q:Are you using exuberant ctags version 5.0 and above?
A:The taglist plugin relies on the features supported by exuberant ctags and will not work with GNU ctags or the Unix ctags utility. 
```

遂只能brew重新安装ctags，link ctags到/usr/local/bin/，该路径恰好在PATH变量中在/usr/bin前边，无缝替代ctags。若不想破坏emacs ctags，可在vimrc中另行此法：

```
let Tlist_Ctags_Cmd = '/path/to/ctags'
```
作为屌丝程序员为了跨平台，怎能就此作罢，不来两句if else怎么能行，参观学习[detect osx in vimrc][1]

```
if has("unix")
  let s:uname = system("uname")
  if s:uname == "Darwin\n"
    let Tlist_Ctags_Cmd = '/path/to/ctags'
  endif
endif
```

has是指vim特性，可通过feature-list查看，手贱的同学可能去看了，我堂堂大vim怎么会没有多系统检测，其中明明有mac的嘛，可就是不行啊，还有macvim啊，也不行，虾米原因？
__系统自带的vim只有unix特性，mac/macunix则没有__，只有MacVim可用这两种特性（槽点：cmd这么不受待见啊）。参考[get os in vim][2]

[1]:http://stackoverflow.com/questions/2842078/how-do-i-detect-os-x-in-my-vimrc-file-so-certain-configurations-will-only-appl
[2]:http://stackoverflow.com/questions/6146633/vimscript-how-do-i-get-the-os-that-is-running-vim?rq=1
