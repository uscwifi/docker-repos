## README
![](https://i.loli.net/2020/02/08/dHmxObSchIaWewu.png)

代码来自[佰阅](https://baiyue.one/archives/1553.html)大佬的镜像：baiyuetribe/code:yiqing2

他的镜像打包有点大，我来精简下 :laughing:

### Dockerfile(镜像115MB)

```dockerfile
FROM python:3.7-alpine

COPY app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 5000


CMD [ "python", "app.py" ]
```

### 使用方法

```bash
docker run  -d --name yiqing3 --log-opt max-size=50m --log-opt max-file=3 --restart=always -p 1234:5000 uscwifi/feiyan
```

然后打开浏览器，http://ip:1234就可以访问

