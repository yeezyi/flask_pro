from flask import Flask, render_template, request, Response, session
import config
from blueprints.bp_cookie import bp_cookie

app = Flask(__name__)
app.config.from_object(config)


# app.register_blueprint(bp_cookie)

@app.route('/')
def index():
    resp = Response('aa')
    resp.set_cookie('cookie_key', 'cookie_value')
    # 子域名拿到cookie
    # resp.set_cookie('cookie_key', 'cookie_value', domain=".lmc.com")
    return resp


@app.route('/del/')
def del_cookie():
    resp = Response('aaa')
    resp.delete_cookie('cookie_key')
    return resp


@app.route('/session/')
def set_session():
    session['session_id'] = 'session_value'
    # permanent: 持久化, 为True且config没有设置PERMANENT_SESSION_LIFETIME时session会保持31天
    session.permanent = True
    return 'session success'


@app.route('/get_session/')
def get_session():
    val = session.get('session_id')
    return val or 'session is None'


@app.route('/del_session/')
def del_session():
    session.pop('session_id')
    # session.clear()  # 清空session内的所有键值
    return 'session is del'


if __name__ == '__main__':
    app.run(port=8004)
