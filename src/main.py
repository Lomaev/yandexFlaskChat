import sys
sys.path.insert(0, sys.path[0] + '\\DB')
from flask import Flask, render_template, request, session
from DB_code_core import DB, MessagesModel

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

messages_DB = DB('messages')
messages_model = MessagesModel(messages_DB.get_connection())
messages_model.init_table()


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        session['username'] = 'Anon'
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        messages_model.insert(user_name=request.form.get('username'), content=request.form.get('content'))
    return render_template('chat_window.html', username=session['username'] )


@app.route('/API/chat_content', methods=['GET', 'POST'])
def content():
    if request.method == 'POST':
        messages_model.insert(user_name=session['username'] if 'username' in session else 'Anon', content=str(list(request.form)[0]), type='image')
    return render_template('chat_content.html', messages=messages_model.get_all()[-10:])


if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')
