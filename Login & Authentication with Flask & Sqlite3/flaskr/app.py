from flask import Flask, render_template, redirect, url_for, request, session
from misqlite3 import Login

app = Flask(__name__)
app.secret_key = "secret_key"

db = Login('dbFilename')

@app.route('/')
def index():
    if "user" in session:
        return render_template('index.html', title='Dashboard', stylesheet='index.css')
    return redirect(url_for('login'))

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        db.open()
        username = request.form['uname']
        password = request.form['upwd']
        result = db.getUser(username, password)
        db.close()
        if result:
            flash("Login Successful!")
            session['user'] = username
            return redirect(url_for('index'))
        else:
            flash("Login Fail!")
    return render_template('login.html', title='Login', stylesheet='login.css')

@app.route('/sign-up', methods=["POST", "GET"])
def signup():
    return render_template('sign-up.html', title='sign-up', stylesheet='sign-up.css')
    
if __name__ == "__main__":
    app.run(debug=True)
