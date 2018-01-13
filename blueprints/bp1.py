from flask import Blueprint

bp_1 = Blueprint('xxx', __name__,url_prefix='/bp1')


@bp_1.route('/bp11/')
def bp1():
    return 'bp1'
