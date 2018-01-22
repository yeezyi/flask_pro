from flask import Flask, url_for, redirect, render_template, request, views
import config
import datetime
from blueprints.bp1 import bp_1
from blueprints.bp2 import bp_2
from blueprints.bp3 import bp_3

# from flask_sqlalchemy import SQLAlchemy

# 初始化Flask对象
# 需要传递一个参数__name__
# 1.方便flask框架去寻找资源
# 2.方便flask插件比如Flask-Sqlalchemy出现错误的时候，好去寻找问题所在的位置
app = Flask(__name__)

# 使用配置文件
app.config.from_object(config)

# 使用蓝图模块化
app.register_blueprint(bp_1)
app.register_blueprint(bp_2)
app.register_blueprint(bp_3)


# 初始化SQLAlchemy
# db = SQLAlchemy(app)

# @app.route
# 这个装饰器的作用是作一个url与视图函数的映射
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return '第一个flask程序!'


# 传参到路由,用于加载不同的数据，参数放在<>中，函数的传参需要与<>内的变量名相同
@app.route('/article/<id>/')
def article(id):
    return 'get_id : ' + id


@app.route('/list/')
def my_list(id):
    return 'get_id : ' + id


@app.route('/reverse/')
def reverse():
    # url 反转  （需要导入url_for模块,通过视图函数的名字得到url）
    # 用处：1.页面重定向的时候  2.在模板中，也会使用url反转
    print(url_for('my_list'))
    print(url_for('article', id='xcv123'))  # 有参数的必须传参数
    return 'reverse'


@app.route('/redirect/')
def redirect1():
    # 重定向
    login_url = url_for('login')
    return redirect(login_url)
    # return redirect('/login/')


@app.route('/login/')
def login():
    return '登录页面'


@app.route('/index/')
def index():
    class Person(object):
        name = 'lmc'
        age = '12'

    p = Person()
    # 传字典，对象，字符串
    result_content = {
        'username': '用户名',
        'gender': '男',
        'age': 18,
        'person': p,
        # 'c_time': datetime.datetime(2017, 6, 6, 20, 11, 30),
        'c_time': '',
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('index.html', **result_content)
    # return render_template('index.html', result=result_content)


@app.template_filter('my_filter')
def xxx(value):
    value = value.center(20, '-')
    return value


@app.template_filter('handle_time')
def xxxx(value):
    if isinstance(value, datetime.datetime):
        now = datetime.datetime.now()
        now_value = (now - value).total_seconds()
        if now_value < 60:
            return '刚刚'
        elif now_value < 3600:
            return '%s分钟前' % (now_value // 60)
        elif now_value < 86400:
            return '%s小时前' % (now_value // 3600)
        elif now_value < 60 * 60 * 24 * 365:
            return '%s天前' % int(now_value / (3600 * 24))
        else:
            return value.strftime('%Y-%m-%d')
    else:
        return ''


def my_list1():
    print(url_for('login'))
    return 'my_list1'


from functools import wraps


def login_require(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        if username and username == 'xxx':
            return func(*args, **kwargs)
        else:
            return '请先登录'

    return wrapper


@app.route('/settings/', endpoint='settings')
@login_require
def settings():
    return '这是设置页面'


class SettingsView(views.View):
    decorators = [login_require]

    def dispatch_request(self):
        return '这是设置界面'


app.add_url_rule('/setting/', view_func=SettingsView.as_view('setting'))

app.add_url_rule('/list1/', endpoint='list111', view_func=my_list1)

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
