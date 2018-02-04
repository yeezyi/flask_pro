from flask import Flask, render_template,request
import config
from form import RegistForm, LoginForm, SettingsForm
import os
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


# @app.route('/upload/', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'GET':
#         return render_template('upload.html')
#     else:
#         desc = request.form.get('desc', 'No DESCRIBE')
#         avatar = request.files.get('avatar')
#         upload_path = os.path.join(os.path.dirname(__file__), 'upload_files')
#         from werkzeug.utils import secure_filename
#         # 对文件名进行包装,解决安全隐患
#         filename = secure_filename(avatar.filename)
#         print(filename)
#         avatar.save(os.path.join(upload_path, filename))
#         print(desc)
#         return 'success'

from form import UploadForm
@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # 将两个不可变字典(request.form,request.file)组合成一个字典
        from werkzeug.datastructures import CombinedMultiDict
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            desc = request.form.get('desc', 'No DESCRIBE')
            # 或 desc = form.desc.data
            avatar = request.files.get('avatar')
            # 或 avatar = form.avatar.data
            upload_path = os.path.join(os.path.dirname(__file__), 'upload_files')
            from werkzeug.utils import secure_filename
            # 对文件名进行包装,解决安全隐患
            filename = secure_filename(avatar.filename)
            print(filename)
            avatar.save(os.path.join(upload_path, filename))
            print(desc)
            return 'success'
        else:
            print(form.errors)
            return 'fail'



@app.route('/getfile/<filename>/')
def get_file(filename):
    from flask import send_from_directory
    file_path = os.path.join(os.path.dirname(__file__), 'upload_files')
    return send_from_directory(file_path, filename)


if __name__ == '__main__':
    app.run(port=8001)
