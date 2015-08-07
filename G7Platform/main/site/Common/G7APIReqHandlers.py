#-*- coding: UTF-8 -*-
__author__ = 'helios'
'''
    该类作为接口基类
'''

from Account.models import G7User
from G7Platform.main.site.Common.G7ReqHandlers import *

class G7APIReqHandler(G7ReqHandler):
    """api请求基类"""

    @property
    def current_user(self):
        doc = "The current_user property."
        if "userid" in self.httpHeadersJson.keys():
            userid = self.httpHeadersJson["userid"]
            try:
                user = G7User.objects.get(userid=userid)
                return user
            except G7User.DoesNotExist:
                return None
        return None

    @property
    def is_login(self):
        deviceid = self.httpHeadersJson["deviceid"]
        usignature = self.httpHeadersJson["usignature"]
        userid = self.httpHeadersJson["userid"]
        if len(deviceid) > 0 and len(usignature) > 0 and len(userid) > 0 and userid is not None and deviceid is not None and usignature is not None:
            queryList = [
                "usignature"
            ]
            condition = "userid == {userid} && deviceid == '{deviceid}'".format(userid=userid, deviceid=deviceid)
            dbUsignature = self.dbGet(queryList, condition)
            return True
        else:
            return False

    
