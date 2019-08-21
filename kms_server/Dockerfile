FROM ubuntu:18.04

ADD k.sh /
RUN apt update \
	&& chmod +x /k.sh \
	&& bash k.sh debian

EXPOSE 1688
CMD ["/bin/bash","/k.sh","start"]
