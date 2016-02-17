---
title: 使用cocos2dx-x3.0的物理引擎实现碰撞检测
tag:
    - cocos2dx
author: disoul
date: 2015-05-28 11:00
---
前几天帮人写了一个小游戏因为传统rect碰撞检测写起来太麻烦于是研究了下自带的物理引擎碰撞检测  

##首先创建物理世界

在.h文件添加如下代码  

```c++
void setPhyWorld(PhysicsWorld* world){m_world = world;}
private:
    PhysicsWorld* m_world;
```

其中第一行中可以添加代码来规定物理世界的一些属性  
如 重力  

```c++
m_world->setGravity(Vec2(0,0)); //取消重力
```
@@
-----------------------------

在.cpp文件添加如下代码  

```c++
#include "HelloWorldScene.h"

Scene* HelloWorld::createScene()
{
    auto scene = Scene::createWithPhysics();
    scene->getPhysicsWorld()->setDebugDrawMask(PhysicsWorld::DEBUGDRAW_ALL);//开启DEBUG模式，会绘制模型边缘关节等
    auto layer = HelloWorld::create();
    layer->setPhyWorld(scene->getPhysicsWorld());
    scene->addChild(layer);
    return scene;   
}
bool HelloWorld::init()
{
    if ( !Layer::init() )
    {
        return false;
    }
    return true;
}
```

通过createWithPhysics()方法创建一个带有物理效果的Scene，然后将需要添加物理效果的层加入其中  

##创建物理边界

```c++
Size visibleSize = Director::getInstance()->getVisibleSize();
auto body = PhysicsBody::createEdgeBox(visibleSize, PHYSICSBODY_MATERIAL_DEFAULT, 3);
auto edgeNode = Node::create();
edgeNode->setPosition(Point(visibleSize.width/2,visibleSize.height/2));
edgeNode->setPhysicsBody(body);
scene->addChild(edgeNode);
```

PhysicsWorld有很多工厂方法，如createEdgeBox创建一个矩形的边框，所有的参数是：

* 矩形区域，设置作为visibleSize
* 可选参数，纹理，默认为PHYSICSBODY_MATERIAL_DEFAULT
* 可选参数，边框大小，默认为1

##设置精灵为刚体

和大多数物理引擎一样，物件只有成为刚体才能受到物理世界的影响

```c++
void HelloWorld::addBoxBodyForSprite(Sprite* sprite)
{
	auto body = PhysicsBody::createBox(sprite->getContentSize());
	body->setDynamic(true);

	body->setContactTestBitmask(0xFFFFFFFF); //设置刚体的接触测试掩码，即所有掩码位为1
	sprite->setPhysicsBody(body);
}
```

如果两个物体的接触测试掩码（ContactTestBitmask）执行“逻辑与”运算，如果结果为非零值，表明这两个物体会触发碰撞检测事件。默认值是0x00000000，表示清除所有掩码位，0xFFFFFFFF表示所有掩码位都设置为1。  
除了接触测试掩码（ContactTestBitmask）外，物理引擎中还定义了类别掩码（CategoryBitmask）和碰撞掩码（CollisionBitmask），它们的作用是当两个物体接触时候是否发生“碰撞反应”，“碰撞反应”会表现为一个物体受到另外物体的碰撞，而改变运动方向。由于两个物体是“刚体”，在碰撞的时候两个物体不会交叉。  

* 类别掩码 body->setCategoryBitmask(int bitmask)
* 碰撞掩码 body->setCollisionBitmask(int bitmask)
* 接触测试掩码 body->setContactTestBitmask(int bitmask)

类别掩码（CategoryBitmask）与碰撞掩码（CollisionBitmask）决定了物体能否发生“碰撞反应”。而接触测试掩码（ContactTestBitmask）的设置，能够检测是否发生接触发生，并且触发EventListenerPhysicsContact监听事件。 接触测试掩码与类别掩码和碰撞掩码没有什么关联。  

##注册碰撞监听事件

Cocos2d-x3.0中，事件派发机制做了重构，所有事件均有事件派发器统一管理。物理引擎的碰撞事件也不例外  
下面的代码注册碰撞begin回调函数。  

```c++
void HelloWorld::onEnter()
{
    Layer::onEnter();

    auto contactListener = EventListenerPhysicsContact::create();
    contactListener->onContactBegin = CC_CALLBACK_2(HelloWorld::onContactBegin, this);

    auto dispatcher = Director::getInstance()->getEventDispatcher();

    dispatcher->addEventListenerWithSceneGraphPriority(contactListener, this);
}

bool HelloWorld::onContactBegin(EventCustom* event, const PhysicsContact& contact)
{
    auto spriteA = (Sprite*)contact.getShapeA()->getBody()->getNode();
    auto spriteB = (Sprite*)contact.getShapeB()->getBody()->getNode();

    CCLOG("Contact!!");

    return true;
}
```

如果一切顺利精灵碰撞时将会打印Contact！
这里根据cocos2dx版本的不同回调函数回有所不同，在我测试的r1版本里，onContactBegin函数没有event参数  
所以注册回调函数的时候使用 CC_CALLBACK_1 
