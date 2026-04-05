class Netflix:
    def __init__(self):
        self.users = []
        self.movie = []
        self.genre_count = []

    def menu(self):
        print("1. Register User")
        print("2. Add Movie")
        print("3. Watch Movie")
        print("4. View History")
        print("5. Get Recommendations")
        print("6. Exit")

    def register_user(self):
        username = input("Enter username: ")

        for user in self.users:
            if user["username"] == username:
                print("User already exists.")
                return


        self.users.append({"username": username, "movies": [], "genre": '', "genre_count": 0})
        print(f"User '{username}' registered successfully.")
        print(self.users)

    def add_movie(self):
        title = input("Enter movie title: ")
        for m in self.movie:
            if m["title"] == title:
                print("Movie already exists.")
                return

        genre = input("Enter genre: ")
        self.movie.append({"title": title, "genre": genre})
        print(self.movie)

        print(f"Movie '{title}' added successfully.")

    def watch_movie(self):
        username = input("Enter username")
        title = input("Enter movie title: ")
        found = False
        for item in self.users:
            for movie in self.movie:
                if movie["title"] == title and item["username"] == username:
                    found = True
                    item["movies"].append(title)
                    print(self.users)
                    print(f"{username} is watching '{title}'")
                    print(self.users)
                    item["genre_count"] +=1
                    print(self.users)

        if not found:
            print("Movie not found.")
            return

    def watch_history(self):
        username = input("Enter username: ")

        counter = 1
        found = False
        for movie in self.users:
            if movie["username"] == username:
                if len(movie["movies"]) == 0:
                    print("No watch history found")
                found= True
                for m in movie["movies"]:

                    print(f"{counter}. {m}")
                    counter+=1
        if not found:
            print("user not found.")

    # def recommendations(self):



user = Netflix()

is_on = True

while is_on:
    user.menu()
    choice = int(input("Enter the choice you want to perform"))

    if choice == 1:
        user.register_user()
    elif choice == 2:
        user.add_movie()
    elif choice ==3:
        user.watch_movie()
    elif choice==4:
        user.watch_history()
