#-*- coding: UTF-8 -*-
__author__ = 'yuyang'

from xml.dom.minidom import Document
from G7Platform.profile.settings.G7Settings import *
from G7Platform.profile.settings.web.G7URLs import *

class G7Profile:

    database = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst=super(G7Profile,cls).__new__(cls,*args,**kwargs)
        return cls._inst

    def __init__(self):

        # 测试模式
        self.debug = debug
        # 路径配置信息
        self.template_path = template_path
        self.static_path = static_path
        self.media_path = media_path
        self.project_path = project_path
        self.subproject_path = subproject_path
        self.project_name = project_name
        self.django_path = django_path
        self.django_project_name = django_project_name
        self.nginx_conf_path = nginx_conf_path
        self.nginx_path = nginx_path
        self.nginx_g7_conf_path = nginx_g7_conf_path
        self.log_path = log_path
        self.release_django_port = release_django_port
        self.release_tornado_port = release_tornado_port
        self.debug_tornado_port = debug_tornado_port
        self.debug_django_port = debug_django_port
        self.tornado_ports = tornado_ports
        self.profile_path = profile_path
        self.tornado_log_path = tornado_log_path

        self.dbname = dbname
        self.dbhost = dbhost
        self.dbuser = dbuser
        self.dbpassword = dbpassword

        # url链接配置
        self.urlList = urlList

        # 数据库服务启动

        # 全局定义
        self.defineMacro()

        # admin 配置初始化
        self.adminProfile()

    def defineMacro(self):
        pass

    def log(self, log):
        with open(path.join(log_path,"{log_name}.log".format(log_name=project_name)), "a") as f:
            logStr = "{project_name} Log At {datetime}: {log}\n".format(project_name=project_name,datetime=str(datetime.datetime.now()),log=str(log))
            f.write(logStr)

    def adminProfile(self):
        g7AdmingXmlPath = os.path.join(self.project_path,"workspace/profile/uwsgi/"+django_project_name+"_profile.xml")

        host = "127.0.0.1"
        port = release_django_port
        listen = 80
        pythonpath1 = self.project_path 	# G7Platform
        pythonpath2 = self.subproject_path
        pythonpath3 = self.subproject_path+"/main/"+django_project_name+"/"+django_project_name+"/"
        pythonpath4 = self.subproject_path+"/main/"+django_project_name+"/"
        pidfile = path.join(nginx_path,"pid/nginx.pid")
        limit_as = 300
        daemonize = self.log_path + "/django/django.log"   # logpath

        childrenNodes = {
            "chdir":django_path,
            "socket":host+":"+str(port),
            "listen":str(listen),
            "master":"true",
            "pidfile":pidfile,
            "processes":"8",
            "pythonpath1":pythonpath1,
            "pythonpath2":pythonpath2,
            "pythonpath3":pythonpath3,
            "pythonpath4":pythonpath4,
            "module":"wsgi",
            "profiler":"true",
            "memory-report":"true",
            "enable-threads":"true",
            "logdate":"true",
            "limit-as":str(limit_as),
            "daemonize":daemonize,
            }

        def g7AdminXmlBuilder(nodes={}, rootNodeName="", xmlpath=""):

            doc = Document()
            rootNode = doc.createElement(rootNodeName)
            doc.appendChild(rootNode)
            for keyName in list(nodes.keys()):
                if "pythonpath" in keyName:
                    keyNode = doc.createElement("pythonpath")
                    valueNode = doc.createTextNode(nodes[keyName])
                    keyNode.appendChild(valueNode)
                    rootNode.appendChild(keyNode)
                else:
                    keyNode = doc.createElement(keyName)
                    valueNode = doc.createTextNode(nodes[keyName])
                    keyNode.appendChild(valueNode)
                    rootNode.appendChild(keyNode)

            f = open(xmlpath,'w')
            f.write(doc.toprettyxml())
            f.close()

        g7AdminXmlBuilder(childrenNodes, "uwsgi", g7AdmingXmlPath)
