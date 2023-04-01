from flask_mail import Mail, Message

class MiMail():
	def __init__(self, app):
		app.config['DEBUG'] = True
		app.config['TESTING'] = False
		app.config['MAIL_SERVER'] = '<your_mail_server>'
		app.config['MAIL_PORT'] = <port_number>   # Depends on which security you use TLS or SSL
		app.config['MAIL_USE_TLS'] = True
		app.config['MAIL_USE_SSL'] = False
		app.config['MAIL_DEBUG'] = True
		app.config['MAIL_USERNAME'] = '<sender_email>'
		app.config['MAIL_PASSWORD'] = '<sender_email_pwd>'
		app.config['MAIL_DEFAULT_SENDER'] = 'sender_email'
		app.config['MAIL_MAX_EMAILS'] = None
		#app.config['MAIL_SUPPRESS_SEND'] = False
		app.config['MAIL_ASCII_ATTACHMENTS'] = False
		self.mail = Mail(app)

	def sendMail(self, subject, body, recvr):
		try:
			msg = Message(subject, recipients=[recvr])
			msg.body = body
			self.mail.send(msg)
			return True
		except:
			return False
