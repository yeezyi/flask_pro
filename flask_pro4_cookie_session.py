from flask import Flask, render_template, request, Response
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

@app.route('/del')
def del_cookie():
    resp = Response('aaa')
    resp.delete_cookie('cookie_key')
    return resp


if __name__ == '__main__':
    app.run(port=8004)
