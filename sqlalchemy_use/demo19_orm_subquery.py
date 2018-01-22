# demo与flask无任何关联
# sqlalchemy 连接数据库
from sqlalchemy import create_engine, Column, INTEGER, String, Float, Boolean, DECIMAL, Enum
from sqlalchemy import DATE, DATETIME, TIME, Text, func
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
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    age = Column(INTEGER, default=0)

    def __repr__(self):
        return '<user(username : %s)>' % self.username


def my_init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    user1 = User(username='1111', city='aaaa', age=18)
    user2 = User(username='2222', city='aaaa', age=18)
    user3 = User(username='3333', city='bbbb', age=18)
    user4 = User(username='4444', city='aaaa', age=20)
    session.add_all([user1, user2, user3, user4])
    session.commit()


def operation():
    # 与1111同城市和年龄的人
    # 传统方式:
    # user = session.query(User).filter(User.username == '1111').first()
    # result = session.query(User).filter(User.city == user.city, User.age == user.age).all()
    # print(result)
    # 子查询方式:
    sub = session.query(User.city.label("city1"), User.age.label("age1")).filter(User.username == '1111').subquery()
    result = session.query(User).filter(User.city == sub.c.city1, User.age == sub.c.age1).all()
    print(result)

if __name__ == '__main__':
    # my_init_db()
    operation()
