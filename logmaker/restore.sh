#!/bin/bash


systemctl stop logmaker

systemctl stop systemd-journald
systemctl stop rsyslog


rm /etc/rsyslog.d/logmaker.conf
rm /etc/systemd/system/logmaker.service
rm /etc/systemd/system/rsyslog.service
cp original/rsyslog.conf /etc/rsyslog.conf
cp original/journald.conf /etc/systemd/journald.conf


systemctl daemon-reload

ssystemctl restart systemd-journald
systemctl restart rsyslog



systemctl status rsyslog
systemctl status systemd-journald




