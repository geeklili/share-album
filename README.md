# share-album
这是一个Flask搭建的云共享相册，支持在线上传，删除，恢复图片，支持一键清空回收站

#### 主页样例如下
![主页](./static/mk_img/web.jpg)

#### 网站分为四个页面
- 页面一：主页
- 页面二：回收站
- 页面三：每日一文
- 页面四：清空站
- 页面五：所有上传的图片
- 页面六：图片详情页

#### 使用问题
由于日常生活中基本上只能用到页面一和页面二和页面三和页面六，所以页面四和页面五被隐藏起来了，细心的道友仔细寻找可以发现，另外搭建好的网站如果不添加限制，容易被其他人员删除相关照片，现在增加了删除和旋转照片必须输入口令。

#### 新增功能
- 主页图片旋转功能，支持局部刷新；
- 直接从页面上删除/恢复照片，支持局部刷新；
- 上传照片提示等待功能；
- 上传照片重定向微信页面访问bug修复；
- 支持清空站/所有照片彻底删除的功能；
- 删除/恢复照片提示功能；
- 详情页功能

#### 函数都放在/api/view.py这个文件里面
用于视图函数的书写，把整个项目的入口变得更加简洁，把函数代码归类到一起,其中使用了蓝图注册的方式把函数放在了一起

#### 增加删除与旋转必须输入口令
![主页](./static/mk_img/pw.jpg)

#### 项目运行
项目中有两个运行文件
- run.py
- run.sh


#### 安装环境
```
$ python3.8 -m venv venv  

$ . venv/bin/activate

$ python -m pip install --upgrade pip  //使用python3.6时候pip版本对应不上出错时候使用

$ pip install -r requirements.txt


```
运行方法一[此方法用于前端运行，可以实时查看log信息]：
```
python3 run.py
```

运行方法二[此方法用于后台运行，根据项目目录下，nohup.out文件查看log信息]：
```
./run.sh  --start
./run.sh  --stop
./run.sh  --restart
```
