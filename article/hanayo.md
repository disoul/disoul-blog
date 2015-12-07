---
title: 博客开始使用Hanayo构建
author: disoul
date: 2015-12-07 16:55
tag:
    - 博客搭建
---

自己写的静态博客生成器肯定只有自己会用...

# Why
总觉得用`django`来搭博客是有点小题大作了
于是就有了自己写生成器的打算，正好最近在学`Node`
Hanayo就这样出现了

# Hanayo

项目主页 [github](https://github.com/disoul/hanayo) :-)

## 构建方式

没什么特别的基本是一条`Stream`跑完
大概的架构也就是`Stream`在跑的过程中不断收集整合对象
在最后一条`Stream`里分发对象到`views`下的`jade`模板
最后编译成静态文件

## 使用方法

估计除了我也不会有人用..

```sh
# install hanayo and hanayo-cli
npm install hanayo -g 

mkdir yourblog && cd yourblog

# defaule template writen by compass
gem update --system && gem install compass

# create hanayo project
hanayo init

# build static files
hanayo build

# start a express server
# using Nginx for Deployment
hanayo server
```
