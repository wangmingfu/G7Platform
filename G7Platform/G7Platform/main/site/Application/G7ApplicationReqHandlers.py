#-*- coding: utf-8 -*-

import io
import zipfile
import plistlib
import uuid
import sys
import time
import json
import mimetypes
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
if sys.version_info.major == 3:
    from http.client import HTTPConnection
else:
    from httplib import HTTPConnection

import tornado
import tornado.web

from Application.models import G7Application, G7Project
from Account.models import G7User
from G7Platform.main.site.Common.G7APIReqHandlers import G7APIReqHandler
from G7Platform.main.site.Common.G7ReqHandlers import G7ReqHandler
from G7Platform.G7Globals import *
from django.core.files.base import ContentFile
from django.conf import settings

class G7ApplicationPgyerUploader():

	def __init__(self):

		self.domain = ""
		self.urlPath = ""
		self.uKey = ""
		self.api_key = ""
		self.ipaFile = ""
		self.installPassword = ""
		self.mail_receiver = []
		self.product_name = ""
		self.build_version = ""
		self.project_version = ""
		self.currentG7User = None

	def fileSize(self, byteSize):

		if byteSize >= 1024 and byteSize < 1024*1024:
			return str(byteSize*1.0/1024)+"KB"

		elif byteSize >= 1024*1024 and byteSize < 1024*1024*1024:
			return str(byteSize*1.0/1024/1024)+"MB"

		elif byteSize >= 1024*1024*1024 and byteSize < 1024*1024*1024*1024:
			return str(byteSize*1.0/1024/1024/1024)+"GB"

		return str(byteSize)+"B"

	#请求字典编码
	def _encode_multipart(self, params_dict):
	    boundary = '----------%s' % hex(int(time.time() * 1000))
	    data = []
	    for k, v in params_dict.items():
	        data.append('--%s' % boundary)
	        if hasattr(v, 'read'):
	            filename = getattr(v, 'name', '')
	            content = v.read()
	            decoded_content = content.decode('ISO-8859-1')
	            data.append('Content-Disposition: form-data; name="%s"; filename="kangda.ipa"' % k)
	            data.append('Content-Type: application/octet-stream\r\n')
	            data.append(decoded_content)
	        else:
	            data.append('Content-Disposition: form-data; name="%s"\r\n' % k)
	            data.append(v if isinstance(v, str) else v.decode('utf-8'))
	    data.append('--%s--\r\n' % boundary)
	    return '\r\n'.join(data), boundary

	#处理 蒲公英 上传结果
	def handle_resule(self, result, mail_receiver):
		json_result = json.loads(result)
		if json_result['code'] is 0:
			return self.send_Email(json_result, mail_receiver)
		else:
			return G7ReqHandler.responseDataText(10003)

	#发送邮件
	def send_Email(self, json_result, mail_receiver):
		if len(mail_receiver) == 0:
			return G7ReqHandler.responseDataText(10005)

		appName = json_result['data']['appName']
		appKey = json_result['data']['appKey']
		appVersion = json_result['data']['appVersion']
		appBuildVersion = json_result['data']['appBuildVersion']
		appShortcutUrl = json_result['data']['appShortcutUrl']
		appIconKey = json_result['data']['appIcon']
		appFileSize  = json_result['data']['appFileSize']
		appIdentifier = json_result['data']['appIdentifier']
		appUpdated = json_result['data']['appUpdated']
		appCreated = json_result['data']['appCreated']

		#根据不同邮箱配置 host，user，和pwd
		
		if self.currentG7User != None and self.currentG7User.mail_pwd and self.currentG7User.mail_pwd != "":
			domain = self.currentG7User.email.split("@")[1]
			mail_host = "smtp."+domain
			mail_user = self.currentG7User.email
			mail_username = self.currentG7User.username
			mail_pwd = self.currentG7User.mail_pwd
		else:
			mail_host = 'smtp.163.com'
			mail_user = 'helios@163.com'
			mail_username = 'helios'
			mail_pwd = '*******'

		mail_to = ','.join(mail_receiver)
		mail_smtpPort = '25'
		mail_sslPort  = '465'

		msg = MIMEMultipart()

		appInstallUrl = 'http://www.pgyer.com/' + str(appShortcutUrl)
		appIconUrl = 'http://pgy-app-icons.qiniudn.com/image/view/app_icons/' + str(appIconKey)
		appQRCodeUrl = 'http://qr.liantu.com/api.php?text=' + str(appInstallUrl)
		appATOInstallUrl = 'itms-services://?action=download-manifest&url=https://ssl.pgyer.com/app/plist/' + str(appKey)

		environsString = '<table width="700" border="0" cellpadding="0" cellspacing="0" align="center">'
		environsString += '<tbody><tr>'
		environsString += '     <td width="100%" style="" align="center" bgcolor="#f7f7f7">'
		environsString += '         <table border="0" cellpadding="0" cellspacing="0" align="center" style="width:100%;">'
		environsString += '             <tbody><tr>'
		environsString += '                 <td valign="top" class="ecxleft" style="width:100%;">'
		environsString += '                     <table border="0" cellpadding="15" cellspacing="0" width="100%" bgcolor="#F6F6F6">'
		environsString += '                         <tbody><tr>'
		environsString += '                             <td>'
		environsString += '                                 <table border="0" cellpadding="0" cellspacing="0" width="100%">'
		environsString += '                                      <tbody><tr>'
		environsString += '                                         <td align="left" width="65">'
		environsString += '                                             <img src="' + str(appIconUrl) + '" style="width:50px;height:50px;border-radius:10px;border-radius:10px;border:1px solid #ddd;">'
		environsString += '                                         </td> '
		environsString += '                                         <td align="left">'
		environsString += '                                             <font color="#55555" size="3" style="font-size:16px;"><b>' + str(self.product_name) + '</b></font><br>'
		environsString += '                                             <font color="#55555" size="2" style="font-size:14px;">版本 ' + str(appVersion) + ' (build ' + str(self.build_version) +  ')</font>'
		environsString += '                                         </td>'
		environsString += '                                         <td width="50">'
		environsString += '                                             <font color="#55555" face="Trebuchet MS,Arial" size="3">'
		environsString += '                                             <a href="' + str(appATOInstallUrl) + '" target="_blank" style="background-color:#56bc94;display:inline-block;font-size:14px;width:90px;height:32px;text-align:center;line-height:32px;color:white;text-decoration:none;font-weight:bold;">设备直接安装</a>  '
		environsString += '                                             </font>'
		environsString += '                                         </td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table>'

		environsString += '<h3>构建包信息</h3><p>'
		# environsString += '<p>ipa 包下载地址 : ' + '暂不提供' + '<p>'
		environsString += '<p>构建版本号 : ' + self.project_version + '<p>'
		environsString += '<p>App名称 : ' + str(self.product_name) + '<p>'
		environsString += '<p>BundleId : ' + str(appIdentifier) + '<p>'
		environsString += '<p>App文件大小 : ' + str(self.fileSize(int(appFileSize))) + '<p>'
		environsString += '<p>版本号 : ' + str(appVersion) + '<p>'
		environsString += '<p>上传时间 : ' + str(appCreated) + '<p>'
		environsString += '<p>更新时间 : ' + str(appUpdated) + '<p>'
		environsString += '<p>在线安装 : ' + 'http://www.pgyer.com/' + str(appShortcutUrl) + '   密码 : ' + self.installPassword + '<p>'
		environsString += '<p>二维码安装 :<p>'
		environsString += '<p><img src="' + str(appQRCodeUrl) + '" style="width:100px;height:100px;border-radius:10px;border-radius:10px;border:1px solid #ddd;"><p>'

		message = environsString
		body = MIMEText(message, _subtype='html', _charset='utf-8')
		msg.attach(body)
		msg['To'] = mail_to
		msg['from'] = mail_user
		msg['subject'] = '[测试]'+ self.product_name + '_v' + appVersion + '_' + self.build_version

		try:
			s =  smtplib.SMTP_SSL(mail_host, mail_sslPort)
			s.ehlo()
			s.login(mail_user, mail_pwd)
			s.sendmail(mail_user, mail_receiver, msg.as_string())
			s.quit()
			return G7ReqHandler.responseDataText(0, "打包成功", {})#self.responseWrite(0, "打包成功", {})
		except Exception as e:
			return G7ReqHandler.responseDataText(10004)


	#############################################################
	#请求参数字典
	def httpClient(self, method="GET", domain="", path="", data=None, headers={}):

	    conn = HTTPConnection(domain)
	    # conn.set_debuglevel(1)
	    conn.request(method, path, body=data, headers=headers)
	    return conn.getresponse().read().decode('utf-8')
	
	def uploadToPgyer(self):
		params = {
			'uKey': self.uKey,
			'_api_key': self.api_key,
			'file': self.ipaFile,
			'publishRange': '2',
			'password': self.installPassword
		}

		coded_params, boundary = self._encode_multipart(params)
		headers = {'Content-Type': 'multipart/form-data; boundary={boundary}'.format(boundary=boundary)}
		try:
			responseObject = self.httpClient("POST",self.domain, self.urlPath, coded_params.encode('ISO-8859-1'), headers)
			return self.handle_resule(responseObject, self.mail_receiver)
		except:
			return G7ReqHandler.responseDataText(10003)

