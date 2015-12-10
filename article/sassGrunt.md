---
title: Grunt下自动编译Scss
tag:
    - 博客搭建
    - web
author: disoul
date: 2015-07-20 23:00
---
早些时候气体说如果写scss的话不把css给ignore掉是不优雅的  
当时因为测试方便就没弄了  
于是现在给博客弄了一个自动编译scss的buff，这样ignore就顺理成章了  
  
为了实现这个效果，Grunt下需要2个插件

* sass
* watch

前者不用多说，编译sass用的，后者是一个监视插件，可以监视文件的修改打开等变动然后触发相应的task执行任务  
@@
# 配置Sass
因为sass是基于ruby的，所以我们要首先安装ruby环境并安装sass

## Ruby和Sass
因为我是ubuntu，所以直接  
`sudo apt-get install ruby`  
之后测试`gem`命令正常则成功，其他的系统安装详见<a href="https://www.ruby-lang.org/en/downloads/">ruby官网</a>  
之后用gem安装sass
`sudo gem install sass`

## Grunt下Sass配置
下面配置Grunt下的sass插件，关于Grunt的入门介绍上一篇介绍过了，这里直接开始配置  
### 安装插件
按照插件<a href="https://www.npmjs.com/package/grunt-contrib-sass">官方文档</a>的步骤，输入  
`npm install grunt-contrib-sass --save-dev`

### 修改Gruntfile
加入`grunt.loadNpmTasks('grunt-contrib-sass');`  
下面给出配置格式  

```js
grunt.initConfig({
  sass: {                              // Task 
    dist: {                            // Target 
      options: {                       // Target options 
        style: 'expanded'
      },
      files: {                         // Dictionary of files 
        'main.css': 'main.scss',       // 'destination': 'source' 
        'widgets.css': 'widgets.scss'
      }
    }
  }
});
 
grunt.loadNpmTasks('grunt-contrib-sass');
 
grunt.registerTask('default', ['sass']);
```
其中`style`有4种，为nested, compact, compressed, expanded.
files定义了编译的目标文件和编译后文件，除了上述方式，还可以使用如下格式  

```js
      files: [{
        expand: true,
        cwd: 'styles',
        src: ['*.scss'],
        dest: '../public',
        ext: '.css'
      }]
```
将文件夹内所有scss文件直接编译到目标路径  
这样sass的配置告一段落  

# 配置Watch
## 安装watch
同样的方法这里不赘述，具体见<a href="https://www.npmjs.com/package/grunt-contrib-watch">文档</a>  
`npm install grunt-contrib-watch --save-dev`  

## 修改Gruntfile
加入`grunt.loadNpmTasks('grunt-contrib-watch');`
这里只需要简单地检测.scss文件,修改后执行sass的task就行了  
格式如下  

```js
watch: {                                                                   
  script: {                                                                
    files: [                                                               
      '<%= meta.scssPath%>/**/*.scss'                                      
    ],                                                                     
    tasks: ['sass'],                                                       
    options: {                                                             
    },                                                                     
  }                                                                        
}
``` 

最后执行`grunt watch`
这样每当scss文件修改，就会输出下面这样的log  

```sh
"blog/static/css/scss/index.scss" changed.
Running "sass:dist" (sass) task^[[24m

Done, without errors.^[[39m
Completed in 4.023s at Tue Jul 28 2015 22:49:29 GMT+0800 (CST) - Waiting...
```
