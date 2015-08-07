#!/bin/sh

# 进行tornado配置初始化后 根据tornado配置初始化django配置，最后获得2者配置后开启nginx

dirPath=$(dirname $0);

sh $dirPath/G7PlatformStop.command;
sh $dirPath/G7PlatformStart.command;








