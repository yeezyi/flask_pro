from exts import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50))

    def __repr__(self):
        return "<User(username : %s )>" % self.username


article_tag_table = db.Table('article_tag',
                             db.Column("article_id", db.INTEGER, db.ForeignKey('article.id'), primary_key=True),
                             db.Column("tag_id", db.INTEGER, db.ForeignKey('tag.id'), primary_key=True)
                             )


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('articles'))
    tags = db.relationship('Tag', backref='articles', secondary=article_tag_table)
    def __repr__(self):
        return "<Article(title : %s )>" % self.title


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
