#-*- coding: utf-8 -*-
__author__ = 'yuyang'
import json
from G7Platform.profile.settings.web.G7Results import G7ResultDic


class G7ResultManager:

    #单例设计模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst=super(G7ResultManager,cls).__new__(cls,*args,**kwargs)
        return cls._inst

    def resultErrorDataWrapperToJson(self, code, data={}):

        retDic = {}
        if type(code) == type(""):
            try:
                code = int(code)
            except:
                return retDic
        if code in list(G7ResultDic.keys()):
            retDic = {
                "code":code,
                "message":G7ResultDic[code],
                "data":data
            }

        return retDic

    def resultErrorDataWrapperToJsonString(self, code, data={}):

        retDic = {}
        if type(code) == type(""):
            try:
                code = int(code)
            except:
                return json.dumps(retDic)

        if code in G7ResultDic.keys():
            retDic = {
                "code":code,
                "message":G7ResultDic[code],
                "data":data
            }

        return json.dumps(retDic)


    def resultSuccessDataWrapperToJson(self, message, data={}):

        retData = {}
        retDic = {
                "code":0,
                "message":message,
                "data":data
            }

        return retDic