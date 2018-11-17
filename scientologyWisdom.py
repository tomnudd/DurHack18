import markovify

def wisdom():
	with open("scientology.txt") as f:
		text = f.read()
	text_model = markovify.Text(text)
	return text_model.make_sentence()

print(wisdom())
