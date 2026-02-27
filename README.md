## 🎓 Student Management System

A professional **Student Management System** built using **Python, Flask, OOP, File Handling (JSON), HTML, and CSS**.

This web application allows users to **Add, Update, Delete, and View student records** with persistent storage using a JSON file.

## 🚀 Features

* ➕ Add new students
* ✏️ Update existing student details
* 🗑️ Delete student records
* 📋 View all students in table format
* ✅ Unique Student ID validation
* 💾 Data persistence using JSON
* 🎨 Responsive and clean UI design
* 🧠 Object-Oriented Programming (OOP) architecture

## 🏗️ Project Structure

Student_Management_System/
│
├── app.py
├── student.py
├── manager.py
├── students.json
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── .gitignore
└── README.md

## 🛠️ Technologies Used

* Python 3.10+
* Flask
* HTML5
* CSS3
* JSON (Data Storage)
* Object-Oriented Programming (OOP)

## 📌 System Architecture

### 1️⃣ Student Class (`student.py`)

* Represents a student object.
* Uses constructor to initialize student attributes.
* Converts student object into dictionary format for JSON storage.

### 2️⃣ Student Manager (`manager.py`)

Handles all core operations:

* Add student
* Update student
* Delete student
* Retrieve all students
* Validates unique Student ID
* Saves and loads data from JSON file

### 3️⃣ Flask Application (`app.py`)

* Connects backend logic with frontend
* Defines routes:

  * `/` → Home page
  * `/add` → Add new student
  * `/update` → Update student
  * `/delete/<id>` → Delete student

## ⚙️ Installation & Setup Guide

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

### 🔹 Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### 🔹 Step 3: Activate Virtual Environment

**Windows:**

```bash
.\venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 🔹 Step 4: Install Dependencies

```bash
pip install flask
```

### 🔹 Step 5: Run the Application

```bash
python app.py
```

Now open your browser and go to:

```
http://127.0.0.1:5000/
```

## 📊 Functional Highlights

✔ CRUD Operations (Create, Read, Update, Delete)
✔ OOP-Based Structure
✔ JSON File Handling
✔ Unique ID Validation
✔ Backend–Frontend Integration
✔ Clean Folder Organization

## 🎯 Learning Outcomes

This project demonstrates:

* Strong understanding of Object-Oriented Programming
* File handling using JSON
* Web development using Flask
* HTML & CSS integration
* REST-style routing
* Real-world CRUD system implementation
* Practical backend development skills

## 🧠 Future Improvements

* Add search functionality
* Implement login authentication
* Connect with SQLite database
* Deploy on Render / Railway / Heroku
* Add pagination
* Add form validation using Flask-WTF

## 🏆 Project Value

This project showcases:

* Clean coding practices
* Structured backend architecture
* Practical web development skills
* File-based data persistence
* Problem-solving ability
* Git & GitHub workflow

## 📄 .gitignore File

Create a `.gitignore` file and add:

```
venv/
__pycache__/
students.json
```

## 👩‍💻 Author

**Khadija Farooq**
BS Computer Engineering Student
Student Management System – Internship Project

## 📜 License

This project is created for educational and internship purposes.

⭐ If you found this project useful, don’t forget to give it a star on GitHub!
