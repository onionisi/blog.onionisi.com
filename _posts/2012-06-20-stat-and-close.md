---
layout: post
title: "stat and close()"
category: program
tags: [linux C, filesystem]
---
{% include JB/setup %}

# file stat and file close

## file stat 

中午吃饭的时候突然聊起了权限，笑777是bus，有点混淆stat的结构了，下午回来看了stat.h

	// 出自bits/stat.h
	#define __S_ISUID   04000   /* Set user ID on execution.  */
	#define __S_ISGID   02000   /* Set group ID on execution.  */
	#define __S_ISVTX   01000   /* Save swapped text after use (sticky).  */   
	#define __S_IREAD   0400    /* Read by owner.  */ 
	#define __S_IWRITE  0200    /* Write by owner.  */
	#define __S_IEXEC   0100    /* Execute by owner.  */
	
	// 出自sys/stat.h 
	#define S_ISUID __S_ISUID   /* Set user ID on execution.  */
	#define S_ISGID __S_ISGID   /* Set group ID on execution.  */
	
	#if defined __USE_BSD || defined __USE_MISC || defined __USE_XOPEN
	/* Save swapped text after use (sticky bit).  This is pretty well obsolete.  */
	# define S_ISVTX    __S_ISVTX
	#endif
	
	#define S_IWUSR __S_IWRITE  /* Write by owner.  */
	#define S_IXUSR __S_IEXEC   /* Execute by owner.  */
	/* Read, write, and execute by owner.  */
	#define S_IRWXU (__S_IREAD|__S_IWRITE|__S_IEXEC)
	
	#define S_IRGRP (S_IRUSR >> 3)  /* Read by group.  */
	#define S_IWGRP (S_IWUSR >> 3)  /* Write by group.  */
	#define S_IXGRP (S_IXUSR >> 3)  /* Execute by group.  */
	/* Read, write, and execute by group.  */
	#define S_IRWXG (S_IRWXU >> 3)
	
	#define S_IROTH (S_IRGRP >> 3)  /* Read by others.  */
	#define S_IWOTH (S_IWGRP >> 3)  /* Write by others.  */
	#define S_IXOTH (S_IXGRP >> 3)  /* Execute by others.  */
	/* Read, write, and execute by others.  */
	#define S_IRWXO (S_IRWXG >> 3)

另外还有就是lsattr的那一串属性，大伙知道是怎么来的不？

## file close

下午上stack_over_flow发现一个问题，Why do I have to use close() to close a file？[链接在此啊](http://stackoverflow.com/questions/11095474/why-do-i-have-to-use-close-to-close-a-file)
热情的筒子们回答得很热烈，但是其中有个哥们觉得他们有些人说的有问题，就是关于close到底处理不处理数据写回到磁盘的操作，我也比较懵，还写了小程序测试，晕，还得出是要回写的结论，结果后边在close的man手册里边的NOTE发现如下一段话。

>A  successful  close does not guarantee that the data has been successfully saved to disk, as the kernel defers writes.  It is not common for a file
>system to flush the buffers when the stream is closed.  If you need to be sure that the data is physically stored use fsync(2).  (It will depend  on
>the disk hardware at this point.)

所以要感谢那位执着的哥们。
