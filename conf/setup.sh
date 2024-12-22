#!/bin/sh
envsubst < ${PROJECT_ROOT}/conf/dnsmasq.conf.tpl > /etc/dnsmasq.conf
