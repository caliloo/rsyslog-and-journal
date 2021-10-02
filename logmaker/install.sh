#!/bin/bash

version=$1
rate=$2

systemctl stop logmaker
truncate --size 0 /home/work/logrotate/logs/logmaker.log

cp $version/logmaker.service /etc/systemd/system/
cp $version/rsyslog.service /etc/systemd/system/
systemctl daemon-reload
cp $version/logmaker.conf /etc/rsyslog.d/
cp $version/journald.conf /etc/systemd/journald.conf
cp $version/rsyslog.conf /etc/rsyslog.conf

echo "$rate" > rate

systemctl restart rsyslog
systemctl restart systemd-journald
sleep 3
systemctl start logmaker



systemctl status rsyslog
systemctl status logmaker
