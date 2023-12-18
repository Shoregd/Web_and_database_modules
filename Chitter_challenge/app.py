import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.ChitterRepository import ChitterRepository



app = Flask(__name__)
global signedin, current_user 
signedin = False
current_user = None
@app.route('/',methods=['GET'])
def main_page():
    connection = get_flask_database_connection(app)
    repository = ChitterRepository(connection)
    peeps = repository.list_peeps()
    return render_template('main_page.html', signedin = signedin,username = current_user,peeps = peeps)

@app.route('/sign_in',methods = ['GET'])
def sign_in_page():
    return render_template('Sign_in.html')

@app.route('/sign_in',methods = ['POST'])
def checkuser_and_sign_in():
    username = request.form['username']
    useremail = request.form['user_email']
    connection = get_flask_database_connection(app)
    repository = ChitterRepository(connection)
    global signedin,current_user
    signedin,current_user = repository.sign_in(username,useremail)
    if signedin:
        return redirect('/')
    else:
        return render_template('Sign_in.html', errors='Username or Email is incorrect. Please try again.')

@app.route('/sign_up', methods=['GET'])
def sign_up_page():
    return render_template('Sign_up.html')


@app.route('/list_users',methods=['GET'])
def list_users():
    connection = get_flask_database_connection(app)
    repository = ChitterRepository(connection)
    result = repository.list_users()
    
    return redirect('/')

@app.route('/sign_up',methods=['POST'])
def check_add_user_and_sign_in():
    username = request.form['username']
    useremail = request.form['user_email']
    connection = get_flask_database_connection(app)
    repository = ChitterRepository(connection)
    errors = repository.add_user(username,useremail)
    
    if 'taken' in errors:
        return render_template('sign_up.html', errors = errors)
    global signedin,current_user
    signedin,current_user = repository.sign_in(username,useremail)
    return redirect('/')

@app.route('/sign_out',methods=['GET'])
def sign_user_out():
    connection = get_flask_database_connection(app)
    repository = ChitterRepository(connection)
    global signedin,current_user
    signedin,current_user = repository.sign_out()
    return redirect('/')


@app.route('/create_post',methods=['POST'])
def create_peep():
    message = request.form['message']
    connection = get_flask_database_connection(app)
    repository = ChitterRepository(connection)
    userid = repository.get_user_id(current_user)
    repository.add_peep(message,userid)
    return redirect('/')
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
