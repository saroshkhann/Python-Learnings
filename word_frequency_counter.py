
def word_frequency(text):

    text = text.lower()
    for char in ".!,?'":
        text = text.replace(char, '')

    words = text.split()

    frequency = {}
    for word in words:
        if word  in frequency:
            frequency[word] +=1
        else:
            frequency[word] = 1

    print(frequency)





word_frequency("The cat sat on the mat. The cat is fat!")