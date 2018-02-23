from flask import Flask
from blueprints.bp_restful import bp_rest
import config
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(bp_rest)



if __name__ == '__main__':
    app.run(debug=True, port=5008)