import json
import os
from contact import contact

class contact_book:
    
    # storing the contacts from a json file
    def __init__(self, storage_file='contacts.json'):
        self.storage_file = storage_file
        self.contacts = [] # make a list instance to update with contacts
        self.load_contacts() # populate the list with pre-existing contacts
    
    # append contact to the end of the list
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()
    
    # rewrite self.contacts to have every contact except the one with the matching name
    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        self.save_contacts()
    
    # edit the contact by finding the same name and assigning the new contact
    # to the contact at the specific position
    def edit_contacts(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[i] = new_contact
                self.save_contacts()
                return True
        return False
    
    # search for a contact given a name (if the name is found in the contact)
    def search_contact(self, name):
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                return contact
        return None
    
    # return the list of contacts
    def list_contacts(self):
        return self.contacts
    
    # The save contacts method writes the information to a file defined in storage_file
    # json.dump() serializes a python object to a JSON string and writes it to the file in JSON format
    def save_contacts(self):
        with open(self.storage_file, 'w') as file:
            json.dump([c.to_dict() for c in self.contacts], file)
    
    # If the file does not exist on the device, break out of the method
    # Otherwise, open the file for reading, load it into contacts_data, and assign self.contacts to
    # the new data using the from_dict method from the contact class       
    def load_contacts(self):
        if not os.path.exists(self.storage_file):
            return
        with open(self.storage_file, 'r') as file:
            contacts_data = json.load(file)
            self.contacts = [contact.from_dict(data) for data in contacts_data]