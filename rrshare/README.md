
## 人人影视docker打包

> [alipne镜像的相关知识](https://yeasy.gitbooks.io/docker_practice/content/cases/os/alpine.html)
>
> [Alpine镜像中not found引出的gnu libc和musl libc的争论](https://blog.csdn.net/liumiaocn/article/details/89702529)
>
> [alpine-pkg-glibc的github项目地址](https://github.com/sgerrand/alpine-pkg-glibc)
>
> [Alpine support - musl libc](https://github.com/ibmdb/node-ibm_db/issues/217)

## 项目说明
这个部署好是用来下载人人影视的视频的，下载到linux服务器上，配合ilemonrain/h5ai可以实现网页播放视频

## 使用方法
**首先**
```
docker run --name rrys -d -p 3001:3001 -v /opt/rrys-data:/opt/work/store   uscwifi/rrshare:latest
```
**然后**  

浏览器访问http://ip:3001


关于libstdc++，参考了：[https://www.kxxzz.com/mgvps/73324.html](https://www.kxxzz.com/mgvps/73324.html)

没想到它这个要用到libstdc++，直接alpine镜像报错也不知道是缺啥玩意儿

**默认登陆密码：123456**

![](https://i.loli.net/2020/02/23/o8Fs2Yf6XBOnqiP.png)

**之前看过别人文章，照猫画虎写过一个制作带glibc的alpine镜像：** [https://blog.51cto.com/14012942/2446376](https://blog.51cto.com/14012942/2446376) 现在看看好像有点问题，那个`jlesage/baseimage`的镜像不能直接用，还得dockerfile制作,不确定libstdc++其他项目也是必须要的...


人人影视的代码下载地址：[http://app.rrys.tv/](http://app.rrys.tv/)

目前的真实下载地址：[http://appdown.rrys.tv/rrshareweb_centos7.tar.gz](http://appdown.rrys.tv/rrshareweb_centos7.tar.gz)