class G7ApplicationReqHandler(G7APIReqHandler):

	def infoPlistFrom(self, buffer):
		info = {}

		try:
			info = plistlib.readPlistFromBytes(buffer)
		except:
			pass

		return info

	def g7CommonPlistFrom(self, buffer):
		info = {}

		try:
			info = plistlib.readPlistFromBytes(buffer)
		except:
			pass

		return info

	def dataFromFile(self, fileBytes):

		data = {
			"InfoPlist":{},
			"G7CommonSettingPlist":{},
			"Icon":None,
		}

		# 获取info.plist
		info = {}

		# 获取G7CommonSetting.plist
		g7CommonSetting = {}

		# 获取图标
		icon = None

		zipBuffer = io.BytesIO()
		zipBuffer.write(fileBytes)
		
		zipBuffer.seek(0)
		zf = zipfile.ZipFile(zipBuffer, "r")
		for zipInfo in zf.infolist():
			
			# 获取名字和bundleid
			if ".app/Info.plist" in zipInfo.filename:
				info = self.infoPlistFrom(zf.read(zipInfo.filename))
			
			# 获取G7CommonSetting.plist
			if ".app/G7CommonSetting.plist" in zipInfo.filename:
				g7CommonSetting = self.g7CommonPlistFrom(zf.read(zipInfo.filename))

			# 获取图标
			if ".app/AppIcon" in zipInfo.filename:
				icon = ContentFile(zf.read(zipInfo.filename))
			# else:
			# 	if ".app/AppIcon60x60@2x.png" in zipInfo.filename:
			# 		icon = ContentFile(zf.read(zipInfo.filename))
			# 	else:
			# 		if ".app/AppIcon60x60.png" in zipInfo.filename:
			# 			icon = ContentFile(zf.read(zipInfo.filename))
		zipBuffer.close()
		zf.close()

		if info and len(info) > 0:
			data["InfoPlist"] = info

		if g7CommonSetting and len(g7CommonSetting) > 0:
			data["G7CommonSettingPlist"] = g7CommonSetting

		if icon:
			data["Icon"] = icon

		return data

	def intFilter(self, integerValue):

		returnedInteger = integerValue
		if type(integerValue) != type(0):
			try:
				returnedInteger = int(integerValue)
			except:
				returnedInteger = 0

		return integerValue

	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def post(self):
		
		product_name = self.get_argument('product_name')
		uid = self.get_argument("uid")
		installPassword = self.get_argument("installPassword")
		product_group_id = int(self.get_argument("product_group_id"))
		pgyer_uKey = ""
		pgyer_apiKey = ""
		currentG7User = None

		if uid == None or uid == "":
			# 请提交搞趣开发平台的用户ID
			return self.responseWrite(10006)
		else:
			uidUsers = G7User.objects.filter(userid=uid)
			if len(uidUsers) == 0:
				# 提交的用户ID对应的用户不存在
				return self.responseWrite(10007)
			else:
				currentG7User = uidUsers[0]
				pgyer_uKey = currentG7User.pgyer_ukey
				pgyer_apiKey = currentG7User.pgyer_apiKey

				if pgyer_uKey == None or pgyer_uKey == "" or pgyer_apiKey == None or pgyer_apiKey == "":
					# 请填写该用户所拥有的蒲公英uKey和apiKey
					return self.responseWrite(10008)

		data = self.dataFromFile(self.request.files["file"][0]["body"])

		# Info.plist
		info = data["InfoPlist"]

		# G7CommonSetting.plist
		g7CommonSetting = data["G7CommonSettingPlist"]

		# 获取BundleID 必须
		bundleID = ""
		if "CFBundleIdentifier" in list(info.keys()):
			bundleID = info["CFBundleIdentifier"]

		if bundleID == None or len(bundleID) == 0 or type(bundleID) != type(""):
			# 返回失败
			# ipa包备份失败, BundleID不合法!!!
			return self.responseWrite(10001)


		######### 进入备份操作 ########

		# 获取G7CH G7PID G7VER G7PT, 若无，取默认值

		# 渠道
		g7CH = 0
		if "G7CH" in list(g7CommonSetting.keys()):
			g7CH = self.intFilter(g7CommonSetting["G7CH"])

		# 产品标识
		g7PID = 0
		if "G7PID" in list(g7CommonSetting.keys()):
			g7PID = self.intFilter(g7CommonSetting["G7PID"])

		# 内部版本
		g7VER = 0
		if "G7PID" in list(g7CommonSetting.keys()):
			g7VER = self.intFilter(g7CommonSetting["G7VER"])

		# 产品类型
		g7PT = 0
		if "G7PT" in list(g7CommonSetting.keys()):
			g7PT = self.intFilter(g7CommonSetting["G7PT"])

		if "G7PT@iPad" in list(g7CommonSetting.keys()) and "G7PT@iPhone" in list(g7CommonSetting.keys()):
			g7PT = 3

		else:
			if "G7PT@iPad" in list(g7CommonSetting.keys()):
				g7PT = 2

			else:
				if "G7PT@iPhone" in list(g7CommonSetting.keys()):
					g7PT = 1
		
		# 获取应用名 
		appName = product_name
		if "CFBundleDisplayName" in list(info.keys()) and (appName == None or appName == ""):
			appName = info["CFBundleDisplayName"]

		# 应用版本
		appVersion = "1.0"
		if "CFBundleShortVersionString" in list(info.keys()):
			appVersion = info["CFBundleShortVersionString"]

		localTime = time.localtime()
		timeNow = time.strftime("%Y%m%d%H%M%S", localTime)
		# g7log("timeNow:"+timeNow)
		# 编译版本
		buildVersion = "{timeNow}".format(timeNow=timeNow)  # 默认获取当前时间
		if "CFBundleVersion" in list(info.keys()):
			buildVersion = info["CFBundleVersion"]

		# 获取图标 若无, 取默认值
		icon = data["Icon"]

		# 判断当前产品中是否使用了接收到的Project_id
		projects = G7Project.objects.filter(project_id = g7PID)
		if len(projects) > 0:
			project = projects[0]
		else:
			project = G7Project(bundleID=bundleID, project_id=g7PID, project_type=0, icon=icon, name=appName, identifier=uuid.uuid4().hex)
			if icon:
				project.icon.save("application/icon/"+timeNow+".png", icon)
			else:
				project.icon = "application/icon/default_icon.png"
			project.save()

		try:
			# 创建新的包
			ipaFile = ContentFile(self.request.files["file"][0]["body"])
			ipaFileDir = time.strftime("%Y%m%d",localTime)
			ipaFileName = "{appName}_V{appVersion}_Build{build_version}_{timeNow}.ipa".format(appName=appName,
				appVersion=appVersion, build_version=buildVersion, timeNow=timeNow)
			# g7log(ipaFileName)
			application = G7Application(bundleID=bundleID, 
			product_id=g7PID, 
			product_type=g7PT,
			name=appName, 
			channel=g7CH, 
			version=appVersion, 
			build_version=buildVersion,
			inner_version=g7VER,
			appid=uuid.uuid4().hex)
			if icon:
				application.icon.save("application/icon/"+timeNow+".png", icon)
			else:
				application.icon = "application/icon/default_icon.png"

			application.save()
			application.file.save(ipaFileName, ipaFile)

			project.applications.add(application)
			project.latest_build_version=application.build_version
			project.latest_version = application.version
			project.latest_inner_version = application.inner_version
			project.save()

			# buff = io.BufferedReader(ipaFile.file)
			# # 上传到蒲公英
			uploader = G7ApplicationPgyerUploader()
		 #    #蒲公英应用上传地址

			uploader.domain = 'www.pgyer.com'
			uploader.urlPath = "/apiv1/app/upload"
			uploader.uKey = pgyer_uKey 
			uploader.api_key = pgyer_apiKey 
			uploader.ipaFile = open(application.file.path, "rb")
			uploader.installPassword = installPassword
			uploader.product_name = appName
			uploader.currentG7User = currentG7User

			users = list(G7User.objects.filter(email_vip=True))+list(project.members.all())
			
			try:
				if type(int(product_group_id)) == type(0) and int(product_group_id) > 0:
					users = list(G7User.objects.filter(email_vip=True))+list(project.members.all())+[user for user in G7User.objects.all() if len([group for group in list(user.groups.all()) if group.id == int(product_group_id)])>0]
			except:
				pass
				
			emails = [user.email for user in users]
			uploader.mail_receiver = list({}.fromkeys(emails).keys())
			uploader.build_version = buildVersion
			uploader.project_version = appVersion

			return self.write(uploader.uploadToPgyer())
		except:
			# ipa包备份失败, 储存资料失败!!!
			return self.responseWrite(10002)

		

