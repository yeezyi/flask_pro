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


class Article(Base):
    __tablename__ = "article"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DATETIME, nullable=False, default=datetime.now)
    uid = Column(INTEGER, ForeignKey('user.id'))
    author = relationship('User', backref=backref("articles"))

    def __str__(self):
        return '%s' % self.title

    # print结果集的时候会执行这个方法
    def __repr__(self):
        return '%s : %s' % (self.title, self.create_time)


def my_init_db():
    # Base.metadata.drop_all()
    # Base.metadata.create_all()
    # user = User(username="1111")
    # user1 = User(username="2222")
    # # user = session.query(User).first()
    # article1 = Article(title='aaaa')
    # article1.author = user
    # article2 = Article(title='bbbb')
    # article3 = Article(title='cccc')
    # article4 = Article(title='dddd')
    # user1.articles.extend([article2, article3, article4])
    # user2 = User(username='3333')
    # session.add(user)
    # session.add(user1)
    # session.add(user2)
    session.commit()


def operation():
    result = session.query(User.username, func.count(Article.id)).join(Article, User.id == Article.uid, isouter=True).group_by(
        User.id).order_by(func.count(Article.id).desc()).all()
    print(result)

    "select user.username,count(article.id) from user left JOIN article on article.uid=user.id GROUP BY user.id order by (count(article.id)) "


if __name__ == '__main__':
    # my_init_db()
    operation()
