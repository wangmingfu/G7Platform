#!/bin/sh

dirPath=$(cd `dirname $0`; pwd);

sudo mysql.server stop;
# 杀死存在的进程
sudo python3 $dirPath/tools/kill_process.py;
