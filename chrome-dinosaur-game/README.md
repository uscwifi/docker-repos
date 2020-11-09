## Chrome离线小恐龙游戏

> 原作者代码地址：[https://github.com/justjavac/chrome-t-rex-game](https://github.com/justjavac/chrome-t-rex-gam

![](https://i.loli.net/2020/11/09/rqcIQs2klNSuYBK.png)

### 一键docker部署

```bash
docker run -d --name chrome-game -p 10086:80 uscwifi/chrome-game
```

### Dockerfile参考

**纯静态页面，直接copy到nginx**

```dockerfile
FROM nginx:alpine

COPY . /usr/share/nginx/html/

EXPOSE 80
```


