from flask import Blueprint

bp_3 = Blueprint('xxxxx', __name__)


@bp_3.route('/bp3/')
def bp1():
    return 'bp3'
