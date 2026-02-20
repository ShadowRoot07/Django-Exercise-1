# 📋 Django Task Manager (ShadowRoot07)

A task management application built with Django, focused on solid software architecture, secure authentication, and well-structured relational data handling.

---

## 🚀 Project Overview

This project is a backend-driven tool for managing daily tasks, supporting categorization, priority levels, and access control.

The primary goal was to implement a scalable architecture following Django’s MTV (Model–Template–View) pattern while integrating production-level features and best practices.

---

## 🛠️ Tech Stack

- **Language:** Python 3.12  
- **Framework:** Django (Auth, ORM, CBVs, Signals)  
- **Database:** PostgreSQL  
- **Environment:** Termux (Linux environment)  
- **Version Control:** Git & GitHub  

---

## 🏗️ Architecture Structure

The project follows a modular structure designed for maintainability and scalability:

```txt
├── core/               # Central configuration (settings, global urls) ├── tasks/              # Main application │   ├── signals.py      # Event-driven logic (authentication hooks) │   ├── models.py       # Data models (Category, Task) │   ├── views.py        # Class-Based Views (CBV) │   └── forms.py        # Form validation and handling └── manage.py           # Django management entry point
```

---

## ✨ Key Features

- **Task Management (CRUD):** Create, read, update, and delete tasks  
- **Authentication System:** Route protection using `@login_required` and session management  
- **Relational Database Design:** Uses `ForeignKey` relationships to organize tasks by custom categories  
- **User Feedback:** Integrated Django Messages Framework for user notifications  
- **Event-Driven Logic:** Signals trigger automatic processes on new user registration  
- **View Architecture:** Migration from function-based views to Class-Based Views (CBVs) for improved scalability and maintainability  

---

## ⚙️ Setup & Installation

To run this project locally (Termux or standard Linux environment):

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies
Bash

```bash
pip install -r requirements.txt
```
3. Apply database migrations
Bash

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run the development server
Bash

```bash
python manage.py runserver
```

📌 Notes

Make sure PostgreSQL is properly configured in your Django settings.
Update the repository URL with your actual GitHub project path.
