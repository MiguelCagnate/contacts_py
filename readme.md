# ContactBookApp

ContactBookApp is a simple contact management application built using Python and `tkinter` for the graphical user interface. The app allows users to add, find, remove, and list contacts.

## Table of Contents
- [ContactBookApp](#contactbookapp)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Code Structure](#code-structure)
    - [Explanation:](#explanation)
    - [Example](#example)
- [main.py](#mainpy)

## Features
- **Add Contact**: Add a new contact with name, phone number, and email.
- **Find Contact**: Find a contact by name.
- **Remove Contact**: Remove a contact by name.
- **List Contacts**: List all saved contacts.

## Installation

### Prerequisites
- Python 3.x
- `tkinter` (usually included with Python installations)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ContactBookApp.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ContactBookApp
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```
2. Use the GUI to interact with the contact book:
   - **Add Contact**: Enter the contact details and click "Add Contact".
   - **Find Contact**: Click "Find Contact" and enter the name of the contact to find.
   - **Remove Contact**: Click "Remove Contact" and enter the name of the contact to remove.
   - **List Contacts**: Click "List Contacts" to display all contacts.

## Code Structure
- `contact.py`: Contains the `Contact` and `ContactBook` classes which handle the core functionality of managing contacts.
- `contact_book_app.py`: Contains the `ContactBookApp` class which handles the GUI using `tkinter`.
- `main.py`: The main script that initializes and runs the application.

### Explanation:
- **Features**: Lists the main functionalities of the app.
- **Installation**: Provides steps to install and set up the project.
- **Usage**: Explains how to run the application and use its features.
- **Code Structure**: Briefly describes the purpose of each module.
- **Contributing**: Encourages contributions and outlines the steps to contribute.
- **License**: Specifies the project's license.


### Example

```python
# main.py
import tkinter as tk
from contact_book_app import ContactBookApp



if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

