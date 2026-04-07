import pandas as pd

class FitnessTracker:
    def __init__(self):
        self.users = {}
        self.workout = None
        self.meal = None

    def ensure_user(self, username):
        if username not in self.users:
            self.users[username] = {
                "workouts": [],
                "meals": []
            }

    def get_username(self):
        return input("Enter username: ")

    def load_data(self, file_path):
        try:
            self.workout = pd.read_csv(file_path)

            for index, row in self.workout.iterrows():
                username = row["username"]

                self.ensure_user(username)

                workout_entry = {
                    "type": row["type"],
                    "duration": row["duration_minutes"],
                    "calories": row["calories_burned"]
                }

                self.users[username]["workouts"].append(workout_entry)

        except ValueError as e:
            print(f"Error: {e}")

    def load_data_meal(self, file_path):
        try:
            self.meal = pd.read_csv(file_path)

            for index, row in self.meal.iterrows():
                username = row["username"]

                self.ensure_user(username)

                meals_entry = {
                    "name": row["meal_name"],
                    "calories": row["calories"],
                    "protein": row["protein"],
                    "carbs": row["carbs"],
                    "fat": row["fat"]
                }

                self.users[username]["meals"].append(meals_entry)

        except FileNotFoundError:
            print("File is not loaded")

    def register_user(self, username):
        try:
            if username in self.users:
                raise ValueError("User already exists!")

            self.users[username] = {
                "workouts": [],
                "meals": []
            }
            print(f"User '{username}' added successfully")
            print(self.users)


        except ValueError as e:
            print(f"Error: {e}")

    def log_workouts(self, username, type, duration, calories):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")


            user = self.users[username]
            user_workouts = user["workouts"]

            workout_data = {
                "type": type,
                "duration": duration,
                "calories": calories
            }

            user_workouts.append(workout_data)
            print("Workout added successfully")

        except ValueError as e:
            print(f"Error: {e}")

    def log_meal(self, username, meal_name, calories, protein, carbs, fat):
        try:
            if username not in self.users:
                raise ValueError("User does not exist!")

            user = self.users[username]
            user_meals = user["meals"]
            print(user_meals)

            meals_data = {
                "name": meal_name,
                "calories": calories,
                "protein": protein,
                "carbs": carbs,
                "fat": fat
            }

            user_meals.append(meals_data)
            print("Meal added successfully")

        except ValueError as e:
            print(f"Error: {e}")

    def view_workouts(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            user = self.users[username]
            workouts = user["workouts"]

            print(f"Workouts for '{username}'\n")
            if len(workouts) == 0:
                print("No workouts found.")
                return
            for workout in workouts:
                 print(f"type: {workout['type']} Duration: {workout['duration']} Calories: {workout['calories']} ")

        except ValueError as e:
            print(f"Error: {e}")

    def view_meals(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            user = self.users[username]
            meals = user["meals"]

            print(f"Meals for '{username}'\n")
            if len(meals) == 0:
                print("No meals found.")
                return

            for meal in meals:
                print(f"Meal: {meal['name']}")
                print(f"Calories: {meal['calories']} | Protein: {meal['protein']}g | Carbs: {meal['carbs']}g | Fat: {meal['fat']}")

        except ValueError as e:
            print(f"Error: {e}")

    def analytics_and_insights(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            user = self.users[username]
            meals = user["meals"]
            workout = user["workouts"]

            # CALORIES

            # if len(meals) or len(workout) == 0:
            #     print(f"No workouts or meals found for user '{username}'")
            #     return

            total_calories_consumed = 0
            for meal in meals:
                total_calories_consumed += meal["calories"]

            total_calories_burned = 0
            for burned in workout:
                total_calories_burned += burned["calories"]

            net_calories = total_calories_consumed - total_calories_burned

            print("Calorie Summary: ")

            print(f"Total Calories Consumed: {total_calories_consumed} kcal")
            print(f"Total Calories Burned: {total_calories_burned} kcal")
            if net_calories == 0:
                print(f"Net Calories: {net_calories} kcal (Balanced)\n")
            elif net_calories > 0:
                print(f"Net Calories: +{net_calories} kcal (Surplus)\n")
            elif net_calories < 0:
                print(f"Net Calories: -{net_calories} kcal (Deficit)\n")

            # MACRONUTRIENTS
            print("Macronutrients:")
            protein_consumed = 0
            for protein_c in meals:
                protein_consumed += protein_c["protein"]
            print(f"Protein: {protein_consumed}g")

            carbs_consumed = 0

            for carbs_c in meals:
                carbs_consumed += carbs_c["carbs"]
            print(f"Carbs: {carbs_consumed}g")

            fat_consumed = 0

            for fat_c in meals:
                fat_consumed += fat_c["fat"]
            print(f"Fat: {fat_consumed}g\n")

            # WORKOUT INSIGHTS
            print("Workout Insights")
            workout_types = [ty["type"] for ty in workout]

            if not workout_types:
                print("No workout data available")
                return

            freq = {}

            for w in workout_types:
                if w in freq:
                    freq[w] +=1
                else:
                    freq[w] = 1

            most_frequent = max(freq, key = freq.get)
            count = freq[most_frequent]

            print(f"Most Frequent Workout: {most_frequent} ({count} times)")
            print(f"Total Workouts Logged: {len(workout)}")

            # MEAL INSIGHTS
            print("\nMeal Insights: ")
            frequent_meal = [m["name"] for m in meals]

            if not frequent_meal:
                print("No meals data available")

            freq_meal = {}
            for m in frequent_meal:
                if m in freq_meal:
                    freq_meal[m] +=1
                else:
                    freq_meal[m] = 1

            most_frequent_meal = max(freq_meal, key= freq_meal.get)
            count_meal = freq_meal[most_frequent_meal]
            print(f"Most Frequent Meal: {most_frequent_meal} ({count_meal} times)")
            print(f"Total meals logged: {len(meals)}\n")

            # RECOMMENDATIONS
            print("Recommendations:")
            if total_calories_consumed > total_calories_burned:
                print("- You are in a calorie surplus. Consider increasing workouts.")
            if total_calories_burned > total_calories_consumed:
                print("- Try adding more cardio (running, cycling).")

            if protein_consumed < 50:
                print("- Protein intake is slightly low. Include eggs, chicken, or legumes.")

        except ValueError as e:
            print(f"Error : {e}")



system = FitnessTracker()

system.load_data("workouts.csv")
system.load_data_meal("meals.csv")


while True:
    print("1. Register User")
    print("2. log Workouts")
    print("3. Log Meal")
    print("4. View Workouts")
    print("5. View Meals")
    print("6. Analytics & Insights")

    try:
        choice = int(input("Enter choice"))

        if choice == 1:
            system.register_user(system.get_username())
        elif choice == 2:
            username = system.get_username()
            type = input("Enter type")
            duration = int(input("Duration in minutes: "))
            calories = int(input("Calories Burned: "))
            system.log_workouts(username, type, duration, calories)
        elif choice == 3:
            username = system.get_username()
            meal_name = input("Enter meal name")
            calories = int(input("Enter Calories"))
            protein = int(input("Enter Protein"))
            carbs = int(input("Enter Carbs"))
            fat = int(input("Enter Fat"))
            system.log_meal(username, meal_name, calories, protein, carbs, fat)
        elif choice == 4:
            system.view_workouts(system.get_username())
        elif choice == 5:
            system.view_meals(system.get_username())
        elif choice == 6:
            system.analytics_and_insights(system.get_username())

    except ValueError:
        print("Please write in Digits not Alphabets")