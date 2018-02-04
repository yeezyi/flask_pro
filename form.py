from wtforms import Form, StringField, IntegerField, BooleanField, SelectField, FileField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, Regexp, URL, UUID
from wtforms.validators import ValidationError


class RegistForm(Form):
    # 变量名和表单的name要一致
    username = StringField(validators=[Length(min=3, max=10, message='长度')])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(
        validators=[Length(min=6, max=10, message='length'), EqualTo('password', message='No equal')])


class LoginForm(Form):
    # email = StringField(validators=[Email()])
    # username = StringField(validators=[InputRequired()])
    # age = IntegerField(validators=[NumberRange(min=0, max=100)])
    # phone = StringField(validators=[Regexp(r'1[34578]\d{9}')])
    # homepage = StringField(validators=[URL()])
    # uuid = StringField(validators=[UUID()])
    captcha = StringField(validators=[Length(max=4, min=4)])

    def validate_captcha(self, field):
        # field.data 存放要验证的数据
        if field.data != '1234':
            raise ValidationError('验证码错误!')


class SettingsForm(Form):
    # 第一个参数label是指渲染模板时使用form.username.label时的值,默认使用变量名首字母大写
    username = StringField('用户名:', validators=[InputRequired()])
    remember = BooleanField('记住我: ')
    # ('a', 'app') a为标签传递的值, app为标签显示的值
    tags = SelectField('学科:', choices=[('a', 'app'), ('b', 'base'), ('c', 'c++')])


from flask_wtf.file import FileRequired, FileAllowed
class UploadForm(Form):
    # 允许什么格式的文件能够上传
    upload_set = {'jpg', 'png', 'txt', 'gif'}
    avatar = FileField(validators=[FileRequired(), FileAllowed(upload_set=upload_set)])
    desc = StringField(validators=[InputRequired()])