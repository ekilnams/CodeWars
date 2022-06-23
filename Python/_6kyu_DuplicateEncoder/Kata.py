def duplicate_encode(word):
    word = word.lower()
    transformed = ""
    for char in word:
        if word.count(char) > 1:
            transformed = transformed + ")"
        else:
            transformed = transformed + "("
    return transformed
