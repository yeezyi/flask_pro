from flask import Blueprint, request

bp_cookie = Blueprint('xxxxx', __name__, subdomain='abc')


@bp_cookie.route('/sub/')
def bp1():
    val = request.cookies.get('cookie_key')
    return val or '得不到cookie'
