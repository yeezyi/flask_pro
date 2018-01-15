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

# equals
# result = session.query(Article).filter_by(id=1).all()
# result = session.query(Article).filter(Article.id == 1).all()

# not equals
# result = session.query(Article).filter(Article.id != 1).all()

# like
# result = session.query(Article).filter(Article.title.like('title%')).all()
# result = session.query(Article).filter(Article.title.ilike('title%')).all()

# in
# result = session.query(Article).filter(~Article.title.in_(['title1', 'title2'])).all()
# result = session.query(Article).filter(Article.title.in_(session.query(Article.title).filter(Article.title.like('title%')))).all()

# not in
# result = session.query(Article).filter(Article.title.notin_(['title1', 'title2'])).all()

# is null
# result = session.query(Article).filter(Article.title == None).all()

# is not null
# result = session.query(Article).filter(Article.title != None).all()

# and
# result = session.query(Article).filter(Article.title == 'title0', Article.id == 1).all()
# from sqlalchemy import and_
# result = session.query(Article).filter(and_(Article.title == 'title0', Article.id == 1)).all()

# or
from sqlalchemy import or_
result = session.query(Article).filter(or_(Article.title == 'title0', Article.id == 2)).all()


print(result)
