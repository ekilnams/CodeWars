def reverse_words(text):
	words = text.split(" ")
	reversed_words = []
	for word in words:
		length = len(word)
		index = 0
		reversed = ""
		while index < length:
			reversed = reversed + word[length - 1 - index]
			index = index + 1
		reversed_words.append(reversed)
	return " ".join(reversed_words)