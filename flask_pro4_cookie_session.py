from flask import Flask, render_template, request, Response
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    resp = Response('aa')
    resp.set_cookie('cookie_key', 'cookie_value')
    return resp


if __name__ == '__main__':
    app.run(port=8004)
