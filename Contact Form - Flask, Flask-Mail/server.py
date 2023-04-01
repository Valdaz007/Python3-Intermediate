from flask import Flask, render_template, request, flash, redirect, url_for
from mimail import MiMail

app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretkeyS"

@app.route('/')
def index():
	return render_template('index.html', title="Home")

@app.route('/email', methods=["POST", "GET"])
def sendMail():
	if request.method == "POST":
		email = request.form["email"]
		subject = request.form["subject"]
		body = request.form["body"]
		mail = MiMail(app)
		if mail.sendMail(subject, body, email):
			flash("Email Sent")
			return redirect(url_for('index'))
		else:
			return 'Error!'

if __name__ == "__main__":
	app.run(debug=True)
