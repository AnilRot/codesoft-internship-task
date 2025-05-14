import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file or return empty dictionary"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to JSON file"""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def display_contact(contact):
    """Display a single contact's details"""
    print("\nContact Details:")
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")

def add_contact(contacts):
    """Add a new contact to the system"""
    print("\nAdd New Contact")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!")

def view_contacts(contacts):
    """Display all contacts in the system"""
    print("\nContact List:")
    if not contacts:
        print("No contacts found.")
        return
    
    print(f"{'Name':<20}{'Phone':<15}")
    print("-" * 35)
    for name, details in contacts.items():
        print(f"{name:<20}{details['phone']:<15}")

def search_contact(contacts):
    """Search for contacts by name or phone number"""
    search_term = input("\nEnter name or phone number to search: ").strip().lower()
    results = []
    
    for name, details in contacts.items():
        if (search_term in name.lower()) or (search_term in details['phone']):
            results.append((name, details))
    
    if not results:
        print("No matching contacts found.")
        return
    
    print(f"\nFound {len(results)} matching contact(s):")
    for name, details in results:
        print(f"\n{name}:")
        print(f"  Phone: {details['phone']}")
        print(f"  Email: {details['email']}")
        print(f"  Address: {details['address']}")

def update_contact(contacts):
    """Update an existing contact's details"""
    name = input("\nEnter name of contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    
    display_contact({'name': name, **contacts[name]})
    
    print("\nEnter new details (leave blank to keep current):")
    phone = input(f"New phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"New email [{contacts[name]['email']}]: ").strip()
    address = input(f"New address [{contacts[name]['address']}]: ").strip()
    
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    
    save_contacts(contacts)
    print("\nContact updated successfully!")

def delete_contact(contacts):
    """Delete a contact from the system"""
    name = input("\nEnter name of contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    
    display_contact({'name': name, **contacts[name]})
    confirm = input("\nAre you sure you want to delete this contact? (y/n): ").lower()
    
    if confirm == 'y':
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Deletion canceled.")

def main_menu():
    """Display the main menu and handle user input"""
    contacts = load_contacts()
    
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add New Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nThank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main_menu()