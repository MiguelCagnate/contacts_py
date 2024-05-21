class Contact:
    def __init__(self, name, phone, email, nationality):
        self.name = name
        self.phone = phone
        self.email = email
        self.nationality = nationality

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email}, {self.nationality}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        return f"Added contact: {contact}"

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name):
        new_contacts = [contact for contact in self.contacts if contact.name != name]
        if len(new_contacts) < len(self.contacts):
            self.contacts = new_contacts
            return f"Removed contact with name: {name}"
        else:
            return f"No contact found with name: {name}"

    def list_contacts(self):
        if not self.contacts:
            return "No contacts in the list."
        return "\n".join(str(contact) for contact in self.contacts)