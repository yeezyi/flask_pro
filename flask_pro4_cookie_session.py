from flask import Flask, render_template, request, Response, session
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    resp = Response('aa')
    resp.set_cookie('cookie_key', 'cookie_value')
    return resp


@app.route('/session/')
def set_session():
    session['session_id'] = 'session_value'
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
