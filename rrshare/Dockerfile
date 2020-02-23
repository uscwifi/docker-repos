FROM alpine:3.10

ENV GLIBC_VERSION=2.30-r0

RUN apk update && \
	apk --no-cache add wget libstdc++ tzdata && \
	cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
	wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
	wget -q https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \
	wget -q https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk && \
 	apk --no-cache add glibc-${GLIBC_VERSION}.apk && \
	apk --no-cache add glibc-bin-${GLIBC_VERSION}.apk && \
	mkdir -p /rrshare && \
	mkdir -p /opt/work/store && \    
	apk del wget tzdata && \
	rm -rf /glibc-${GLIBC_VERSION}.apk && \
	rm -rf /glibc-bin-${GLIBC_VERSION}.apk && \
        rm -rf /var/cache/apk/* /root/.wget-hsts

COPY rrshareweb /rrshare/rrshareweb

WORKDIR /opt/work/store
VOLUME ["/opt/work/store"]
EXPOSE 3001 

CMD ["sh", "-c", "/rrshare/rrshareweb/rrshareweb"]
