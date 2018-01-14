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

import enum


class TagEnum(enum.Enum):
    tag1 = "tag1"
    tag2 = "tag2"
    tag3 = "tag3"


class Article(Base):
    __tablename__ = "article"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # price = Column(Float)
    # prices = Column(DECIMAL(10, 4))  # 10表示一共有10位,小数占4位,存储位数超过时会报错
    # is_delete = Column(Boolean)
    # tag = Column(Enum("tag1", "tag2", "tag3"))  # 只能存储以上3种值
    # tag = Column(Enum(TagEnum))  # 也可以传enum的子类
    # create_time = Column(DATE)
    # create_time = Column(DATETIME)
    # create_time = Column(TIME)
    # title = Column(String(50))
    # content = Column(Text)
    # content = Column(LONGTEXT)

# 删除绑定在Base下的所有表
Base.metadata.drop_all()
Base.metadata.create_all()

from datetime import datetime

article = Article(create_time=datetime(2018, 1, 1, 15, 32, 59))
session.add(article)
session.commit()
