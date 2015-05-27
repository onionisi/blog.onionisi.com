Title: vim二三事
Date: 2015-03-19
Category: Blog
Tags: vim, plugin
Slug: vim_plugin_I_used


话说天下编辑器分为两派，不知不觉从了vim老久了，老夫老妻就感觉没激情了，不想捯饬各种配置，这不趁着neo-vim的新鲜劲儿，重新梳理了一遍配置。

### nvim
这个vim的岁数也不小了，几十年来，江湖众人想搞个小鲜肉大家尝尝，neo-vim便是其中之一。这货骨骼精奇，尽得前辈真传，同时还自创不少武术套路，确实是值得会会。

    alias vi='nvim'
    cp ~/.vimrc ~/.nvimrc
    
配置完全兼容，这丝滑。命令响应采用S/C模式，so后台会有一个单独pymodule neovim监听。得益于新的软件架构，插件执行效率更高更快。新特性还有vt，可直接集成终端，各位可自行前往github围观。

### vundle 
自由软件的世界不能没有包管理，你看看各大发行板，你看看node，你看看ruby/python，你看看go，现在新的编程语言没有这个好意思发布么，再看看rust。那么vim这个屌丝呢，也有很多包管理哦，vundle和github结合较好，比较好用的说。

呃，vundle的interface早就更改了，Bundle变Plugin了，妈蛋，老子还一直纳闷怎么插件都不更新了，怪不得老是同步不上捏。是时候好好整理一下vim的插件啦，不然还说是vimer，囧rz。

配置文件也有变化，晕
    
    call vundle#rc()

现在变成

    call vundle#begin()
    ...
    call vundle#end()

### 常用Plugin

积累了不少插件和快捷键，和大家share一下

#### 常规四件

    Plugin 'scrooloose/nerdtree'
    Plugin 'bling/vim-airline'
    Plugin 'majutsushi/tagbar'
    Plugin 'minibufexpl.vim'
    
东南西北四大神兽打先锋，nerdtree作文件导航，airline替代powerline美化bar，tagbar替补taglist分析文本展现词条，minibufexpl管理buffer

#### 编辑能手

    Plugin 'tpope/vim-commentary'
    Plugin 'kien/ctrlp.vim'
    Plugin 'Valloric/YouCompleteMe'
    Plugin 'ervandew/supertab'
    Plugin 'mattn/emmet-vim'
    Plugin 'godlygeek/tabular'
    Plugin 'rking/ag.vim'
    
commentary自动帮你识别注释符号，你只需要选中并注释，无需亲自编辑。    
ctrlp不必多说，文件查找神奇，同时注意ignore各种无关文件    
YCM更不必废话，但是更新后要重新编译，感叹为什么我写C的时候没出来？？一般与supertab配合使用。    
emmet，敲代码最烦的就是符号配对啦，你要编辑html怎么能少了她！    
tabular对齐神器，为了代码更有逼格，你值得试试    
ag全称advanced grep，完爆grep，you known，宇宙最强文本搜索，该插件直接调用的shell
    
    
#### 类型识别

    Plugin 'klen/python-mode'
    Plugin 'fatih/vim-go'
    Plugin 'plasticboy/vim-markdown'
    Plugin 'elzr/vim-json'
    Plugin 'scrooloose/syntastic‘
    
靠python养家的我怎能没有你，python-mode    
go有自己的官方插件，但是这个打包的更好，话说go真心不错，像极了python和C的bastard    
不写md的同学难道你写rst   
json貌似在浏览器里看得多点    
syntastic语法检测，避免出错    
 
### 基本配置

还有一些可配置小点，各位小主有兴趣可以取用。

集中各中间文件，方便统一处理。

    " Centralize backups, swapfiles and undo history
    set backupdir=~/.vim/backups
    set directory=~/.vim/swaps
    if exists("&undodir")
        set undodir=~/.vim/undo
        set undofile
        set undolevels=500
        set undoreload=500
    endif

不同类型文档不同缩进

    au FileType javascript,sass setlocal ts=2 sw=2 sts=2 et
    au FileType python setlocal ts=4 sw=4 sts=4 et
