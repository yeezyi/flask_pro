from flask import Flask, render_template
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return "<User(username : %s )>" % self.username

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.INTEGER, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('articles'))

    def __repr__(self):
        return "<Article(title : %s )>" % self.title

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
    # users = User.query.all()
    # users = User.query.order_by(User.id.desc()).all()
    # print(users)
    # 上面是单表查询的简便写法,多表查询还是要db.session.query

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8000)
