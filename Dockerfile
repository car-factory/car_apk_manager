FROM alpine:3.21
LABEL maintainer="0623 <hi@inn-df.com>" \
      version="0.5.1"

ARG ENTRY_IP="127.0.0.1"
ARG DJANGO_ENV=develop

ENV DJANGO_MODE=${DJANGO_ENV} \
    PROJECT_ROOT="/opt/car_apk_manager"

ADD . ${PROJECT_ROOT}
WORKDIR ${PROJECT_ROOT}

RUN sed -i 's#https\?://dl-cdn.alpinelinux.org/alpine#https://mirrors.tuna.tsinghua.edu.cn/alpine#g' /etc/apk/repositories

RUN apk update && \
        apk add --no-cache --no-progress dnsmasq supervisor \
            nginx openssl gettext py3-pip && \
        python3 -m venv .py3 && \
        . .py3/bin/activate && \
        pip3 install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple -r requirements.txt && \
        mkdir -pv /var/log/car-web/ \
            /opt/apk/ \
            ${PROJECT_ROOT}/statics/ \
            /etc/supervisor/conf.d/ \
            /etc/nginx/ssl && \
        cp -p conf/nginx.conf /etc/nginx/ && \
        cp -p conf/supervisord.conf /etc/ && \
        cp -p conf/supervisor/*.conf /etc/supervisor/conf.d/ && \
        cp -p conf/setup.sh / && \
        cp -p start.sh /

# * config car_apk_manager project *
RUN . .py3/bin/activate && \
    python manage.py collectstatic --noinput && \
    python manage.py showmigrations && \
    python manage.py migrate

# * config dnsmasq&ngx ssl *
RUN envsubst < ${PROJECT_ROOT}/conf/dnsmasq.conf.tpl > /etc/dnsmasq.conf && \
    sh conf/gen_ssl.sh

CMD ["/start.sh"]
# CMD /usr/bin/supervisord -c /etc/supervisord.conf
