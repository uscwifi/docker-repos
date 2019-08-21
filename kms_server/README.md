# kms_server服务器

> 局域网也可以使用的，服务器上也可以跑

## 一、运行容器：

```
docker run --name kms_server -d -p 1688:1688 uscwifi/kms_server:v1.7
```



## 二、查看下日志怎么使用

```
docker logs kms_server
```





## 三、关于Dockerfile

```
FROM ubuntu:18.04

ADD k.sh /
RUN apt update \
	&& chmod +x /k.sh \
	&& bash k.sh debian

EXPOSE 1688
CMD ["/bin/bash","/k.sh","start"]
```


