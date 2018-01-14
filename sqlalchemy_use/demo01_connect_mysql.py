# demo与flask无任何关联
# sqlalchemy 连接数据库
from sqlalchemy import create_engine

HOST = '127.0.0.1'
PORT = 3306
DATABASE = 't3'
USERNAME = 'root'
PASSWORD = '124578'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}" \
         "?charset=utf8".format(username=USERNAME,
                                password=PASSWORD, host=HOST,
                                port=PORT, db=DATABASE)

engine = create_engine(DB_URI)
conn = engine.connect()
with conn:
    result = conn.execute('select count(1) from four_imagesurl')
    print(result.fetchone())