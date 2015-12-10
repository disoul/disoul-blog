---
title: Learning Advanced JavaScript 学习笔记(1)
tag:
    - javascript
    - web
author: disoul
date: 2015-10-13 23:00
---
首先承认自己js已经鱼到不忍直视..于是刷了一波资料..这里只是学习记录  

# Defining Functions 定义函数
第一个例子

```javascript
var canFly = function(){ return true; }; 
window.isDeadly = function(){ return true; }; 
assert( isNimble() && canFly() && isDeadly(), "Still works, even though isNimble is moved." ); 
function isNimble(){ return true; }
```
这里`isNimble`定义在第4行，但第3行依然返回true  
所以函数可以声明在任何位置，在运行之前js都会升级这些函数的声明
@@      
下一个  

```javascript
assert( typeof canFly == "undefined", "canFly doesn't get that benefit." ); 
assert( typeof isDeadly == "undefined", "Nor does isDeadly." ); 
var canFly = function(){ return true; }; 
window.isDeadly = function(){ return true; };
```
这里2个函数在执行到1 2行的时候都是未定义，原因好像有点难理解哈。。  
首先一个变量是有`值`和`声明`两个概念的，对于Js来说在运行之前都会将变量的`声明`提升至相应的域，比如这个程序是在`global域`
如果变量在函数内就是函数的`local域`，之类的  
但仅仅只是`声明`提升，`值`并没有
当程序执行到这个变量声明的位置时，才会将这个变量的值也提升至相应的域  
所以这里1 2行显示`undefined`  
恩没错也许大概就是这样  

# Named Functions命名函数
于是栗子  

```javascript
var ninja = function myNinja(){ 
  assert( ninja == myNinja, "This function is named two things - at once!" ); 
}; 
ninja(); 
assert( typeof myNinja == "undefined", "But myNinja isn't defined outside of the function." ); 
log( ninja );
```
这里我们可以看出，这种定义方式，在函数内部，变量名和函数名是一个概念，但是在函数外只有变量名有效  
     
下一波

```javascript
var ninja = { 
  yell: function(n){ 
    return n > 0 ? ninja.yell(n-1) + "a" : "hiy"; 
  } 
}; 
assert( ninja.yell(4) == "hiyaaaa", "A single object isn't too bad, either." ); 
 
var samurai = { yell: ninja.yell }; 
var ninja = null; 
 
try { 
  samurai.yell(4); 
} catch(e){ 
  assert( false, "Uh, this isn't good! Where'd ninja.yell go?" ); 
}
```
没错这里是一个递归，然而这货试图通过第二个变量`samurai`浅复制`yell`的递归调用  
然而不幸的是，这里递归调用时用的函数是`ninja.yell`自然`samurai`执行的时候`ninja`已经是`null`了  
于是解决方案

```javascript
var ninja = { 
  yell: function yell(n){ 
    return n > 0 ? yell(n-1) + "a" : "hiy"; 
  } 
}; 
assert( ninja.yell(4) == "hiyaaaa", "Works as we would expect it to!" ); 
 
var samurai = { yell: ninja.yell }; 
var ninja = {}; 
assert( samurai.yell(4) == "hiyaaaa", "The method correctly calls itself." );
```
给了ninja.yell一个函数名`yell`，递归调用时调用这个函数名自然也就没`ninja`什么事了  
还有一个比较有用的策略

```javascript
var ninja = { 
  yell: function(n){ 
    return n > 0 ? arguments.callee(n-1) + "a" : "hiy"; 
  } 
}; 
```
非常有用的一个技巧  
`arguments.callee`代表自己这个函数，也就是调用自己进行递归  

# Functions as Objects 函数对象

```javascript
var obj = {}; 
var fn = function(){}; 
obj.prop = "some value"; 
fn.prop = "some value"; 
assert( obj.prop == fn.prop, "Both are objects, both have the property." );
```
如你所见就是这样，2者实质都是一样的，并且都有自己的`property`

```javascript
function getElements( name ) { 
  var results; 
 
  if ( getElements.cache[name] ) { 
    results = getElements.cache[name]; 
  } else { 
    results = document.getElementsByTagName(name); 
    getElements.cache[name] = results; 
  } 
 
  return results; 
} 
getElements.cache = {}; 
 
log( "Elements found: ", getElements("pre").length ); 
log( "Cache found: ", getElements.cache.pre.length );
```
感觉很厉害的一种写法，给函数添加cache属性来储存缓存，思路和缓存的处理思路一样  
没记录查，查完存记录，有记录直接返回  
   
嘛今天先到这，滚去看直播了...



