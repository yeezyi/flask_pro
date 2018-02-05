# 以配置文件形式配置项目
# 以debug模式运行，出错时页面会显示错误信息，且在此模式下，python文件被修改时会自动重新run
DEBUG = True

import os
SECRET_KEY = os.urandom(24)  # 产生一个24位随机的key

# SQLALCHEMY_DB

# SERVER_NAME = 'lmc.com:8004'

HOST = '127.0.0.1'
PORT = 3306
DATABASE = 't4'
USERNAME = 'root'
PASSWORD = '124578'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}" \
         "?charset=utf8".format(username=USERNAME,
                                password=PASSWORD, host=HOST,
                                port=PORT, db=DATABASE)

# SQLALCHEMY_DATABASE_URI是固定变量名,名字不可变
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False