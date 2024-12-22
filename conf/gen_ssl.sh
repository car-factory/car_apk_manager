#!/bin/sh

openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
    -subj "/C=CN/ST=Beijing/L=Beijing/O=MyOrg/OU=MyUnit/CN=dzsms.gwm.com.cn" \
    -keyout /etc/nginx/ssl/server.key \
    -out /etc/nginx/ssl/server.crt
