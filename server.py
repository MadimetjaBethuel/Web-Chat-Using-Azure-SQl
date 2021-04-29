

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_restful import Api
from flask_sse import sse
import random
import string
from config import *


app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')
api = Api(app)

NAME_KEY = 'username'

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

letters = string.digits
result_str = ''.join(random.choice(letters) for i in range(3))


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and 'username' in request.form:
        username = request.form['username']

        query_login = "SELECT * FROM users WHERE Name = ?"

        cursor.execute(query_login, username)

        account = cursor.fetchone()
        session['user'] = username
        if account:

            if 'user' in session:
                x = '1'
                query_insert_status = "UPDATE users SET Status= ?"
                cursor.execute(query_insert_status, x)
                cursor.commit()
                flash("Logged in")

                return redirect(url_for('userlist'))
        else:
            flash('Incorrect name')
            return redirect(url_for('register'))
            cursor.close()
    return render_template('index.html')


@ app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        x = '0'
        qery_log = "UPDATE users SET Status= ?"
        cursor.execute(qery_log, x)
        cursor.commit()
        session.pop(user, None)
        session.clear()

        flash('you are logged out')
        return redirect(url_for('login'))
    return redirect(url_for('login'))


@ app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']

        query_register = "SELECT * FROM users WHERE Name = ?"

        cursor.execute(query_register, username)

        account = cursor.fetchall()

        if account:
            return redirect(url_for('userlist'))
        else:
            insert_username = "INSERT INTO users (Name) VALUES (?)"

            cursor.execute(insert_username, username)
            cursor.commit()
            return redirect(url_for('userlist'))

    return render_template('register.html')


@app.route('/userlist')
def userlist():

    if 'user' in session:

        query_get_users = " SELECT * FROM users"
        Allusers = cursor.execute(query_get_users)
        users = Allusers.fetchall()

        return render_template('userlist.html', users=users)
    else:
        return redirect(url_for('login'))


@app.route('/chat/<string:name>', methods=['POST', 'GET'])
def chat(name):
    if 'user' in session:
        session['name'] = name

        query_get_users = "SELECT * FROM users"
        Allusers = cursor.execute(query_get_users)
        chatusers = Allusers.fetchall()

        '''query_message = "SELECT * FROM messages"

        Allmessages = cursor.execute(query_message)

        messages = Allmessages.fetchall()
            '''
        if request.method == 'POST':

            out_going_id = request.form['outgoing_id']
            incoming_id = request.form['incoming_id']
            message = request.form['message']

            send_message = "INSERT INTO messages(icoming_msg_id,outgoing_msg_id,msg) VALUES (?,?,?) "
            cursor.execute(send_message, incoming_id, out_going_id, message)
            cursor.commit()

            query_message = "SELECT * FROM messages"

            Allmessages = cursor.execute(query_message)

            messages = Allmessages.fetchall()

            # messages=messages)
            return render_template('chat.html', chatusers=chatusers)
    else:
        return redirect(url_for('login'))
    # messages=messages)
    return render_template('chat.html', chatusers=chatusers)


@app.route('/messages', methods=['POST', 'GET'])
def messages():
    if 'user' in session:

        query_message = "SELECT * FROM messages"

        Allmessages = cursor.execute(
            query_message)

        messages = Allmessages.fetchall()

        return render_template('chat.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
