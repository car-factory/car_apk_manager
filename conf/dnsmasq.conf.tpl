# https://github.com/jpillora/docker-dnsmasq/tree/master
# git@github.com:jpillora/docker-dnsmasq.git

cache-size=10000
log-queries
log-facility=/var/log/dnsmasq.log
local-ttl=600
strict-order
no-resolv
server=114.114.114.114
address=/dzsms.gwm.com.cn/${ENTRY_IP}
