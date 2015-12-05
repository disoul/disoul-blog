---
title: Learning Advanced JavaScript 学习笔记(3)
tag:
    - web
    - javascript
author: disoul
---
# Flexible Arguments 灵活的参数
函数的参数也是一个学问，还是栗子

```javascript
function merge(root){ 
  for ( var i = 1; i < arguments.length; i++ ) 
    for ( var key in arguments[i] ) 
      root[key] = arguments[i][key]; 
  return root; 
} 
 
var merged = merge({name: "John"}, {city: "Boston"}); 
assert( merged.name == "John", "The original name is intact." ); 
assert( merged.city == "Boston", "And the city has been copied over." );
```
@@
这里函数`merge`只有一个参数`root`，但在调用这个函数的时候传入了2个字典参数  
其中第一个`{name:"John"}`就是root，但第二个参数并不会被舍弃  
在传参时，js会把所有的参数存入一个`arguments`对象，`arguments`是一个函数作用域的对象    
<b>注意，`arguments`并不是数组，只是可以通过[i]索引访问元素</b>   
     
下一个栗子

```javascript
function smallest(array){ 
  return Math.min.apply( Math, array ); 
} 
function largest(array){ 
  return Math.max.apply( Math, array ); 
} 
assert(smallest([0, 1, 2, 3]) == 0, "Locate the smallest value."); 
assert(largest([0, 1, 2, 3]) == 3, "Locate the largest value.");
```
这里在函数中，通过`apply`对`array`对象调用`Math`对象的`min`或者`max`方法   
然而这一节说的是参数，于是下面黑魔法  

```javascript
function smallest(){ 
  return Math.min.apply( Math, arguments ); 
} 
function largest(){ 
  return Math.max.apply( Math, arguments ); 
} 
assert(smallest(0, 1, 2, 3) == 0, "Locate the smallest value."); 
assert(largest(0, 1, 2, 3) == 3, "Locate the largest value.");
```
解释上面说过了，通过`arguments`指代参数，瞬间优雅不少  
下一个杨栗

```javascript
function highest(){ 
  return arguments.sort(function(a,b){ 
    return b - a; 
  }); 
} 
assert(highest(1, 1, 2, 3)[0] == 3, "Get the highest value."); 
assert(highest(3, 1, 2, 3, 4, 5)[1] == 4, "Verify the results.");
```
这个程序看起来好像没问题   
但是运行会报错，`ERROR arguments.sort is not a function`   
这里就和我们上面说的有关了，`arguments`并不是一个数组，而`sort`是`Array`对象的方法   
于是悲剧发生了，那么如何才能实现这个效果呢？   
让一个非`Array`对象调用`Array`对象的方法...   
Bingo，`call`或者`apply`

```javascript
function highest(){ 
  return makeArray(arguments).sort(function(a,b){ 
    return b - a; 
  }); 
} 
 
function makeArray(array){ 
  return Array().slice.call( array ); 
} 
 
assert(highest(1, 1, 2, 3)[0] == 3, "Get the highest value."); 
assert(highest(3, 1, 2, 3, 4, 5)[1] == 4, "Verify the results.");
```
这里作者是用`makeArray`通过`apply`复制了一份`arguments`作为`Array`对象   

# Closures 闭包
说js怎么能不提闭包～
什么是闭包，我的理解  
闭包就是这个函数加上创建这个函数时的环境   
关于闭包的理解我还是认为mdn写的不错，链接<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Closures">还是戳我</a>   
下面是作者的栗子   

```javascript
var num = 10; 
 
function addNum(myNum){ 
  return num + myNum; 
} 
 
num = 15; 
 
assert( addNum(5) == 20, "Add two numbers together, one from a closure." );
```
`addNum()`是一个基本的闭包，储存的环境就是全局参数`num`  
这个栗子里返回的值是20，也就是说  
闭包储存变量的方式是通引用记录而不是值记录，所以`num`的值也随之改变了  

```javascript
var count = 0; 
 
var timer = setInterval(function(){ 
  if ( count < 5 ) { 
    log( "Timer call: ", count ); 
    count++; 
  } else { 
    assert( count == 5, "Count came via a closure, accessed each step." ); 
    assert( timer, "The timer reference is also via a closure." ); 
    clearInterval( timer ); 
  } 
}, 100);
```
闭包在计时器中的应用
之后作者又举了一些应用，其中比较重要的，比如下面这位  

```javascript
function Ninja(){ 
  var slices = 0; 
   
  this.getSlices = function(){ 
    return slices; 
  }; 
  this.slice = function(){ 
    slices++; 
  }; 
} 
 
var ninja = new Ninja(); 
ninja.slice(); 
assert( ninja.getSlices() == 1, "We're able to access the internal slice data." ); 
assert( ninja.slices === undefined, "And the private data is inaccessible to us." );
```
实现私有变量成员`slices`   
对外接口是`getSlices`，实现了面向对象的访问控制
其中`getSlices`就是一个闭包函数，因为js的作用域链，`getSlices`内可以访问`slices`,而在外部则不能，从而实现效果  
嘛如果是公有变量直接写成`this.slices`即可  
     
睡觉...
