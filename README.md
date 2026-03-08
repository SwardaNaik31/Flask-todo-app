# 📝 Flask Todo App

A simple **Todo List Web Application** built using **Flask, MySQL, and Bootstrap**.  
This application allows users to manage their daily tasks by performing basic **CRUD operations** (Create, Read, Update, Delete).

---

## 🚀 Features

- ➕ Add new todos
- 📋 View all todos
- ✏️ Update existing todos
- ❌ Delete todos
- 🗄️ MySQL database integration
- 🎨 Responsive UI using Bootstrap

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **MySQL**
- **HTML**
- **Bootstrap**

---

## 📂 Project Structure
Flask-todo-app
│
├── app.py
├── templates
│ ├── index.html
│ └── update.html
├── requirements.txt
└── README.md

---

##⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/SwardaNaik31/Flask-todo-app.git
2️⃣ Navigate to the project folder
cd Flask-todo-app
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
python app.py
5️⃣ Open in your browser
http://127.0.0.1:5000
🗄️ Database Setup

Make sure MySQL is running, then create a database:

CREATE DATABASE todo_db;

Update the database connection in app.py if needed:

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@localhost/todo_db"

---


👨‍💻 Author

Swarda Naik

GitHub:
👉 https://github.com/SwardaNaik31
