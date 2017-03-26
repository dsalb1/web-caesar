import cgi

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