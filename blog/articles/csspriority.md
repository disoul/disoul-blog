Css规则的优先级
css web
今天写css踩了一波坑，于是记录下css的优先级规则  
# 样式的优先级
也就是css写在哪里优先级比较高   
其中按照下表排序  

* 内联样式最高，也就是写在标签的style里的样式
* 内部样式和外联样式谁后出现谁优先级高

也就是如果

```html
<style>
...
</style>
<link rel="stylesheet" type="text/css" href="233.css"/> 
<!-- 此时外联样式覆盖内部样式 -->

```
@@
# 选择器的优先级
主要就是踩在这里了。。。   
对于css，选择器有`权值`一说   

* 内联样式，  权值1000
* id选择器，  权值100
* 类选择器，  权值10
* 元素选择器，权值1

对于同一个元素如果有不同的选择器选中它    
生效的只有`权值最大`的那个选择器下的规则
如果权值相同，则按照后出现的规则覆盖前一个规则  
如 

```scss
#main-scene .left-list {
  .... //权值为 100 + 10 = 110
}

#mask {
  .... //权值为 100
}
```

所以如果对于元素`<div id="main-scene"><div class="left-list" id="mask"></div></div>`   
生效的只有第一个选择器   
