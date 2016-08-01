# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'

from dal.domain.do.PayOrderDO import PayOrderDO

"""
PayOrderMapper数据库操作接口类
"""

class PayOrderMapper(object):


	"""
	查询（根据主键ID查询）
	"""
	def selectByPrimaryKey(self,id):
		return self.session.query(PayOrderDO).filter(PayOrderDO.id==id).one()

	def selectBatch(self,start,number):
		return self.session.query(PayOrderDO).order_by(PayOrderDO.id)[start:number]

	def selectByOutOrderSnList(self, outOrderSnList):
		return self.session.query(PayOrderDO).filter(PayOrderDO.isDeleted=='N') \
			.filter(PayOrderDO.outOrderSn.in_(outOrderSnList)).filter(PayOrderDO.orderType.in_([1,3])).all()

	def selectPayOrderInfo(self, outOrderSnList):
		return self.session.query(PayOrderDO).filter(PayOrderDO.isDeleted=='N')\
			.filter(PayOrderDO.outOrderSn.in_(outOrderSnList)).filter(PayOrderDO.orderType.in_([1])).all()

	def updatePayOrderAmount(self, updatePayOrderAmountInfo, session):
		if session is None:
			session = self.session

		for key,value in updatePayOrderAmountInfo:
			session.query(PayOrderDO).filter(PayOrderDO.id == key).update({
				PayOrderDO.payOrderAmount : value
			})


