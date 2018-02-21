from flask import Flask, request, current_app, url_for, g
from werkzeug.local import Local
app = Flask(__name__)

@app.route('/')
def index():
    print(current_app.name)
    return 'index'
@app.route('/index/')
def abc():
    return 'index'
# with app.app_context():
#     print(current_app.name)
with app.test_request_context():
    # print(current_app.name)
    print(url_for('abc'))


if __name__ == '__main__':
    app.run(port=5005, debug=True)