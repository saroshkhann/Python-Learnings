def calculate_love_score(name1, name2):
    name = (name1 + name2).lower()
    true_letters = ["t", "r", "u", "e"]
    love_letters = ["l", "o", "v", "e"]

    true_score = 0
    love_score = 0
    for letter in true_letters:
        true_score+= name.count(letter)
    for letters in love_letters:
        love_score += name.count(letters)

    finaL_score = str(true_score) + str(love_score)
    print(finaL_score)

calculate_love_score("Sarosh khan", "Jack")