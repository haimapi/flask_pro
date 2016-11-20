from flask import Flask, request, url_for, session, make_response
from flask.globals import _request_ctx_stack, _app_ctx_stack
app = Flask(__name__)

#app.config['SERVER_NAME'] = 'haimapi.com'
app.config['SECRET_KEY'] = '8\xceK\x9c\xef\xc6\xadY\xddoOA\x07Q\x0e\xfa\xf3`\x81\xb9\x1b\\FQ'

'''
@app.route('/haha')
def v_index():
    print request
    print _request_ctx_stack.top.request
    print _app_ctx_stack.top
    return 'see console'

with app.app_context():
    print url_for('v_index')
'''
'''
env = {
    'SERVER_NAME': 'fake.com',
    'SERVER_PORT': '80',
    'REQUEST_METHOD': 'GET',
    'PATH_INFO': '/genius',
    'wsgi.url_scheme': 'http'
}
with app.request_context(env):
    print request
'''

@app.route('/')
def index():
    return 'this is not the point'

@app.before_first_request
def before_first_request():
    print 'before process first request'

@app.before_request
def before_request():
    print 'before each request'

@app.after_request
def after_request(rsp):
    print 'after each process'
    return rsp

@app.teardown_request
def teardown_request(e):
    print 'teardown request context'

@app.teardown_appcontext
def teardown_appctx(e):
    print 'teardown application context'


@app.route('/vvv_index')
def v_index():
    session['counter'] = 1
    '''
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return 'this is the {} visit'.format(session.get('counter'))
    '''
    rsp = make_response('{}'.format(session['counter']))
    rsp.set_cookie('name', 'xq')
    return rsp

if __name__ == '__main__':
    app.run()
