from flask_script import Manager
from flask_pro2 import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models import User,Article

manager = Manager(app)
# 绑定app和SQLAlchemy
Migrate(app, db)
# 将Migrate命令添加到Flask-Script中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()