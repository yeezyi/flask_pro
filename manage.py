from flask_script import Manager
from flask_pro import app
from manage_db import db_manage

manager = Manager(app)
manager.add_command('db', db_manage)


# 将great变成一个命令(无法带参数)  --> python manage.py great 会输出"你好"
@manager.command
def great():
    print('你好')


# 使用带参数的命令  --> python manage.py add_user -u abc --age 15
@manager.option('-u', '--username', dest='username')
@manager.option('-a', '--age', dest='age')
def add_user(username, age):
    print('输入的用户为 %s, %s岁' % (username, age))



if __name__ == '__main__':
    manager.run()
