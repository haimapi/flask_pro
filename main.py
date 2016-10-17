from flask import Flask, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from config import DevConfig
from flask import Blueprint


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


## define blueprint ##
blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder='templates/blog',
    url_prefix='/blog'
)

vote_blueprint = Blueprint(
    'vote',
    __name__,
    template_folder='templates/vote',
    static_folder='static/vote',
    url_prefix='/vote'
)




class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        lazy='dynamic',
        backref='user'
    )

    def __init__(self, username):
        self.username = username


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    pub_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    comments = db.relationship(
        'Comment',
        lazy='dynamic',
        backref='post'
    )

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Post {}>'.format(self.title)


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Comment {}>'.format(self.name)


#tags = db.Table('post_tags',
#    db.Column('post_id', db.Integer(), db.ForeignKey('post.id')),
#    db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id'))
#)


@blog_blueprint.route('/')
def home():
    return '<h3>welcome to blog</h3>'


@vote_blueprint.route('/')
def home():
    return '<h2>vote page</h2>'

@app.route('/')
def index():
    return redirect(url_for('blog.home'))


app.register_blueprint(blog_blueprint)
app.register_blueprint(vote_blueprint)

if __name__ == "__main__":
    app.run()
