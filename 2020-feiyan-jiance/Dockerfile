FROM python:3.7-alpine

COPY app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 5000


CMD [ "python", "app.py" ]
