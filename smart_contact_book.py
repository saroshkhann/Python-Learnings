contacts = []

def add_contact():
    name = input("Enter Your Name: ")
    phone = input("Enter you Phone Number: ")
    city = input("Enter your City: ")
    contacts.append({"name": name.lower(), "phone": phone, "city": city.lower()})

def view_contacts():
    counter = 1
    for contact in contacts:
        print(f"{counter}. {contact["name"]} - {contact["phone"]} - {contact["city"]}")
        counter +=1

def search_contact():
    search_by_name = input("Enter the name to search: ")
    found = False
    for search in contacts:
        if search["name"] == search_by_name.lower():
            print("Found:")
            print(f"{search["name"]} - {search["phone"]} - {search["city"]}")
            found = True
    if not found:
        print("Contact not found")

def filter_city():
    filter_by_city = input("Enter city: ")
    found = False

    print(f"Contacts in {filter_by_city}")

    for person_city in contacts:
        if person_city["city"] == filter_by_city.lower():
            print(f"{person_city["name"]} - {person_city["phone"]}")
            found = True
    if not found:
        print("No contacts found in this city")


def delete_contact():
    deleted = input("Enter name to delete: ")

    found = False

    for delete_person in contacts:
        if delete_person["name"] == deleted.lower():
            contacts.remove(delete_person)
            print("Contact deleted successfully!")
            found = True
            break
    if not found:
        print("Contact not found!")

def menu():
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Filter Contact")
    print("5. Delete Contact")
    print("6. Exit")


is_on = True

while is_on:
    menu()
    choice = int(input("Choose the operation you want to perform"))

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        filter_city()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        is_on = False