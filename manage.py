from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from main import app, db, User, Post, Comment


manager = Manager(app)
migrate = Migrate(app)

# manager.add_command('server', Server())
manager.add_command('db', )

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment)


if __name__ == "__main__":
    manager.run()
