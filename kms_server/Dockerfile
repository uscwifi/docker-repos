FROM ubuntu:18.04 as builder

ADD k.sh /
RUN apt update \
	&& chmod +x /k.sh \
	&& bash k.sh debian


FROM ubuntu:18.04
EXPOSE 1688
COPY --from=builder /usr/local/kms/vlmcsd /usr/bin/vlmcsd
CMD [ "/usr/bin/vlmcsd", "-D", "-d" ]
