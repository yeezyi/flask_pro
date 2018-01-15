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

from datetime import datetime


class Article(Base):
    __tablename__ = "article"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

    def __str__(self):
        return '%s : %s :%s' % (self.id, self.title, self.price)

    # print结果集的时候会执行这个方法
    def __repr__(self):
        return '%s : %s' % (self.title, self.price)

# 删除绑定在Base下的所有表
# Base.metadata.drop_all()
# Base.metadata.create_all()

# from random import randint
#
# for x in range(6):
#     article = Article(title='title%s' % x, price=randint(1, 30))
#     session.add(article)
# session.commit()

# 模型对象
# result = session.query(Article).all()

# 模型属性
# result = session.query(Article.id, Article.title).all()

# 聚合函数
from sqlalchemy import func
result = session.query(func.count(Article.id)).first()

# for i in result:
#     print(i)
print(result)