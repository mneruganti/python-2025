import json
import os

class contact_book:
    
    # storing the contacts from a json file
    def __init__(self, storage_file='contacts.json'):
        self.storage_file = storage_file
        self.contacts = [] # make a list instance to update with contacts
        self.load_contacts() # populate the list with pre-existing contacts
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()
    
    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        self.save_contacts()
    
    def edit_contacts(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[i] = new_contact
                self.save_contacts()
                return True
        return False
    
    
        