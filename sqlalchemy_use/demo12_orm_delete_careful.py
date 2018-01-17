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
    username = Column(String(50))


class Article(Base):
    __tablename__ = "article"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    # 添加外键约束RESTRICT后在SQL层面是无法删除父表外键的,但是在ORM代码中是可以删除的
    # 删除后字表的外键值会设为NULL
    # 想避免这种情况,需要在字表的外键处添加nullable=False
    uid = Column(INTEGER, ForeignKey('user.id'), nullable=False)
    author = relationship('User', backref='articles')

    def __str__(self):
        return '%s' % self.title

    # print结果集的时候会执行这个方法
    def __repr__(self):
        return '%s : %s' % (self.title, self.id)

#
# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='lmc')
# article = Article(title='lllllllll')
# article.author = user
# session.add(article)
# session.commit()

user = session.query(User).first()
session.delete(user)
session.commit()

