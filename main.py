import os
from flask import Flask, redirect, url_for, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from config import DevConfig
from flask import Blueprint


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
mail = Mail(app)


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
## end of blueprint



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
    return render_template('blog.html')


@vote_blueprint.route('/')
def home():
    return render_template('vote.html')

@app.route('/')
def index():
    print request.cookies
    return render_template('index.html')

@app.route('/music')
def music():
    #print request.form['uid']
    return render_template('music.html')


@app.route('/movie')
def movie():
    return render_template('movie.html')


@app.route('/search')
def search():
    return request.args['search_content']



@app.route('/book')
def book():
    return render_template('book.html')


@app.route('/json_test', methods=['GET', 'POST'])
def json_test():
    print request.json
    return render_template('json_test.html')




@app.route('/user/<uname>/friend/<fname>')
def user(uname, fname):
    return "<h1>{0}'s friend is {1}</h1>".format(uname, fname)


@app.route('/add/<int:num_1>/<int:num_2>')
def add(num_1, num_2):
    return '{0} + {1} = {2}'.format(num_1, num_2, num_1+num_2)


@app.route('/file/<path:fname>')
def read_file(fname):
    base_dir = os.getcwd()
    fullname = os.path.join(base_dir, 'share', fname)
    fp = open(fullname)
    cnt = fp.read()
    fp.close()
    return cnt

@app.route('/auth', methods=['POST'])
def auth():
    uid = request.form['uid']
    pwd = request.form['pwd']
    sys = request.form['system']
    log_in_success = False
    if uid == 'jon' and pwd == '123' and sys == 'CRM':
        log_in_success = True
    return render_template('auth.html', log_in_status=log_in_success)

@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

app.register_blueprint(blog_blueprint)
app.register_blueprint(vote_blueprint)

if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0')
