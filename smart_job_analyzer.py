import pandas as pd

class SmartJob:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)

    def view_all_jobs(self):
        print("-------- JOB LIST --------")

        for index, row in self.data.iterrows():
            print(f"{index+1}. {row['job_title']} | {row['company']} | {row['location']} | {row['salary']}")

        print("--------------------------")
        print(f"Total jobs: {len(self.data)}")

    def search_job(self, skills):

        try:
            print("-------- MATCHING JOBS --------")

            total_matches = 0
            for index, row in self.data.iterrows():
                skill = row["skills"].split(",")

                if skills not in skill:
                    raise ValueError("No jobs found for this skill!")


                for item in skill:
                    if item.lower() == skills.lower():
                        print(f"{row['job_title']} | {row['salary']} PKR")
                        total_matches+=1

            print("----------------------------")
            print(f"Total Matches: {total_matches}")

        except ValueError as e:
            print(f"Error: {e}")

    def skill_demand(self):
        all_skills = []
        skills_column = self.data["skills"]

        for skills in skills_column:
            split_skills = skills.split(",")

            for skill in split_skills:
                all_skills.append(skill.strip())

        skill_series = pd.Series(all_skills)
        skill_count = skill_series.value_counts()

        for skill, count in skill_count.items():
            print(f"{skill} -> {count} jobs")

    def salary_analysis(self):

        print("-------- SALARY ANALYSIS --------")
        total_salary = 0

        for index, row in self.data.iterrows():
            total_salary += row["salary"]

        total_data = len(self.data)
        average_salary = int(total_salary/ total_data)

        print(f"Average Salary: {average_salary} PKR")

        highest_salary = 0
        highest_job = ""
        for index , row in self.data.iterrows():
            if row["salary"] > highest_salary:
                highest_salary = row["salary"]
                highest_job = row["job_title"]

        print("Highest Salary: ")
        print(f"{highest_salary} PKR ({highest_job})")

        lowest_salary = 10000000000
        lowest_job = ""

        for index , row in self.data.iterrows():
            if row["salary"] < lowest_salary:
                lowest_salary = row["salary"]
                lowest_job = row["job_title"]

        print(f"{lowest_salary} PKR ({lowest_job})")




system = SmartJob()

system.load_data("jobs_dataset.csv")


is_on = True

while is_on:
    print("-------- JOB MARKET ANALYZER --------")
    print("1. View all jobs")
    print("2. Search jobs by Skill")
    print("3. Skill Demand Analysis")
    print("4. Salary Analysis")
    print("5. Career Recommendation")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice"))

        if choice == 1:
            system.view_all_jobs()
        elif choice == 2:
            skill = input("Enter skill: ")
            system.search_job(skill)
        elif choice == 3:
            system.skill_demand()
        elif choice ==4:
            system.salary_analysis()
        elif choice == 5:
            skills = input("Enter your skills")
            system.career_recommendation(skill)
        elif choice == 6:
            print("Exiting")
            is_on = False

    except ValueError:
        print("Please write choice in digits")
