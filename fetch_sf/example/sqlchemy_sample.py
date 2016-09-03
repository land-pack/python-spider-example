from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
	__tablename__ = 't_sf_user'
	id = Column(String(32), primary_key = True)
	name = Column(String(32))

engine = create_engine('mysql://crazy_bet:crazy_bet@192.168.50.203:3306/crazy_bet')
DBSession = sessionmaker(bind=engine)
User.metadata.create_all(engine)

if __name__ == '__main__':
	session = DBSession()
	new_user = User(id='5',name='Bob')
	session.add(new_user)
	session.commit()
	session.close()
