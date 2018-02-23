from flask import Flask
from flask_restful import Api, Resource, reqparse, marshal_with, fields
import config
from models import User, Article, Tag
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
api = Api(app)


class LoginView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="用户名验证错误")
        parser.add_argument('password', type=str, help="密码验证错误")
        args = parser.parse_args()
        print(args)  # {"username":"xx", "password":"xxx"}
        return {"username": "zhiliao"}


api.add_resource(LoginView, '/login/', endpoint='login')


class ArticleView(Resource):
    resource_fields = {
        'title': fields.String,
        'user': fields.Nested({
            'username': fields.String,
            'user_email': fields.String(attribute='email')
        }, attribute='author'),
        # 'authorname': fields.String(attribute='author.username'),  # author指User模型
        'tag': fields.List(fields.String(attribute='name'), attribute='tags')
    }

    @marshal_with(resource_fields)
    def get(self, a_id):
        article = Article.query.get(a_id)
        return article


api.add_resource(ArticleView, '/articles/<a_id>', endpoint='article')


@app.route('/create/')
def create():
    # user = User(username="user1111", email="qweqwe@qwe.com")
    # article = Article(title="title1111")
    # article.author = user
    # tag1 = Tag(name="tag111")
    # tag2 = Tag(name="tag222")
    # article.tags.extend([tag1, tag2])
    # db.session.add(article)
    # db.session.commit()
    # tag3 = Tag(name="我是标签")
    # article = Article.query.get(3)
    # article.tags.append(tag3)
    # db.session.commit()
    return 'create success !'


if __name__ == '__main__':
    app.run(debug=True, port=5007)
