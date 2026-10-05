# Contact Management System

contacts = []


# Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("\nContact added successfully!")


# View Contacts
def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n----- Contact List -----")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")


# Search Contact
def search_contact():
    search = input("Enter name or phone number to search: ").lower()

    found = False

    for contact in contacts:
        if (search in contact["name"].lower() or
                search in contact["phone"]):

            print("\nContact Found:")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])
            found = True

    if not found:
        print("\nContact not found.")


# Update Contact
def update_contact():
    name = input("Enter name of contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            contact["name"] = input("Enter new name: ")
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address: ")

            print("\nContact updated successfully!")
            return

    print("\nContact not found.")


# Delete Contact
def delete_contact():
    name = input("Enter name of contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("\nContact deleted successfully!")
            return

    print("\nContact not found.")


# Main Menu
while True:
    print("\n========== CONTACT MANAGEMENT SYSTEM ==========")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Management System!")
        break

    else:
        print("Invalid choice! Please try again.")