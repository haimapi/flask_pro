from flask import Flask, render_template_string, request, url_for

app = Flask(__name__)


@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]



@app.template_filter('word_counter')
def word_counter_filter(s):
    return len(s.split(' '))

'''
@app.route('/')
def index():
    tpl = 'the string {{ str }} has {{ str | word_counter }} words!'
    return render_template_string(tpl, str='hello, xq, it is good!')
'''
@app.route('/')
def index():
    user = {'id':123, 'nickname':'<script>alert("xss vulnerable!")</script>'}
    tpl = '<h1>homepage of {{ nickname | safe }}</h1>'
    return render_template_string(tpl, **user)

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        tpl = '''
            <form method='POST' action='{{ url_for("test") }}'>
              <input type="text" name="msg" placeholder='input message'></input>
              <input type="submit" value="submit"></input>
            </form>
            '''
        return render_template_string(tpl)
    else:
        tpl = '''
            you just leave: {{ msg | safe }}
            '''
        return render_template_string(tpl, msg=request.form['msg'])

if __name__ == '__main__':
    app.run()
