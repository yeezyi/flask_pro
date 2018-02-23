from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with
from models import Article

bp_rest = Blueprint("rest", __name__, url_prefix='/api')
api = Api(bp_rest)


class ArticleView(Resource):
    resource_fields = {
        'article_title': fields.String(attribute='title'),
        'author': fields.Nested({
            'author_name': fields.String(attribute='username'),
            'author_email': fields.String(attribute='email')
        }),
        'article_tag': fields.List(fields.String(attribute='name'), attribute='tags')
    }

    @marshal_with(resource_fields)
    def get(self, article_id):
        article = Article.query.get(article_id)
        return article


api.add_resource(ArticleView, '/article/<article_id>/', endpoint='article')
