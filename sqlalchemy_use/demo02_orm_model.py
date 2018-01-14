# demo与flask无任何关联
# sqlalchemy 连接数据库
from sqlalchemy import create_engine, Column, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

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

# create table person(id int primary_key autoincrement,name varcher(50), age int)
# 1.创建一个ORM模型,模型必须继承自sqlalchemy为我们提供好的基类
class Person(Base):
    __tablename__ = 'person'
    # 2.在这个ORM模型中创建一些属性，来跟表中的字段进行一一映射，属性必须是sqlalchemy为我们提供好的数据类型
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(INTEGER)
# 3.将创建好的ORM模型，映射到数据库中
Base.metadata.create_all()