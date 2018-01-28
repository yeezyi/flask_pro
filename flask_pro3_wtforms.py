from flask import Flask, render_template,request
import config
from form import RegistForm, LoginForm, SettingsForm
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        # username = request.form.get('username')
        # password = request.form.get('password')
        # password_repeat = request.form.get('password_repeat')
        # if len(username) < 3 or len(username) > 10:
        #     return '用户名长度不正确'
        # if len(password) < 6 or len(password) > 10:
        #     return '密码长度不正确'
        # if password != password_repeat:
        #     return '两次输入的密码不一致'
        form = RegistForm(request.form)
        if form.validate():
            # 通过验证
            return "success"
        else:
            print(form.errors)
            return "fail"


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            for k, v in request.form.items():
                print('%s:%s' % (k, v))
            return 'success'
        else:
            print(form.errors)
            return 'fail'

@app.route('/settings/', methods=['GET', 'POST'])
def setting():
    if request.method == 'GET':
        form = SettingsForm()
        return render_template('settings.html', form=form)
    else:
        form = SettingsForm(request.form)
        if form.validate():
            for k, v in request.form.items():
                print('%s:%s' % (k, v))
            return 'success'
        else:
            print(form.errors)
            return 'fail'


if __name__ == '__main__':
    app.run(port=8001)
