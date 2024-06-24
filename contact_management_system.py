import re

def add_contact(contacts): # Works great - too much research was needed
    contact_name = input("Please enter new contact name: ")
    contact_phone_number = input("Please enter contact's phone number with dashes: ")
    contact_email = input("Please enter the contact's email address: ")
    # Always have trouble remembering I can set the parameters as I need to, sometimes error goes first,
    # then appropiate approach afterwards. 
    for contact in contacts.values():
         if (contact["Name"] == contact_name and 
            contact["Phone Number"] == contact_phone_number and
            contact["E-Mail Address"] == contact_email):
            print("Contact with the same name, phone number, and email already exists! ")
            return
    new_contact = {
        "Name": contact_name,
        "Phone Number": contact_phone_number,
        "E-Mail Address": contact_email
        }
    contacts[contact_name] = new_contact
    print(f"Contact {contact_name} was added successfully")


#-----------------------------------------------------------------------------------------------------------------


def edit_contact(contacts): #Works great - pain in my ass
    contact_name = input("Whose contact info would you like to change? ")
    try:
        if contact_name in contacts:
            new_phone_number = input("Please enter the new phone number: ")
            contacts[contact_name]["Phone Number"] = new_phone_number   # Looks for the contact in dictionary and is ready to be reassigned
            print(f"Phone number for {contact_name} has been updated to {new_phone_number}.")
        else:
            print(f"Contact '{contact_name}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")
    try:
        if contact_name in contacts:
            new_contact_email = input("Please enter the new email address: ")
            contacts[contact_name]["E-Mail Address"] = new_contact_email  # Same thing happening here, just formatted to change the email instead of phone number
            print(f"E-Mail Address for {contact_name} has been updated to {new_contact_email}.")
        else:
            print(f"Contact '{contact_name}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")


#-----------------------------------------------------------------------------------------------------------------

   
def delete_contact(contacts): # Works Great, pretty easy to destroy things, hard to build :P
    contact_name = input("Who's contact info would you like to remove? ")
    if contact_name in contacts:
        contacts.pop(contact_name)
        print(f"{contact_name} has been removed. ")
    else:
        print("Please enter a valid contact... ")


#-----------------------------------------------------------------------------------------------------------------


def search_contact(contacts): #Works flawless, thank you to Blake M. for guidance 
    search_name = input("Enter the contact to search for: ")
    found = False
    for contact_name, details in contacts.items():
        if search_name.lower() in contact_name.lower():
            found = True
            print("Contact Details:")
            for key, value in details.items():
                print(f" - {key}: {value}")
            print()
    if not found:
        print(f"Contact '{search_name}' not found.")


#-----------------------------------------------------------------------------------------------------------------


def display_contacts(contacts):# Works Great 
    for contact_name, details in contacts.items(): 
        print("Contact Details: ")
        for key, value in details.items():
            print(f" - {key}: {value}")
        print()


#-----------------------------------------------------------------------------------------------------------------
    

def export_contact(contacts): # Works great somehow
    file = open("new_contact_info_dict.txt", "w+")  # Opens an entire new file to write in
    with open("new_contact_info_dict.txt", "w") as file:  
        for contact_name, new_contact in contacts.items(): # K:V are identified then written into the .txt file
            file.write(f"{contact_name}: {new_contact}\n")
    print("Contacts have been exported, changes have been saved! ")

#-----------------------------------------------------------------------------------------------------------------
        
def import_contact(contacts): # for the sake of testing, I made two seperate files. 
                              # one with old contact info and one with new. New stuff gets put in new file
                              # and the old is is prefilled with information already ready to be put in the new system
                              # Thank you to my friend who goes by Moose 
    filename = "old_contact_info.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  # Removes the white space (\n)
            if ":" in line:
                contact_name, contact_info_str = line.split(":", 1) 
                contact_name = contact_name.strip()
                contact_info = {} # Extracting details from the string
                details = contact_info_str.strip()[1:-1].split(",")  # Remove surrounding curly braces and split by comma using slicing
                for detail in details:
                    key, value = detail.split(":")
                    contact_info[key.strip()] = value.strip().strip("'\"")
                contacts[contact_name] = {                 # Add the contact to the contacts dictionary based on appropiate K:V
                    "Name": contact_info["'Name'"],
                    "Phone Number": contact_info["'Phone Number'"],
                    "E-Mail Address": contact_info["'E-Mail Address'"]
                }
        print("Contacts have been imported successfully.")


#-----------------------------------------------------------------------------------------------------------------

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


