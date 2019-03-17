import sys
sys.path.insert(0, sys.path[0] + '\\DB')
from flask import Flask, render_template
from DB_code_core import DB, MessagesModel

app = Flask(__name__)

messages_DB = DB('messages')
messages_model = MessagesModel(messages_DB.get_connection())
messages_model.init_table()
messages_model.insert()
messages_model.insert(user_name='Masha', content='NO')
messages_model.insert(user_name='Admin', content='Yes')
print(messages_model.get_all())

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('chat_window.html')


@app.route('/API/chat_content')
def content():
    return render_template('chat_content.html', messages=messages_model.get_all())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
