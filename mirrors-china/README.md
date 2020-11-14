## docker部署国内镜像站点列表

> 参考：[https://github.com/lework/lemonitor](https://github.com/lework/lemonitor)

### ![image-20201114095836741](https://i.loli.net/2020/11/14/2E8iyQvT4DGh9MN.png)

### docker一键部署

```bash
docker run --name mirrors-china -p 3030:80  -d uscwifi/mirrors-china

#然后浏览器输入http://ip:3030就可以访问了
```

### Dockerfile

```dockerfile
FROM node:lts-alpine as build0

COPY . /mirrors/

WORKDIR /mirrors

RUN npm install  && \
    npm run build


FROM nginx:alpine

COPY --from=build0 /mirrors/docs /usr/share/nginx/html
```

### 说明

看到原作者的这个页面挺有意思的，就拿来部署了，因为是纯静态应用，就没有使用nodejs镜像跑了，nginx足以。

如果想自己构建的话将代码克隆到本地使用`docker build`构建就可以咯


