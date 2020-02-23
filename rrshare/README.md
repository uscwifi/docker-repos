
## 人人影视docker打包

> [alipne镜像的相关知识](https://yeasy.gitbooks.io/docker_practice/content/cases/os/alpine.html)
>
> [Alpine镜像中not found引出的gnu libc和musl libc的争论](https://blog.csdn.net/liumiaocn/article/details/89702529)
>
> [alpine-pkg-glibc的github项目地址](https://github.com/sgerrand/alpine-pkg-glibc)
>
> [Alpine support - musl libc](https://github.com/ibmdb/node-ibm_db/issues/217)

关于libstdc++，参考了：[https://www.kxxzz.com/mgvps/73324.html](https://www.kxxzz.com/mgvps/73324.html)

没想到它这个要用到libstdc++，直接alpine镜像报错也不知道是缺啥玩意儿

**默认登陆密码：123456**

![](https://i.loli.net/2020/02/23/o8Fs2Yf6XBOnqiP.png)

**之前看过别人文章，照猫画虎写过一个制作带glibc的alpine镜像：** [https://blog.51cto.com/14012942/2446376](https://blog.51cto.com/14012942/2446376) 现在看看好像有点问题，那个`jlesage/baseimage`的镜像不能直接用，还得dockerfile制作,不确定libstdc++其他项目也是必须要的...
