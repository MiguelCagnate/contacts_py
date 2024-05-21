import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from contact import Contact, ContactBook

class ContactBookApp:
    def __init__(self, root):
        self.contact_book = ContactBook()

        self.root = root
        self.root.title("Contact Book")

        # Main frame
        main_frame = ttk.Frame(root, padding="10 10 10 10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Add Contact Frame
        add_frame = ttk.LabelFrame(main_frame, text="Add Contact", padding="10 10 10 10")
        add_frame.grid(column=0, row=0, padx=10, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(add_frame, text="Name").grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        self.name_entry = ttk.Entry(add_frame)
        self.name_entry.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(add_frame, text="Phone").grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        self.phone_entry = ttk.Entry(add_frame)
        self.phone_entry.grid(column=1, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(add_frame, text="Email").grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
        self.email_entry = ttk.Entry(add_frame)
        self.email_entry.grid(column=1, row=2, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(add_frame, text="Nationality").grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
        self.nationality_entry = ttk.Entry(add_frame)
        self.nationality_entry.grid(column=1, row=3, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(add_frame, text="Add Contact", command=self.add_contact).grid(column=0, row=4, columnspan=2, pady=5)

        # Action Buttons Frame
        actions_frame = ttk.Frame(main_frame, padding="10 10 10 10")
        actions_frame.grid(column=0, row=1, padx=10, pady=10, sticky=(tk.W, tk.E))

        ttk.Button(actions_frame, text="Find Contact", command=self.find_contact).grid(column=0, row=0, padx=5, pady=5)
        ttk.Button(actions_frame, text="Remove Contact", command=self.remove_contact).grid(column=1, row=0, padx=5, pady=5)
        ttk.Button(actions_frame, text="List Contacts", command=self.list_contacts).grid(column=2, row=0, padx=5, pady=5)

        # Output Frame
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding="10 10 10 10")
        output_frame.grid(column=0, row=2, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.output_text = ScrolledText(output_frame, height=10, wrap=tk.WORD)
        self.output_text.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure column/row weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        add_frame.columnconfigure(1, weight=1)
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        nationality = self.nationality_entry.get()
        if name and phone and email and nationality:
            contact = Contact(name, phone, email, nationality)
            result = self.contact_book.add_contact(contact)
            self.output_text.insert(tk.END, result + "\n")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.nationality_entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Warning", "All fields must be filled!")

    def find_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to find:")
        if name:
            contact = self.contact_book.find_contact(name)
            if contact:
                self.output_text.insert(tk.END, f"Found contact: {contact}\n")
            else:
                self.output_text.insert(tk.END, f"No contact found with name: {name}\n")
        else:
            messagebox.showwarning("Warning", "Name field must be filled!")

    def remove_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to remove:")
        if name:
            result = self.contact_book.remove_contact(name)
            self.output_text.insert(tk.END, result + "\n")
        else:
            messagebox.showwarning("Warning", "Name field must be filled!")

    def list_contacts(self):
        result = self.contact_book.list_contacts()
        self.output_text.insert(tk.END, result + "\n")