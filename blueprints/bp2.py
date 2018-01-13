from flask import Blueprint

# bp_2 = Blueprint('xxxx', __name__)
bp_2 = Blueprint('xxxx', __name__, subdomain='abc')

@bp_2.route('/bp2/')
def bp1():
    return 'bp2'
