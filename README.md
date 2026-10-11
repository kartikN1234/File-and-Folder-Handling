# 📁 File and Folder Handling System Using Python

## 📌 Project Overview

The **File and Folder Handling System** is a menu-driven Python application that allows users to perform basic file and folder management operations through a command-line interface.

The project demonstrates Python's file handling capabilities and the use of built-in modules such as `pathlib`, `shutil`, and `os` to manage files and directories efficiently.

Users can create, read, rename, update, and delete files and folders by selecting options from an interactive menu.

## ✨ Features

### 📂 Folder Operations
- **Create Folder:** Create a new directory with a user-defined name.
- **Read Files and Folders:** Display files and directories within the current working directory and its subdirectories.
- **Rename Folder:** Change the name of an existing directory.
- **Delete Folder:** Delete a directory, including its contents.

### File Operations
- **Create File:** Create a new file and write user-provided content.
- **Read File:** Read and display the contents of an existing file.
- **Update File:** Perform the following operations:
  - Rename an existing file.
  - Append new content to a file.
  - Overwrite the existing file content.
- **Delete File:** Delete an existing file.

### 🛠️ Additional Features
- Interactive, menu-driven command-line interface.
- Basic error handling using `try-except` blocks.
- Checks for file and folder existence before performing operations.
- Uses Python's built-in modules for filesystem management.

## 🧰 Technologies Used

- **Programming Language:** Python
- **Modules:**
  - `pathlib` — For handling file and directory paths.
  - `shutil` — For deleting directories and their contents.
  - `os` — Imported for operating-system-related functionality.

## 📂 Project Structure

```text
File-and-Folder-Handling/
│
├── main.py          # Main Python application
└── README.md         # Guide
```

*Note: The files and folders shown above are included in the current project structure. Additional files and directories may be created while using the application.*

## ⚙️ Prerequisites

- Python 3.8 or later recommended.
- A terminal, command prompt, or code editor such as Visual Studio Code.

**No external Python packages are required.** The project uses Python's standard library.

## 🚀 Installation and Setup

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/kartikN1234/File-and-Folder-Handling.git
```


### 2. Navigate to the Project Directory

```bash
cd File-and-Folder-Handling
```

### 3. Run the Application

```bash
python main.py
```

If the `python` command is not recognized on your system, try:

```bash
py main.py
```

## 💻 How to Use

After starting the application, an interactive menu appears:

```text
Options : -

1. Create a folder
2. Read files and folder
3. Update the folder
4. Delete the folder
5. Create a file
6. Read a file
7. Update the file
8. Delete the file
Press 0 to exit
```

### Example Workflow

# Run the Python program.
  1. Create a folder
  2. Read files and folder
  3. Update the folder
  4. Delete the folder
  5. Create a file
  6. Read a file
  7. Update the file
  8. Delete the file
  0. Press 0 to exit

## 📚 Python Concepts Demonstrated

This project provides practical experience with the following Python concepts:

- File handling using `open()`.
- File modes such as `x`, `r`, `a`, and `w`.
- Working with paths using `pathlib.Path`.
- Creating directories using `mkdir()`.
- Listing directory contents using `rglob()`.
- Renaming files and directories using `rename()`.
- Deleting files using `unlink()`.
- Deleting directories recursively using `shutil.rmtree()`.
- Exception handling using `try-except`.
- Functions and modular programming.
- User input and conditional statements.
- Checking file and directory properties using `exists()`, `is_file()`, and `is_dir()`.

## 🎯 Learning Objectives

The main objectives of this project are:

- To understand how Python interacts with the filesystem.
- To implement basic CRUD operations for files and directories.
- To practice using Python's standard library.
- To understand file modes and directory management.
- To improve problem-solving skills through a practical Python project.
- To build a foundation for developing more advanced file management applications.

## ⚠️ Important Notes

- Run the application from the directory where you want to manage files and folders.
- Use valid file and directory names for your operating system.
- **Deleting a folder using this application permanently removes the folder and its contents.** Verify the folder path before confirming a deletion.
- Overwriting a file replaces its existing content.
- The current implementation uses relative paths, so file and folder operations depend on the application's current working directory.
- Avoid running the application in directories containing important system files or sensitive data.

## 🔮 Future Enhancements

Potential improvements for future versions include:

- Add a graphical user interface (GUI).
- Implement search functionality for files and folders.
- Add file copying and moving operations.
- Support selecting files and folders from a displayed numbered list.
- Improve input validation and error messages.
- Add confirmation prompts before deleting files or folders.
- Implement logging to record file and folder operations.
- Add support for file metadata, including file size and modification time.
- Introduce safer path validation to prevent accidental operations outside the intended directory.

## 👨‍💻 Author

**Kartik Nalawade**

GitHub: https://github.com/kartikN1234

---

⭐ If you find this project useful, consider giving the repository a star!