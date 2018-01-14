# demo与flask无任何关联
# sqlalchemy 连接数据库
from sqlalchemy import create_engine, Column, INTEGER, String
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


class Person(Base):
    __tablename__ = 'person'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(INTEGER)

    def __str__(self):
        return "id: {id}, name: {name}, age: {age}".format(id=self.id, name=self.name, age=self.age)


# 增
def create_data():
    # 单条数据
    # p = Person(name='aabbcc', age=10)
    # session.add(p)  # 此时还没提交到数据库
    # session.commit()
    # 多条数据
    p1 = Person(name='aabbccdd', age=11)
    p2 = Person(name='aabbccddee', age=12)
    session.add_all([p1, p2])  # 此时还没提交到数据库
    session.commit()


# 删
def delete_data():
    # 删除前需要获得这个对象
    person = session.query(Person).first()
    session.delete(person)
    session.commit()


# 改
def update_data():
    # 修改前需要获得这个对象
    person = session.query(Person).first()
    # 直接修改属性即可
    person.name = 'aa'
    # 修改之后提交
    session.commit()


# 查
def select_data():
    # 查找某个模型的所有数据
    # select_person = session.query(Person).all()
    # 根据条件查找
    # select_person = session.query(Person).filter_by(age=11).all()
    # 或 使用filter(条件查询)  如>=, <=
    # select_person = session.query(Person).filter(Person.age>=11).all()
    # for p in select_person:
    #     print(p)
    # 根据主键ID获取
    # person = session.query(Person).get(1)
    # print(person)
    # 使用first方法获取结果集中的第一条数据
    person = session.query(Person).first()
    print(person)

if __name__ == '__main__':
    # create_data()
    # select_data()
    # update_data()
    delete_data()