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

from sqlalchemy import ForeignKey, Table

from sqlalchemy.orm import relationship

# 第一个参数:表的名字
# 第三个参数:有哪些列
# article_id 和 tag_id 组成主键联合唯一
article_tag = Table("article_tag", Base.metadata,
                    Column("article_id", INTEGER, ForeignKey('article.id'), primary_key=True),
                    Column("tag_id", INTEGER, ForeignKey('tag.id'), primary_key=True)
                    )


class Article(Base):
    __tablename__ = "article"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    tags = relationship("Tag", backref='articles', secondary=article_tag)

    def __str__(self):
        return '%s' % self.title

    # print结果集的时候会执行这个方法
    def __repr__(self):
        return '%s : %s' % (self.title, self.id)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return self.name


#
# Base.metadata.drop_all()
# Base.metadata.create_all()

# article1 = Article(title="111111")
# article2 = Article(title="222222")
# tag1 = Tag(name='aaaaaa')
# tag2 = Tag(name='bbbbbb')
#
# article1.tags.append(tag1)
# article1.tags.append(tag2)
# article2.tags.append(tag1)
# article2.tags.append(tag2)
#
#
# session.add_all([article1, article2])
# session.commit()

article = session.query(Article).first()
print(article.tags)

tag = session.query(Tag).first()
print(tag.articles)
