# 📇 Contact Book CLI Application

A simple yet powerful command-line contact management system built with Python. Organize, search, and manage your contacts efficiently with an intuitive menu-driven interface.

## ✨ Features

- **📝 Create Contacts** - Add new contacts with name and phone number validation
- **👁️ View All Contacts** - Display all saved contacts in a formatted list
- **✏️ Update Contacts** - Modify phone numbers for existing contacts
- **🗑️ Delete Contacts** - Remove contacts from your contact book
- **🔍 Search Contacts** - Find specific contacts by name
- **📊 Contact Count** - View the total number of saved contacts
- **⚡ Input Validation** - Comprehensive validation for phone numbers and contact information

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/LakshyaPandey3/RealWorldPracticeProject3.git
cd RealWorldPracticeProject3
```

2. Run the application:
```bash
python ContactBookpracticeproject-3.py
```

## 📖 Usage Guide

When you launch the application, you'll see a menu with the following options:

```
Welcome to the contact book Application
Choose an option:
1. Create a new contact
2. View all contacts
3. Update a contact
4. Delete a contact
5. Search for a contact
6. Count the total number of contacts
7. Exit
```

### 1️⃣ Create a New Contact
- Enter the contact's name
- Enter a phone number (7-12 digits)
- The application will validate and save the contact

**Validation Rules:**
- Name cannot be empty
- Phone number must contain only digits (0-9)
- Phone number must be between 7 and 12 digits long
- Duplicate contacts are not allowed

### 2️⃣ View All Contacts
Displays all saved contacts in a clean, formatted list with names and phone numbers.

### 3️⃣ Update a Contact
- Enter the name of the contact to update
- Provide the new phone number
- The contact's phone number will be updated if found

### 4️⃣ Delete a Contact
- Enter the name of the contact to delete
- The contact will be removed from your contact book

### 5️⃣ Search for a Contact
- Enter the name of the contact you're looking for
- View the contact's details if found

### 6️⃣ Count Total Contacts
View the total number of contacts currently stored in your contact book.

### 7️⃣ Exit
Safely exit the application.

## 🔍 Example Workflow

```
Welcome to the contact book Application
Choose an option:
1. Create a new contact
2. View all contacts
...
Enter your choice: 1

Enter the name: John Doe
Enter the phone number: 9876543210
Contact added successfully

Enter your choice: 2
--------Contact List--------
John Doe: 9876543210

Enter your choice: 7
Thank you for using this application
```

## 💡 Key Features Explained

### Input Validation
The application includes robust validation to ensure data integrity:
- Non-empty contact names
- Numeric phone numbers only
- Phone number length constraints
- Duplicate contact prevention

### Case-Insensitive Search
All search, update, and delete operations are case-insensitive, making it easier to find contacts regardless of how you type their names.

### User-Friendly Interface
- Clear menu options
- Helpful error messages
- Success confirmations
- Simple navigation

## 📁 Project Structure

```
RealWorldPracticeProject3/
├── ContactBookpracticeproject-3.py
└── README.md
```

## 🎯 Learning Outcomes

This project demonstrates:
- ✅ Data structures (lists and dictionaries)
- ✅ Function implementation and modular design
- ✅ Input validation and error handling
- ✅ String manipulation and comparison
- ✅ Control flow (loops, conditionals)
- ✅ User interface design for CLI applications

## 🔧 Technical Details

- **Language:** Python 3
- **Type:** Command-Line Interface (CLI)
- **Data Storage:** In-memory (contacts stored during session)
- **No External Dependencies:** Pure Python implementation

## 📝 Note

The contacts are stored in memory during the application session. When you exit the application, the contact data will be lost. For persistent storage, consider implementing file I/O (JSON or CSV) in future versions.

## 🚀 Future Enhancements

Potential improvements for this project:
- 💾 File persistence (save contacts to JSON/CSV)
- 📧 Email field support
- 🏷️ Contact categories/groups
- 📍 Address field
- 🌐 Database integration
- 🔐 Data encryption
- 📤 Import/Export functionality

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Lakshya Pandey**

---

**Happy Contact Managing! 📇