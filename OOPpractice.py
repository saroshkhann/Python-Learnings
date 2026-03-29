class Introduction:
    def __init__(self, str_1, str_2):
        self.string1 = str_1
        self.string2 = str_2

    def string_concat(self):
        return self.string1 + self.string2


user_1 = Introduction("Sarosh", "Khan")
print(user_1.string_concat())

