Title: oh-my-zsh的芯
Date: 2012-04-17
Category: Blog
Tags: shell, src, zsh
Slug: oh-my-zsh

用zsh有一段时间了，前段时间在github上找见了这个神奇的项目，试用起来果然还是
很有爱。但是之前的配置已经有我比较熟悉的快捷键，所以还是要改造一番，美其名曰
本地化。

## 主配置.zshrc

主配置很简洁，主要功能就是选主题选插件，形式各样的千奇百怪的prompt，各种功能
不同的插件，可根据发行版，版本控制工具进行选择，大家各取所需。
这也就是vim、firefox这些软件强大的原因---有广大的同志还开发插件！所以说群众
的力量是无穷的。
                 
下边就是主体程序的目录结构：

	/home/onionisi/.oh-my-zsh/
	|+cache/
	|+custom/
	|+lib/
	|+log/
	|+plugins/
	|+templates/
	|+themes/
	|+tools/
	|-oh-my-zsh.sh
	`-README.textile

## oh-my-zsh.sh

这个脚本才开始真正进入主题。

### upgrade

	# Check for updates on initial load...
	if [ "$DISABLE_AUTO_UPDATE" != "true" ]
	then
	  /usr/bin/env ZSH=$ZSH zsh $ZSH/tools/check_for_upgrade.sh
	fi

如果没有禁止自动升级的，首先会upgrade，oh-my-zsh作为一个公共项目，每天的更新
还是挺频繁，从github的图上就能看出来。再来看check_for_upgrade

	function _current_epoch() {
	  echo $(($(date +%s) / 60 / 60 / 24))
	}
	
	function _update_zsh_update() {
	  echo "LAST_EPOCH=$(_current_epoch)" > ~/.zsh-update
	}
	
	function _upgrade_zsh() {
	  /usr/bin/env ZSH=$ZSH /bin/sh $ZSH/tools/upgrade.sh
	  # update the zsh file
	  _update_zsh_update
	}

使用了天数来比较，比较有意思，若大于6天就要自己选择了，在upgrade中就主要用
git来pull最近的更新了，办公室的电脑是代理上网的所以我前边加上了proxychains。

### 初始化

首先就是要载入一些“库”，呵呵...有个custom可以自定义哦。

	# add a function path
	fpath=($ZSH/functions $ZSH/completions $fpath)
	
	# Load all of the config files in ~/oh-my-zsh that end in .zsh
	# TIP: Add files you don't want in git to .gitignore
	for config_file ($ZSH/lib/*.zsh) source $config_file
	
	# Set ZSH_CUSTOM to the path where your custom config files
	# and plugins exists, or else we will use the default custom/
	if [[ -z "$ZSH_CUSTOM" ]]; then
	    ZSH_CUSTOM="$ZSH/custom"
	fi
	
	is_plugin() {
	  local base_dir=$1
	  local name=$2
	  test -f $base_dir/plugins/$name/$name.plugin.zsh \
	    || test -f $base_dir/plugins/$name/_$name
	}
	# Add all defined plugins to fpath. This must be done
	# before running compinit.
	for plugin ($plugins); do
	  if is_plugin $ZSH_CUSTOM $plugin; then
	    fpath=($ZSH_CUSTOM/plugins/$plugin $fpath)
	  elif is_plugin $ZSH $plugin; then
	    fpath=($ZSH/plugins/$plugin $fpath)
	  fi
	done

### keypoint

俗话说得好包子好吃不在褶儿上，这配置好用可都在插件里，下边上插件


	# Load all of the plugins that were defined in ~/.zshrc
	for plugin ($plugins); do
	  if [ -f $ZSH_CUSTOM/plugins/$plugin/$plugin.plugin.zsh ]; then
	    source $ZSH_CUSTOM/plugins/$plugin/$plugin.plugin.zsh
	  elif [ -f $ZSH/plugins/$plugin/$plugin.plugin.zsh ]; then
	    source $ZSH/plugins/$plugin/$plugin.plugin.zsh
	  fi
	done
	
	# Load all of your custom configurations from custom/
	for config_file ($ZSH_CUSTOM/*.zsh) source $config_file
	
	# Load the theme
	if [ "$ZSH_THEME" = "random" ]
	then
	  themes=($ZSH/themes/*zsh-theme)
	  N=${#themes[@]}
	  ((N=(RANDOM%N)+1))
	  RANDOM_THEME=${themes[$N]}
	  source "$RANDOM_THEME"
	  echo "[oh-my-zsh] Random theme '$RANDOM_THEME' loaded..."
	else
	  if [ ! "$ZSH_THEME" = ""  ]
	  then
	    if [ -f "$ZSH/custom/$ZSH_THEME.zsh-theme" ]
	    then
	      source "$ZSH/custom/$ZSH_THEME.zsh-theme"
	    else
	      source "$ZSH/themes/$ZSH_THEME.zsh-theme"
	    fi
	  fi
	fi

欧欧欧...我觉得我都在粘代码了，还是大神linus说得对RTFSC，同志们还是直接去看
吧，直接明了。

下一步就是我要把我先前的顺手货拆开再组装上去，未完待续哦...
