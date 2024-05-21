class Contact:
    # Initialize each contact with a name, phone number, and email.
    def __init__(self, name, phone, email):
        # Store the input parameters into instance variables
        # Your code here (3 lines)

class ContactBook:
    # Initialize the ContactBook with an empty list to hold Contact instances.
    def __init__(self):
        # Your code here (1 line)

    # Method to add a new Contact instance to the contact list.
    def add_contact(self, contact):
        # Your code here (1 line)

    # Method to find and return a Contact by their name.
    def find_contact(self, name):
        # Loop through the contacts list to find a matching contact name.
        # Return the contact if found, otherwise return None.
        # Your code here (implement loop and condition)

    # Method to remove a Contact by name.
    def remove_contact(self, name):
        # Remove a contact by name from the contact book and create a new list excluding the contact with the given name.
        # Your code here (3-5 lines)

    # Method to print all contacts in the ContactBook.
    def list_contacts(self):
        # Print the details of each contact in the contacts list.
        # Your code here (implement loop to print contact details)