#Real World Practice Project Contact Book CLI application


contacts = []


def newcontact():
    name = input("Enter the name: ").strip()
    PhoneNumber = input("Enter the phone number: ").strip()

    aContact = {
        "name": name,
        "PhoneNumber": PhoneNumber
    }

    # Validation
    if not name:
        print("Name cannot be empty")
        return
    if not PhoneNumber:
        print("Phone number cannot be empty")
        return
    if not PhoneNumber.isdigit():
        print("Phone number must contain only digits")
        return
    if len(PhoneNumber) < 7 or len(PhoneNumber) > 12:
        print("Phone number length must be between 7 and 12")
        return

    # Add contact
    if any(contact["name"].lower() == name.lower() for contact in contacts):
        print("Contact already exists")
        return
    else:
        contacts.append(aContact)
        print("Contact added successfully")





def viewcontacts():
    print("--------Contact List--------")
    if not contacts:
        print("No contacts found")
    else:
        for contact in contacts:
            print(f"{contact['name']}: {contact['PhoneNumber']}")





def updatecontacts():
    updateContact = input("Enter the name of the contact you want to update: ").lower().strip()
    newContact = input("Enter the new number: ").strip()

    # Validation
    if not newContact:
        print("Phone number cannot be empty")
        return
    if not newContact.isdigit():
        print("Phone number must contain only digits")
        return
    if len(newContact) < 7 or len(newContact) > 12:
        print("Phone number length must be between 7 and 12")
        return


    found = False

    for contact in contacts:
        if contact["name"].lower() == updateContact:
            contact["PhoneNumber"] = newContact
            print("Contact updated successfully")
            found = True
            break

    if not found:
        print("No such contact found!")





def deletecontacts():
    deleteContact = input("Enter the name of the contact you want to delete: ").lower().strip()

    found = False

    for i in range(len(contacts)):
        if contacts[i]["name"].lower().strip() == deleteContact:
            contacts.pop(i)
            print("Contact deleted successfully")
            found = True
            break

    if not found:
        print("No such contact found!")





def searchcontacts():
    searchContact = input("Enter the name of the contact you want to search: ").lower().strip()

    found = False

    for contact in contacts:
        if contact["name"].lower().strip() == searchContact:
            print(f'Your contact is :  \n -> {contact["name"]}  :  {contact["PhoneNumber"]}')
            found = True
            break

    if not found:
        print("No such contact found!")




def totalcontacts():
    print("--------Total Contacts --------")
    print(f"The total number of contacts are: {len(contacts)}")


def exitingcontacts():
    print("Thank you for using this application")
    exit()


while True:
    print("\nWelcome to the contact book Application")
    print("Choose an option:")
    print("1. Create a new contact")
    print("2. View all contacts")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Search for a contact")
    print("6. Count the total number of contacts")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if choice == 1:
        newcontact()
    elif choice == 2:
        viewcontacts()
    elif choice == 3:
        updatecontacts()
    elif choice == 4:
        deletecontacts()
    elif choice == 5:
        searchcontacts()
    elif choice == 6:
        totalcontacts()
    elif choice == 7:
        exitingcontacts()
    else:
        print("Invalid choice")