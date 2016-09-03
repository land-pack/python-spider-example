from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class SFOrder(Base):
	__tablename__ = 't_sf_order'
	id = Column(Integer,primary_key=True)
	sfid = Column(String(32))
	origin = Column(String(32))
	originOld = Column(String(32))
	originCode = Column(String(32))
	destination = Column(String(32))
	destinationOld = Column(String(32))
	receiveBillFlg =  Column(String(32),default='')
	delivered = Column(Boolean)
	expectedDeliveryTime = Column(String(64),default='')
	expectedDeliveryTimeEnd=Column(String(64),default='')
	recipientTime=Column(String(64))
	refundable=Column(Boolean)
	limitTypeCode=Column(String(32))
	limitTypeName=Column(String(32))
	mainlandToMainland=Column(Boolean)
#routes=Column()	# TODO
	prioritized=Column(Boolean)
	warehouse=Column(Boolean)
	signed=Column(Boolean)
	expressState=Column(String(32))
	lstElementHtml=Column(String(32),default='')
	childSet=Column(String(128),default='[]')
	showThermometer=Column(Boolean)
	productCode=Column(String(32))
	productName=Column(String(32))
	billFlag=Column(String(4))
	weight=Column(String(32))

class SFRoutes(Base):
	__tablename__ = 't_sf_routes'
	id = Column(Integer,primary_key=True)
	scanDateTime=Column(String(64))
	remark=Column(String(1024))
	stayWhyCode=Column(String(128))

engine = create_engine('mysql://crazy_bet:crazy_bet@192.168.50.203:3306/crazy_bet')
DBSession = sessionmaker(bind=engine)
SFOrder.metadata.create_all(engine)

if __name__ == '__main__':



	session = DBSession()
	new_user = SFOrder(sfid='606721866344',origin='sz')
	session.add(new_user)
	session.commit()
	session.close()
