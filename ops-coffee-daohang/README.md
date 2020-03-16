## 咖啡吧导航

> **项目来自：** [https://github.com/ops-coffee/nav](https://github.com/ops-coffee/nav)
>
> **在线访问：** [https://nav.ops-coffee.cn](https://nav.ops-coffee.cn/)

### 效果图

![](https://i.loli.net/2020/03/16/uFpKX4Wzy7vENQh.png)

### 全是静态页面，直接docker化

```dockerfile
FROM nginx:alpine

ADD . /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### **自己部署**

```bash
docker run --name daohang -d -p 8080:80 uscwifi/daohang
```


