#-*- coding: utf-8 -*-

from G7Platform.main.site.Common.G7APIReqHandlers import G7APIReqHandler

class G7ApplicationReqHandler(G7APIReqHandler):

	def post(self):

		self.responseWrite(0,"请求成功",{"success":"yes"})