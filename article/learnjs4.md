---
title: Learning Advanced JavaScript 学习笔记(4)
tag:
    - web
    - javascript
author: disoul
---
# Temporary Scope 临时作用域
至于标题啥意思一开始也没弄清楚，看栗子比较直观  

```javascript
(function(){ 
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
})(); 
 
assert( typeof count == "undefined", "count doesn't exist outside the wrapper" ); 
assert( typeof timer == "undefined", "neither does timer" );
```
@@
这段栗子的标题叫Self-executing, temporary, function   
显而易见，在定义函数的时候在函数体套上`()`就可以实现这种临时函数的效果    
自执行、临时的函数    
所以这个函数内部变量的作用域也是临时的，栗子中可见在在外部访问显示`undefined`   
       
```javascript
for ( var d = 0; d < 3; d++ ) (function(d){ 
 setTimeout(function(){ 
   log( "Value of d: ", d ); 
   assert( d == d, "Check the value of d." ); 
 }, d * 200); 
})(d);
```
使用临时函数的方法在每个循环下创建参数为这个循环序号的函数    
因为闭包的特性变量d会记忆在这个函数里，从而实现效果   
             
```javascript
var myLib = (function(){ 
  function myLib(){ 
    // Initialize 
  } 
 
  // ... 
   
  return myLib; 
})();
```
封装库的一个方法   

# Function Prototypes 函数原型
什么是原型？    
对于js，每个函数都有它的原型`prototype`   
举个栗子

```javascript
function Ninja(){} 
 
Ninja.prototype.swingSword = function(){ 
  return true; 
}; 
 
var ninjaA = Ninja(); 
assert( !ninjaA, "Is undefined, not an instance of Ninja." ); 
 
var ninjaB = new Ninja(); 
assert( ninjaB.swingSword(), "Method exists and is callable." );
```
这里首先定义函数`Ninja`,如你所见只是个空壳   
但是`Ninja`拥有`prototype`属性    
这个`prototype`指向一个对象`object`，也就是这个函数的原型对象   
那么显而易见`var ninjaA = Ninja()`是不会创建对象的，不会实例化   
通过`new`实例化ninjaB，从而创建了基于`Ninja`的`NinjaB`对象    
那这是个什么过程呢？   
在了解之前先看一些函数的介绍，来自<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/prototype">Prototype from Mdn</a>    
`Object.prototype.constructor`     
Specifies the function that creates an object's prototype.    
返回一个指向创建了该对象原型的函数引用。需要注意的是，该属性的值是那个函数本身，而不是一个包含函数名称的字符串。    
所以我们可以得出，在这个程序中  
`Ninja.prototype.constructor` == `NinjaB.constructor` == `function Ninja(){}`  //始终成立
               
`Object.prototype.__proto__ `
Points to the object which was used as prototype when the object was instantiated
当对象实例化时将其指向其原型对象，也就是`Ninja.prototype`
      
呦西，接下来我们来看看对象到底是如何实例化的   

* 首先，`var ninjaB = new Ninja()`发现了野生的`new`操作符！  
* 将`ninjaB`的`__proto__`指向其原型对象`Ninja.prototype`  
* 将`ninjaB`对象作为`this`去调用`Ninja`，是指其属性方法从而初始化这个对象  
这样全新的对象`ninjaB`就创建完成了  
     
而后如果对原型对象加以修改会发生什么呢？

```javascript
function Ninja(){} 
 
Ninja.prototype.swingSword = function(){ 
  return true; 
}; 
 
var ninjaA = Ninja(); 
assert( !ninjaA, "Is undefined, not an instance of Ninja." ); 
 
var ninjaB = new Ninja(); 
assert( ninjaB.swingSword(), "Method exists and is callable." );
```
这个例子中，给原型对象增加了成员`swingSword`（略中二...
可以看到，最终创建的`ninjaB`对象也拥有了`swingSword`   
这是由于之前的`__proto__`   
`ninjaB.swingSword`实际上是`ninjaB.__proto__.swingSword`的一个引用   
      
那如果在`prototype`和函数里都定义了同名成员怎么办？

```javascript
function Ninja(){ 
  this.swingSword = function(){ 
    return true; 
  }; 
} 
 
// Should return false, but will be overridden 
Ninja.prototype.swingSword = function(){ 
  return false; 
}; 
 
var ninja = new Ninja(); 
assert( ninja.swingSword(), "Calling the instance method, not the prototype method." );
```
最终`ninja.swingSword`返回`true`  
也就是说，会返回实例的成员，而不会返回`__proto__`所指，也就是原型的成员   
在同名状况下，原型的成员会被`overridden`  
        
那既然会被覆盖，如果想利用`prototype`修改已经实例了的成员该如何？ 

```javascript
function Ninja(){ 
  this.swung = true; 
} 
 
var ninjaA = new Ninja(); 
var ninjaB = new Ninja(); 
 
Ninja.prototype.swing = function(){ 
  this.swung = false; 
  return this; 
}; 
 
assert( !ninjaA.swing().swung, "Verify that the swing method exists and returns an instance." ); 
assert( !ninjaB.swing().swung, "and that it works on all Ninja instances." );
```
如你所见,`this即可`，虽然会被覆盖，但依旧会执行
