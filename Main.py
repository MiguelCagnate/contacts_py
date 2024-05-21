import tkinter as tk
from tkinter import ttk,messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from contact_book_app import Contact, ContactBook,ContactBookApp


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
