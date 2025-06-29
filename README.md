# 🍨 Ice Cream Delight Website

## 📝 Description
**Ice Cream Delight** is a user-friendly web application built using **Flask** and **MySQL** that allows customers to register, log in, and manage their details. It is designed for an ice cream shop or similar setting where customers’ contact and feedback data are stored securely and can be updated or removed by the admin. The project includes user and admin login, real-time data fetching, and HTML table display using Pandas.

---

## 🚀 Features
- User Registration & Login
- Admin Login with access to all data
- Insert, Update, Delete Customer Records
- Data display using styled HTML tables
- Secure login validation with MySQL backend
- Form handling using Flask routes
- Responsive templates using Bootstrap

---

## 🧱 Technologies Used
- **Frontend**: HTML, CSS (Bootstrap)
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Library**: Pandas

---

## 🗂️ Folder Structure

IceCreamDelight/
│
├── static/ # Static assets like CSS/images
├── templates/ # HTML templates
│ ├── user_login.html
│ ├── admin_login.html
│ ├── registration.html
│ ├── index.html
│ └── frame-18.html
│
├── app.py # Main Flask application
└── README.md # Project documentation

---

## 🛠️ How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ice-cream-delight.git
   cd ice-cream-delight

2. **Install dependencies:**
   ```bash
   pip install flask mysql-connector-python pandas

3. **Setup your MySQL database using database.txt file:**

4. **Update DB credentials in app.py according to you:**

5. **Run the Flask app:**
   ```bash
   python app.py

6. **Open in browser:**
   ```bash
   [python app.py](http://127.0.0.1:5000/)

💡 Notes
- Admin login checks credentials from admindata table.
- Pandas is used for fetching and converting MySQL data to HTML table format.
- All data is securely stored and modified using SQL queries inside Flask routes.
































