from flask import Flask, render_template, url_for, redirect, request, abort, flash, session as login_session 
from database import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    if True: ##not session.get('logged_in'):
        return render_template('home_page.html', is_logged = True)
    else:
        return render_template('home_page.html', is_logged = False)

@app.route('/login', methods=['GET', 'POST'])
def log_in():
    if request.method == 'GET':
        return render_template('log_page.html')
    else:
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)
        if user.password == password:
            print (user)
            return render_template('home_page.html', username = username)
        else: 
            message = "wrong username or password!!! try again."
            return render_template('log_page.html', message = message)
    
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_page.html')
    else:
        username = request.form['username']
        password = request.form['password']        
        if valid_username(username) == True and valid_password(password) == True:
            add_user(username, password)
            user = get_user_by_username(username)
            print (user)
            login_session['username'] = username
            username = login_session['username']
            return render_template('home_page.html', username = username)
        elif valid_username(username) == False:
            message = "username is taken! choose another one :)"
            return render_template("sign_page.html", message = message)
        elif valid_password(password) == False:
            message = "password is too short! make it 4 letters or more :)"
            return render_template('sign_page.html', message = message)

@app.route('/items')
def items():
    if 'username' in login_session:
        username = login_session['username']
        puppets = get_all_puppets()
        return render_template('items_page.html', puppets = puppets, is_logged = True, username = username)
    else:
        puppets = get_all_puppets()
        return render_template('items_page.html', puppets = puppets, is_logged = False)
        
# @app.route('/puppet/<int:puppet_id>')
# def puppet(puppet_id):
#     puppet=session.query(Puppets).filter_by("id=puppet_id").first()
# return render_template('puppet.html', puppet=puppet)

@app.route('/cart') #/<int[]:puppets_id
def cart():
    return render_template('cart_page.html')

@app.route('/buynow',methods=['GET','POST'])
def buynow():
    return render_template('buynow_page.html')

@app.route("/templates/<string:filename>")
def templates(filename):
    return render_template(filename)

if __name__ == '__main__':
    app.run(debug=True)
 
# def do_admin_login():
# if request.form['password'] == 'password' and request.form['username'] == 'admin':
# session['logged_in'] = True
# {% block body %}
# {% if session['logged_in'] %}
 
# You're logged in already!
 
# {% else %}
# <form action="/login" method="POST">
#   <input type="username" name="username" placeholder="Username">
# <input type="password" name="password" placeholder="Password">
# <input type="submit" value="Log in">
# </form>{% endif %}
# {% endblock %}