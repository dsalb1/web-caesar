import webapp2
from caesar import alphabet_position, rotate_character, encrypt

form = """
<!DOCTYPE HTML>
<head>
	<title>Web Caesar</title>
</head>
<html>
<body>
	<h1>Web Caesar</h1>
	<h3>Enter some text to encrypt:</h3>
		<form method="post" id="encrypt_form">
			<textarea name="message" rows="5" cols="40" form="encrypt_form">%(encrypted_message)s
			</textarea>
			<p><label>Enter how much you would like to rotate the letters:</label></p>
			<div style="color:red">%(error)s</div>
			<p><input type="text" name="rot"/><input type="submit" value="Encrypt"/></p>			
		</form>
</body>
</html>
""" 

class MainHandler(webapp2.RequestHandler):
	def write_form(self, encrypted_message="", error=""):
		self.response.write(form % {"encrypted_message":encrypted_message, "error":error,})

	def get(self):
		self.write_form()

	def post(self):
		#global encrypted_message, form
		new_message = self.request.get("message")
		rot = self.request.get("rot")

		if rot and rot.isdigit():
			encrypted_message = encrypt(new_message, rot)
			self.write_form(encrypted_message)
		else:
			error = "That is not a valid number, friend. Try again."
			self.write_form(new_message, error)
		

app = webapp2.WSGIApplication([
	('/', MainHandler),
], debug=True)
