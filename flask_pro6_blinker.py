from flask import Flask, template_rendered, render_template
from blinker import Namespace

# 1.定义信号
# Namespace的作用是防止多人开发时,信号名字的冲突
myspace = Namespace()
fire_signal = myspace.signal('fire')

# 2.监听信号 fire_signal.connect(func) # 要指定接受到信号后执行的函数
def fire_signal_listen(sender):
    # sender 指信号是谁发送的
    print(sender)
    print('fire_signal_listen..')
fire_signal.connect(fire_signal_listen)

# 3.发送信号
fire_signal.send('firesender')




app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True, port=5006)
