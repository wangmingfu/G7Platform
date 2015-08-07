# -*- coding: utf-8 -*-
__author__ = 'yuyang'

from G7Platform.G7Globals import *

def start_g7platformshell():
	shellString = django_manage_path+" shell"
	os.system(shellString)


if __name__ == '__main__':
	start_g7platformshell()