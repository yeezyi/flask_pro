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
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)




class Article(Base):
    __tablename__ = "article"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DATETIME, nullable=False, default=datetime.now)
    uid = Column(INTEGER, ForeignKey('user.id'))
    author = relationship('User', backref=backref("articles", lazy='dynamic'))

    def __str__(self):
        return '%s' % self.title

    # print结果集的时候会执行这个方法
    def __repr__(self):
        return '%s : %s' % (self.title, self.create_time)

        # __mapper_args__ = {
        #     'order_by': -create_time
        # }


def my_init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    user = User(username="1111")
    for i in range(100):
        article = Article(title='title %s' % i)
        article.author = user
        session.add(article)
    session.commit()


def operation():
    user = session.query(User).first()
    # print(user.articles)
    # print(user.articles.limit(10).all())
    article = Article(title='title 100')
    user.articles.append(article)
    session.commit()

if __name__ == '__main__':
    # my_init_db()
    operation()
