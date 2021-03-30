list = ['Mickey Mouse was a kind of mouse.', 'Mickey Mouse was a kind of mouse. A mouse with a sense of humour.']

for i in list:
    words = i.split()
    final = []
    i = 0
    for word in words:
        if word[0] == "m" and i == 0:
            final.append(word.capitalize())
            i += 1
        else:
            final.append(word)
    print(" ".join(final))

#dont understand this