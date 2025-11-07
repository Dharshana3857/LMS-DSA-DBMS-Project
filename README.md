# 📚 Library Management System (DSA + DBMS Project)

## 🧩 Overview

This project is a **Library Management System** built using a combination of **Data Structures and Algorithms (DSA)** and **Database Management System (DBMS)** concepts.
It provides an efficient way to manage books, users, and transactions in a digital library environment — integrating algorithmic efficiency with persistent database storage.

Additionally, the system is connected to **Gmail** to automatically send **email reminders** for due or overdue books to specific users.

---

## ⚙️ Features

* 🔍 **Book Management** — Add, search, issue, and return books using efficient data structures.
* 👥 **User Management** — Store and track user details in a database.
* 💾 **Database Integration (DBMS)** — Persistent storage using SQL tables for books, users, and transactions.
* 📬 **Email Alerts via Gmail** — Sends due-date reminder emails automatically using the Gmail SMTP service or API.
* 🔄 **Transaction Handling** — Keeps records of book issues and returns.
* 🧠 **Use of DSA Concepts** —

  * Linked Lists for user/book queues
  * Trees or Hash Tables for quick book lookup
  * Queues for managing issue requests

---

## 🏗️ Technologies Used

* **Programming Language:** Python / C++ / Java *(choose based on your implementation)*
* **Database:** MySQL / SQLite
* **Email Integration:** Gmail API / SMTP Library
* **Data Structures:** Linked Lists, Trees, Hash Tables, Queues

---

## 🧮 Database Schema (Example)

**Tables:**

* `books(book_id, title, author, available_copies)`
* `users(user_id, name, email)`
* `transactions(trans_id, user_id, book_id, issue_date, due_date, return_date)`

---

## 📧 Email Notification Feature

* Uses Gmail’s SMTP or API to send due-date reminders automatically.
* Sends personalized email to each user with pending returns.
* Example subject:

  ```
  Reminder: Your library book is due soon!
  ```

---



## 🧑‍💻 Future Enhancements

* Web-based user interface
* Admin dashboard for analytics
* Integration with cloud-based databases
* SMS reminders in addition to email

---

## 🪪 Author

**Developed by:** *Dharshana*
**Project Type:** DSA + DBMS Integration
**Email Notifications:** Enabled via Gmail

---

⭐ *If you like this project, don’t forget to star the repo!*
