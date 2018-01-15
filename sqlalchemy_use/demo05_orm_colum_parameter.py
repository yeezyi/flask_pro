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
    read_count = Column(INTEGER, default=0)
    title = Column('my_title',String(50))
    create_time = Column(DATETIME, default=datetime.now)
    update_time = Column(DATETIME, onupdate=datetime.now)


# 删除绑定在Base下的所有表
Base.metadata.drop_all()
Base.metadata.create_all()

article = Article(create_time=datetime(2018, 1, 1, 15, 32, 59))
session.add(article)
session.commit()
