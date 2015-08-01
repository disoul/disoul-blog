# Context 上下文
感觉这一章比较难以理解，但应该也是很重要的一章  
在学习之前先了解，Context(上下文)是个什么鬼  
按照我现在的理解方法，就是每个对象在不同的域内有不同的context  
context体现在this对象上，就好像在代码的不同区域this所指向的对象不同一样  
举个栗子  

```javascript
var a = function(){
  setTrue: function(){
    this.flag = true;
  }
  setFalse: function(){
    this.flag = false;
  } //在这2个方法里，this是指向a的
    //但是js可以轻松地改变this的指向，也就是修改上下文
}
```
@@
```javascript
assert(a.flag == null, '可以看到，虽然a对象创建了，但是在调用方法之前a.flag都不存在');
a.setTrue();
assert(a.flag == true, '注意我们是通过a.setTrue调用的，也就是说此时上下文是a
                        执行方法的时候，this指的也是a');
window.setFalse = a.setFalse; //window对象可以理解为一个全局对象的概念
                              //js中所有全局对象都是window的属性
window.setFalse();//此时在setFalse中this就指向了window而不是a，上下文变成了window
                  //所以下面2句应该就能理解了
assert((a.flag == true)&&(window.flag == false));
```
上面只是理解上下文的举例  
更改上下文在js里一般用到`call`和`apply`，具体见下面栗子  

```javascript


var object = {}; 
function fn(){ 
  return this; 
} 
assert( fn() == this, "The context is the global object." ); 
assert( fn.call(object) == object, "The context is changed to a specific object." );
```
这里`call`是指fn执行object方法，也就是={}，所以返回object  
`call`方法是js里非常重要的一种方法  
语法`fun.call(thisArg[, arg1[, arg2[, ...]]])`
其中`thisArg`指的是执行方法时的上下文，也就是this的指向  
具体定义可以参照mdn的`call`条目，<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/call">戳这里</a>  
   
除了`call`以外还有一个类似作用的方法`apply`，于是又是栗子  

```javascript
function add(a, b){ 
  return a + b; 
} 
assert( add.call(this, 1, 2) == 3, ".call() takes individual arguments" ); 
assert( add.apply(this, [1, 2]) == 3, ".apply() takes an array of arguments" );
```
可以看出`apply`只接受一个数组作为后面的参数，而`call`可以跟任意数量的参数  
下面这个栗子，举例了使用call来更改方法调用的上下文

```javascript
function loop(array, fn){ 
  for ( var i = 0; i < array.length; i++ ) 
    fn.call( array, array[i], i ); 
} 
var num = 0; 
loop([0, 1, 2], function(value, i){ 
  assert(value == num++, "Make sure the contents are as we expect it."); 
  assert(this instanceof Array, "The context should be the full array."); 
});
```
这里`fn.call`时指定的第一个参数是`array`，也就是一个`Array`对象  
所以倒数第二行里在执行的时候`this instanceof Array`返回true  

# Instantiation 实例
栗子  

```javascript
function Ninja(){ 
  this.name = "Ninja"; 
} 
 
var ninjaA = Ninja(); 
assert( !ninjaA, "Is undefined, not an instance of Ninja." ); 
 
var ninjaB = new Ninja(); 
assert( ninjaB.name == "Ninja", "Property exists on the ninja instance." );
```
这个例子里，`ninjaA`虽然写了定义没有实例，而通过`new`创建的`ninjaB`才拥有实例，从而拥有了方法属性    
下面的栗子

```javascript
function Ninja(){ 
  this.swung = false; 
   
  // Should return true 
  this.swingSword = function(){ 
    this.swung = !this.swung; 
    return this.swung; 
  }; 
} 
 
var ninja = new Ninja(); 
assert( ninja.swingSword(), "Calling the instance method." ); 
assert( ninja.swung, "The ninja has swung the sword." ); 
 
var ninjaB = new Ninja(); 
assert( !ninjaB.swung, "Make sure that the ninja has not swung his sword." );
```
意思大概就是不同实例的this对应不同对象，互不影响  
next  

```javascript
function User(first, last){ 
  this.name = first + " " + last; 
} 
 
window.name = "Resig"; 
var user = User("John", name); 
 
assert( name == "John Resig", "The name variable is accidentally overridden." );
```
注意，这段代码在创建`user`时并没有使用`new`操作符  
所以`user`是没有实例的，但是从结果来看  
`User`里的代码被执行了，因为改变的量是`window.name`   
所以在执行这段代码时，上下文是全局  
这和`new`的区别在于，通过`new`创建的对象  
执行方法时上下文指的是本身创建的对象而不是全局  
     
所以下面作者给出了这段代码

```javascript
function User(first, last){ 
  if ( !(this instanceof User) ) 
    return new User(first, last); 
   
  this.name = first + " " + last; 
} 
 
var name = "Resig"; 
var user = User("John", name); 
 
assert( user, "This was defined correctly, even if it was by mistake." ); 
assert( name == "Resig", "The right name was maintained." );
```
即在执行方法是判断上下文，如果不是这个对象，则自己添加`new`操作符创建   
防止自己手滑么...   
      
明天再更
