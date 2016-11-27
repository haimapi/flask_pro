import os
from flask import Flask
from flask.ext.stormpath import StormpathManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'IAMSECRETSTRING'
app.config['STORMPATH_API_KEY_ID'] = os.environ.get('STORMPATH_API_KEY_ID')
app.config['STORMPATH_API_KEY_SECRET'] = os.environ.get('STORMPATH_API_KEY_SECRET')
app.config['STORMPATH_APPLICATION'] = os.environ.get('STORMPATH_APPLICATION')

stormpath_manager = StormpathManager(app)

@app.route('/')
def index():
    return "<h1>HOLA</h1>"

if __name__ == '__main__':
    app.run()
