---
title: 使用Nginx实现Node反向代理
tag:
    - web
    - node.js
author: disoul
---

最近为了学node写了一个node的项目,部署到服务器上时使用了这个方法，在此做下记录    

# 反向代理
所谓反向代理，简单理解就是，我的`node`跑在8080端口，而nginx监听的是80端口   
使用反向代理后，当向80端口发送请求后，nginx会将这个请求转发给8080端口  
同时将`response`也返回
@@
# nginx配置
`nginx`这个命令倒没多少选项，大多数都是配置文件所控制  
`nginx -t` 测试但不运行自己的配置文件，同时也会输出自己配置文件的位置  
比如我`/etc/nginx/nginx.conf`  
那么下面  

```shell
cd /etc/nginx/sites-enable/
vim node_nginx.conf
```
直接贴上我的配置文件

```config
upstream nodejs{
        server 127.0.0.1:3000;
        #server 127.0.0.1:3001;
        keepalive 64;
}
server {
        listen 80;
        server_name www.moive.me moive.me;
        access_log /var/log/nginx/moiveme.log;
        location / {
                proxy_set_header   X-Real-IP            $remote_addr;
                proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
                proxy_set_header   Host                   $http_host;
                proxy_set_header   X-NginX-Proxy    true;
                proxy_set_header   Connection "";
                proxy_http_version 1.1;
                proxy_pass         http://nodejs;
                root ...;
                index ...;
        }
}
```
很容易可以看出，上游接受来自node8080端口的信息并且将80`proxy_pass`到上游   
然后重启nginx服务`sudo /etc/init.d/nginx restart`    
运行node服务监听8080端口   
还有一点，在服务器端需要使用forever命令来守护node进程   
`npm install forever -g`   
`forever xxx.js`
