import re

def add_contact(contacts): # "Working" Needs tweaking ((Works technically)printing issue)
    contact_name = input("Please enter new contact name: ")
    contact_phone_number = input("Please enter contact's phone number with dashes: ")
    contact_email = input("Please enter the contact's email address: ")
    for contact in contacts.values():
         if (contact["Name"] == contact_name and 
            contact["Phone Number"] == contact_phone_number and
            contact["E-Mail Address"] == contact_email):
            print("Contact with the same name, phone number, and email already exists! ")
    new_contact = {
        "Name": contact_name,
        "Phone Number": contact_phone_number,
        "E-Mail Address": contact_email
        }
    contacts[contact_name] = new_contact
    print(f"Contact {contact_name} was added successfully")

def edit_contact(contacts): # "Working" Needs tweaking (Keeps the old phone number)
    contact_name = input("Whose contact info would you like to change? ")
    if contact_name in contacts:
        contact_phone_number = input("Please enter the new phone number: ")
        contacts[contact_name]["Phone Number: "] = contact_phone_number
        print(f"Phone number has been updated to {contact_phone_number}. ")
   
def delete_contact(contacts): #Works Great
    contact_name = input("Who's contact info would you like to remove? ")
    if contact_name in contacts:
        contacts.pop(contact_name)
        print(f"{contact_name} has been removed. ")
    else:
        print("Please enter a valid contact... ")

def search_contact(contacts): # Doesn't Work
    contact_name = input("Whose contact info are you searching for? ")
    # if contact_name in contacts:
    #     for key in contact_name.keys():
    #         print(contact_name)
    
def display_contacts(contacts):# Works Great 
    for contact_name, details in contacts.items():
        print("Contact Details: ")
        for key, value in details.items():
            print(f" - {key}: {value}")
        print()
    
def export_contact(contacts): # Works perfect somehow
    file = open("new_contact_info_dict.txt", "w+")
    with open("new_contact_info_dict.txt", "w") as file:
        for contact_name, new_contact in contacts.items():
            file.write(f"{contact_name}: {new_contact}\n")
    print("Contacts have been exported, changes have been saved! ")
        
def import_contact(contacts): # Doesn't Work
    pass
    # with open("old_contact_info.txt", "r") as file:
    #     for line in file:
    #         contact_name, new_contact = line.strip().split(": ")
    #         contacts[contact_name] = new_contact
    # print("Contacts have been imported? Restore Success?")

contacts = {}

def main(contacts):
    print("""
          Welcome to the Contact Management System...

          Menu:
         1. Add a new contact
         2. Edit an existing contact
         3. Delete a contact
         4. Search for a contact
         5. Display all contacts
         6. Export contacts to a text file
         7. Import contacts from a text file
         8. Quit
          
          """)
    while True:
        response = input("Please choose from the menu above: ")
        if response == "1":
            add_contact(contacts)
        elif response == "2":
            edit_contact(contacts)
        elif response == "3":
            delete_contact(contacts)
        elif response == "4":
            search_contact(contacts)
        elif response == "5":
            display_contacts(contacts)
        elif response == "6":
            export_contact(contacts)
        elif response == "7":
            import_contact(contacts)
        elif response == "8":
            print("Exiting Program... ")
            break
        else:
            print("Please enter a valid response... ")
    
main(contacts)

