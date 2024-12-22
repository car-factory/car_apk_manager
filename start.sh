#!/bin/sh
# startup config here

/bin/sh /setup.sh
/usr/bin/supervisord -c /etc/supervisord.conf
