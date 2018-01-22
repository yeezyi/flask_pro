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
    age = Column(INTEGER, default=0)
    gender = Column(Enum('male', 'female', 'secret'), default='male')


def my_init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    user1 = User(username="1111", age=17, gender='male')
    user2 = User(username="2222", age=17, gender='male')
    user3 = User(username="3333", age=18, gender='female')
    user4 = User(username="4444", age=19, gender='female')
    user5 = User(username="5555", age=20, gender='female')
    session.add_all([user1, user2, user3, user4, user5])
    session.commit()


def operation():
    # result = session.query(User.gender, func.count(User.id)).group_by(User.gender).all()
    result = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age >=18).all()
    print(result)
    # session.commit()


if __name__ == '__main__':
    # my_init_db()
    operation()
