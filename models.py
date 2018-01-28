from exts import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User(username : %s )>" % self.username


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.INTEGER, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('articles'))

    def __repr__(self):
        return "<Article(title : %s )>" % self.title
