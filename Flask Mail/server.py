from flask import Flask
from mimail import MiMail

app = Flask(__name__)

@app.route('/')
def index():
	mail = MiMail(app)
	if mail.sendMail('Hello Flask Mail', 'recipient_email_address'):
		return 'Email Sent!'
	else:
		return 'Error!'

if __name__ == "__main__":
	app.run(debug=True)
