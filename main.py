import webapp2
import cgi

add_header = """
<!DOCTYPE HTML>
<head>
	<title>Web Caesar</title>
</head>
<html>
<body>
	<h1>Web Caesar</h1>
	<h3>Enter some text to encrypt</h3>
"""

add_footer = """
</body>
</html>
"""
new_message = ""

message_form1 = """
<form action="/encrypt" method="post" id="encrypt_form">
	<textarea name="message" rows="5" cols="40" form="encrypt_form">"""

message_form2="""
</textarea>
	<p><label>Enter how much you would like to rotate the letters</label></p>
	<p><input type="text" name="rot"/></p>
	<p><input type="submit" value="Encrypt"/></p>
</form>
"""

def alphabet_position(letter):
	result = ord(letter.lower()) - 97
	return int(result)

def rotate_character(char, rot):
	rot = int(rot)
	new_position = (alphabet_position(char) + rot) % 26
	if char.isupper():
		new_char = chr(new_position + 65)
	else:
		new_char = chr(new_position + 97)
	return new_char

def encrypt(text, rot):
	encrypted_text = ""
	for letter in text:
		if letter.isalpha():
			new_character = rotate_character(letter, rot)
			encrypted_text += new_character
		else:
			letter = cgi.escape(letter)
			encrypted_text += letter
	return encrypted_text

class MainHandler(webapp2.RequestHandler):
	def get(self):
		content = add_header + message_form1 + new_message + message_form2 + add_footer
		self.response.write(content)

class AddMessage(webapp2.RequestHandler):
	def post(self):
		new_message = self.request.get("message")
		rot = self.request.get("rot")
		encrypted_message = encrypt(new_message, rot)
		content = add_header + message_form1 + encrypted_message + message_form2 + add_footer
		self.response.write(content)

app = webapp2.WSGIApplication([
	('/', MainHandler),
	("/encrypt", AddMessage)
], debug=True)
