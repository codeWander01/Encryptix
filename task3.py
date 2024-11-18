import tkinter as tk                # Import tkinter for the graphical interface
from tkinter import messagebox       # Import messagebox for showing pop-up messages
import json                          # Import json to save and load contacts from a file

# Main Contact Book Application Class
class ContactBookApp:
    def __init__(self, master):      # Initialize the app
        self.master = master
        self.master.title("Contact Book")  # Set window title
        self.master.geometry("400x500")    # Set window size

        # Load contacts from a JSON file or create an empty contact list if file doesn't exist
        self.contacts = self.load_contacts()
        
        # Create the user interface
        self.create_widgets()

    # Load contacts from a file
    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                return json.load(file)     # Load and return contact data
        except FileNotFoundError:
            return {}                      # Return an empty dictionary if file doesn't exist

    # Save contacts to a file
    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file) # Save contacts to file

    # Set up the UI elements (text fields, buttons, etc.)
    def create_widgets(self):
        # Create text fields for entering contact details
        tk.Label(self.master, text="Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.master, width=30)
        self.name_entry.pack()

        tk.Label(self.master, text="Phone Number:").pack(pady=5)
        self.phone_entry = tk.Entry(self.master, width=30)
        self.phone_entry.pack()

        tk.Label(self.master, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.master, width=30)
        self.email_entry.pack()

        tk.Label(self.master, text="Address:").pack(pady=5)
        self.address_entry = tk.Entry(self.master, width=30)
        self.address_entry.pack()

        # Create buttons for different actions
        tk.Button(self.master, text="Add Contact", command=self.add_contact, bg="lightblue").pack(pady=10)
        tk.Button(self.master, text="View Contacts", command=self.view_contacts, bg="lightgreen").pack(pady=5)
        tk.Button(self.master, text="Search Contact", command=self.search_contact, bg="lightyellow").pack(pady=5)
        tk.Button(self.master, text="Update Contact", command=self.update_contact, bg="lightcoral").pack(pady=5)
        tk.Button(self.master, text="Delete Contact", command=self.delete_contact, bg="lightpink").pack(pady=5)

    # Function to add a new contact
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:   # Check that name and phone number are not empty
            self.contacts[phone] = {       # Add contact to the dictionary using phone number as key
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            self.save_contacts()           # Save updated contact list to file
            messagebox.showinfo("Success", "Contact added!")
            self.clear_entries()            # Clear the text fields after adding
        else:
            messagebox.showwarning("Error", "Name and Phone Number are required!")

    # Function to view all contacts
    def view_contacts(self):
        if not self.contacts:    # Check if contact list is empty
            messagebox.showinfo("Contact List", "No contacts to display.")
            return

        contact_list = ""
        for phone, info in self.contacts.items():
            contact_list += f"{info['name']} - {phone}\n"    # Display name and phone
        messagebox.showinfo("Contact List", contact_list)

    # Function to search for a contact
    def search_contact(self):
        search_query = self.name_entry.get() or self.phone_entry.get()
        
        if not search_query:
            messagebox.showwarning("Error", "Enter a name or phone number to search.")
            return

        found = False
        for phone, info in self.contacts.items():
            if search_query.lower() in info["name"].lower() or search_query == phone:
                result = f"Name: {info['name']}\nPhone: {phone}\nEmail: {info['email']}\nAddress: {info['address']}"
                messagebox.showinfo("Contact Found", result)
                found = True
                break

        if not found:
            messagebox.showinfo("Search Results", "No contact found.")

    # Function to update an existing contact
    def update_contact(self):
        phone = self.phone_entry.get()
        if phone in self.contacts:
            self.contacts[phone] = {
                "name": self.name_entry.get(),
                "phone": phone,
                "email": self.email_entry.get(),
                "address": self.address_entry.get()
            }
            self.save_contacts()
            messagebox.showinfo("Success", "Contact updated!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Contact not found.")

    # Function to delete a contact
    def delete_contact(self):
        phone = self.phone_entry.get()
        if phone in self.contacts:
            del self.contacts[phone]
            self.save_contacts()
            messagebox.showinfo("Success", "Contact deleted!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Contact not found.")

    # Clear all text fields
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Run the application
root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()
