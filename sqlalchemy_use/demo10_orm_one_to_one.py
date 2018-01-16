# demo与flask无任何关联
# sqlalchemy 连接数据库
from sqlalchemy import create_engine, Column, INTEGER, String, Float, Boolean, DECIMAL, Enum
from sqlalchemy import DATE, DATETIME, TIME, Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = '127.0.0.1'
PORT = 3306
DATABASE = 't4'
USERNAME = 'root'
PASSWORD = '124578'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}" \
         "?charset=utf8".format(username=USERNAME,
                                password=PASSWORD, host=HOST,
                                port=PORT, db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

# 对数据的增删改查都需要这个对象
session = sessionmaker(engine)()

from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    # extend = relationship('UserExtend', uselist=False)

    def __repr__(self):
        return "%s, %s" % (self.id, self.username)
class Article(Base):
    __tablename__ = "article"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    uid = Column(INTEGER, ForeignKey("user.id", ondelete="RESTRICT"))
    user = relationship('User', backref="xxarticlesxx")

    def __str__(self):
        return '%s : %s :%s' % (self.id, self.title, self.price)

    # print结果集的时候会执行这个方法
    def __repr__(self):
        return '%s : %s' % (self.title, self.price)

from sqlalchemy.orm import backref
class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(INTEGER, ForeignKey('user.id'))
    # user = relationship("User")
    user = relationship("User", backref=backref("extend", uselist=False))

# Base.metadata.drop_all()
# Base.metadata.create_all()

user = User(username='zxczxc123aaa')
# user = session.query(User).first()
# extend1 = UserExtend(school='1ss21asdasd1111')
extend1 = session.query(UserExtend).first()
user.extend = extend1
session.add(user)
session.commit()