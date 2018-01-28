from flask import Flask, render_template
import config
from exts import db
from models import User, Article
app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)


# db.drop_all()
# db.create_all()


@app.route('/')
def index():
    # 增
    # user = User(username='2aa222')
    # article = Article(title='bbqqssqq')
    # article.author = user
    # db.session.add(user)
    # db.session.commit()
    # 查 order_by,filter,filter_by,group_by,having,join
    users = User.query.all()
    # users = User.query.order_by(User.id.desc()).all()
    print(users)
    # 上面是单表查询的简便写法,多表查询还是要db.session.query

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8000)
