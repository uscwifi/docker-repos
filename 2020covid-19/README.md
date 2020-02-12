##  2019-ncov

>  **项目来自：** [https://github.com/shfshanyue/2019-ncov](https://github.com/shfshanyue/2019-ncov)
>
> **全国新型冠状病毒，肺炎疫情实时省市地图** [https://ncov.shanyue.tech](https://ncov.shanyue.tech/)
>
> **预览地址2：** ncov.uscwifi.xyz

**具体项目详情请参考：**  [https://github.com/shfshanyue/2019-ncov](https://github.com/shfshanyue/2019-ncov)

**本文只是对该项目的简单Docker化，没有多少技术含量**

### 效果图

![ncov.png](https://i.loli.net/2020/02/12/5gNMlZTxu4kJodW.png)

### Dockerfile

```bash
FROM node:lts-alpine

COPY 2019-ncov /app

WORKDIR /app

RUN npm config set registry https://registry.npm.taobao.org && \
  npm  install && \
  node scripts/build-origin.js

EXPOSE 5000


CMD [ "npm", "start" ]
```

### 使用方法

**首先运行容器：** 

```bash
docker run -d --name covid-19 -p 30002:3000 uscwifi/covid-19
```

**然后设置计划任务**

```bash
echo '*/30 * * * * /usr/bin/docker exec -it covid-19 node scripts/build-origin.js &> /dev/null' >> /var/spool/cron/root 
```

**然后浏览器访问http://宿主机IP:30002** 

### 删除容器和计划任务

```bash
# 删除容器
docker rm -f covid-19 
# 删除计划任务
sed '/docker exec -it covid-19 node scripts\/build-origin.js/d'  /var/spool/cron/root -i
```


