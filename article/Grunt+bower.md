---
title: 使用 Grunt+Bower 管理前端
tag:
    - web
    - 博客搭建
author: disoul
---
# 介绍
### Grunt
下面是官网的介绍  
Grunt是基于Node.js的项目构建工具。它可以自动运行你所设定的任务。Grunt拥有数量庞大的插件,几乎任何你所要做的事情都可以用Grunt实现。  

### Bower
简单来说是一个用来解决各个web工具依赖关系，一个web下的包管理器

# 思路
使用Bower管理我的如jquery,bootstrp之类的资源，然后使用Grunt统一部署到服务器static下的lib文件夹  
因为刚刚接触Grunt，所以打算先做点简单的实现
@@
# 实现
## Node环境
首先这两个都是基于Node的，所以需要在机器上支持Node.js  
从https://nodejs.org/官网下载源码包  
解压后执行命令编译，编译顺利的话就可以通过`node`和`npm`命令查看版本了

```sh
./configure
make
make install
```

## Grunt
### 安装GruntCLI
`npm install -g grunt-cli`
上述命令执行完后，`grunt` 命令就被加入到你的系统路径中了，以后就可以在任何目录下执行此命令了。

注意，安装`grunt-cli`并不等于安装了 `Grunt`！`Grunt CLI`的任务很简单：调用与`Gruntfile`在同一目录中 Grunt。这样带来的好处是，允许你在同一个系统上同时安装多个版本的 `Grunt`。

### Package.js&Gruntfile
`grunt`的使用依赖与`package.json`和`Gruntfile`  
`package.json`应当放置于项目的根目录中，与`Gruntfile`在同一目录中，并且应该与项目的源代码一起被提交。在`package.json`所在目录中运行npm install将依据`package.json`文件中所列出的每个依赖来自动安装适当版本的依赖。  
输入命令`npm init`创建一个基本的package.json文件  
参考：我的`package.json`<a href="https://github.com/disoul/disoul-blog/blob/master/package.json">在这里</a>  
`devDependencies`下列出需要的包，其他的一些如作者、认证的写法规范可以参照  
<a href="https://docs.npmjs.com/files/package.json">Specifics of npm's package.json handling</a>  
  
接下来生成`Gruntfile`，`Gruntfile.js` 或 `Gruntfile.coffee` 文件是有效的 `JavaScript` 或 `CoffeeScript` 文件，应当放在你的项目根目录中，和`package.json`文件在同一目录层级，并和项目源码一起加入源码管理器。
我们可以通过`grunt-init`，简单生成一个Gruntfile，具体关于Gruntfile<a href="http://www.gruntjs.net/getting-started#gruntfile">戳这里</a>

```sh
npm install grunt-init -g
git clone https://github.com/gruntjs/grunt-init-gruntfile.git ~/.grunt-init/gruntfile
grunt-init gruntfile
```
### 安装Grunt
`npm install grunt --save-dev`

## Bower
### 安装
`npm install bower -g`

### 使用
比如，我想安装jquery到我的项目，只需要简单地键入  
`bower install jquery`  
`install`后面跟的参数需要是一个git仓库的地址，或者是一些大家都用的库可以直接输名字（如 jquery）  
因为我的项目还有font-awesome，所以继续输入  
`bower install font-awesome`  
之后这2个库就会下载在你当前目录下一个叫bower_components文件夹内  
接下来要做的就是用Grunt把bower生成的库拷贝到我项目的static下  

## 使用grunt-bower-task
### 安装
`npm install grunt-bower-task --save-dev`

### 配置Gruntfile
<a href="https://www.npmjs.com/package/grunt-bower-task">grunt-bower-task文档</a>  
将`grunt.loadNpmTasks('grunt-bower-task')`放在Gruntfile中module.exports函数内  

在`grunt.initConfig`内加入一个名为`bower`的数据
类似这种结构  
```js
grunt.initConfig({
  bower: {
    install: {
      options: {
		"targetDir": ..., //拷贝bower到目标地址
		"layout": ..., //拷贝后bower内各个库在文件夹内的布局  
                         "byType"按照js/css/html分3个文件夹  
						 "byComponent"按照各个库的不同分文件夹  
		"cleanTargetDir": ... //是否在install前清空`tatgetdir`
		...
		...
	 }
    }
  }
});
``` 
关于具体的options配置信息请参考上方的文档地址  

###实现
最后运行
`grunt bower`
再结合ignore就实现了我想要的效果  
于是下一步准备用Grunt实现自动编译scss，下回再弄
