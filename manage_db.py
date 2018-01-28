from flask_script import Manager

db_manage = Manager()


# 添加到主manager后,使用python manage.py db init命令即可运行该方法
@db_manage.command
def init():
    print('初始化成功')