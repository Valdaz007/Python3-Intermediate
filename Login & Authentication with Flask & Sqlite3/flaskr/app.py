from flask import Flask, render_template, redirect, url_for, request, session
from misqlite3 import Login

app = Flask(__name__)
app.secret_key = "secret_key"

db = Login()

@app.route('/')
def index():
    if 'user' not in session:
        redirect(url_for('login'))
    for i in session:
        print(i)
    return render_template('index.html', title='Dashboard', stylesheet='index.css')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        db.open('test.db')
        username = request.form['uname']
        password = request.form['upwd']
        print(db.getUser(username))
        db.close()
        return redirect(url_for('login'))
    
    return render_template('login.html', title='Login', stylesheet='login.css')

@app.route('/sign-up', methods=["POST", "GET"])
def signup():
    return render_template('sign-up.html', title='sign-up', stylesheet='sign-up.css')
    
if __name__ == "__main__":
    app.run(debug=True)
