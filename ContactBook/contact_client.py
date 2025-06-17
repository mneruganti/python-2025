from contact_book import contact_book
from contact import contact as Contact

class contact_client:
    
    def __init__(self):
        self.contact_book = contact_book()
        self.commands = {
            'add': self.add_contact,
            'delete': self.delete_contact,
            'edit': self.edit_contact,
            'search': self.search_contact,
            'list': self.list_contacts,
            'help': self.show_help,
            'exit': self.exit
        }
    
    def run(self):
        print("Welcome to the Contact Book CLI!")
        print("Type 'help' to see available commands.\n")
        
        while True:
            command = input("> ").strip().lower()
            if command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Type 'help' for available commands.")
    
    def add_contact(self):
        print("\nAdd a new contact")
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        relationship = input("Relationship (optional): ").strip() or None
        
        if name and phone:
            contact = Contact(name, phone, relationship)
            self.contact_book.add_contact(contact)
            print("Contact added successfully!")
        else:
            print("Name and phone are required fields.")
        print()
    
    def delete_contact(self):
        name = input("\nEnter name of contact to delete: ").strip()
        if name:
            self.contact_book.delete_contact(name)
            print("Contact deleted successfully!")
        else:
            print("Please enter a name.")
        print()
    
    def edit_contact(self):
        name = input("\nEnter name of contact to edit: ").strip()
        contact = self.contact_book.search_contact(name)
        
        if not contact:
            print("Contact not found.")
            return
        
        print("\nCurrent contact details:")
        print(contact)
        
        print("\nEnter new details (leave blank to keep current value):")
        new_name = input(f"Name [{contact.name}]: ").strip() or contact.name
        new_phone = input(f"Phone [{contact.phone}]: ").strip() or contact.phone
        new_relationship = input(f"Relationship [{contact.relationship}]: ").strip() or contact.relationship
        
        new_contact = Contact(new_name, new_phone, new_relationship)
        if self.contact_book.edit_contacts(name, new_contact):
            print("Contact updated successfully!")
        else:
            print("Failed to update contact.")
        print()
    
    def search_contact(self):
        name = input("\nEnter name to search: ").strip()
        contact = self.contact_book.search_contact(name)
        
        if contact:
            print("\nContact found:")
            print(contact)
        else:
            print("Contact not found.")
        print()
    
    def list_contacts(self):
        contacts = self.contact_book.list_contacts()
        if not contacts:
            print("\nNo contacts found.")
        else:
            print("\nAll Contacts:")
            for i, contact in enumerate(contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")
        print()
    
    def show_help(self):
        print("\nAvailable commands:")
        print("  add     - Add a new contact")
        print("  delete  - Delete a contact")
        print("  edit    - Edit a contact")
        print("  search  - Search for a contact")
        print("  list    - List all contacts")
        print("  help    - Show this help message")
        print("  exit    - Exit the program\n")
    
    def exit(self):
        print("Goodbye!")
        exit()