from transactions import issue_book, return_book
from db import get_connection

# ================== BOOK FUNCTIONS ==================
def view_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT isbn, title, author, available_copies FROM books")
    books = cursor.fetchall()
    print("\n=== Books in Library ===")
    if not books:
        print("No books found.")
    for book in books:
        print(f"ISBN: {book[0]} | Title: {book[1]} | Author: {book[2]} | Available: {book[3]}")
    cursor.close()
    conn.close()

def add_book():
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    publisher = input("Enter Publisher: ")
    year = int(input("Enter Year: "))
    total_copies = int(input("Enter Total Copies: "))
    category = input("Enter Category: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (isbn, title, author, publisher, year, total_copies, available_copies, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (isbn, title, author, publisher, year, total_copies, total_copies, category))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Book added successfully!")

def view_borrowed_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT br.id, u.name, b.title, br.issue_date, br.due_date
        FROM borrow_records br
        JOIN users u ON br.user_id = u.user_id
        JOIN books b ON br.isbn = b.isbn
        WHERE br.return_date IS NULL
    """)
    records = cursor.fetchall()
    print("\n=== Active Borrowed Books ===")
    if not records:
        print("No active borrowings.")
    else:
        for rec in records:
            print(f"BorrowID: {rec[0]} | User: {rec[1]} | Book: {rec[2]} | Issued: {rec[3]} | Due: {rec[4]}")
    cursor.close()
    conn.close()

# ================== USER FUNCTIONS ==================
def view_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, email, phone, max_books FROM users")
    users = cursor.fetchall()
    print("\n=== Registered Users ===")
    if not users:
        print("No users found.")
    for user in users:
        print(f"UserID: {user[0]} | Name: {user[1]} | Email: {user[2]} | Phone: {user[3]} | Max Books: {user[4]}")
    cursor.close()
    conn.close()

def add_user():
    user_id = input("Enter User ID (e.g., U206): ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    max_books = int(input("Enter Max Books Allowed: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (user_id, name, email, phone, max_books)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, name, email, phone, max_books))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ User added successfully!")

# ================== REPORTS ==================
def top_borrowed_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.title, COUNT(*) as borrow_count
        FROM borrow_records br
        JOIN books b ON br.isbn = b.isbn
        GROUP BY b.title
        ORDER BY borrow_count DESC
        LIMIT 5
    """)
    rows = cursor.fetchall()
    print("\n=== Top 5 Borrowed Books ===")
    if not rows:
        print("No borrow records found.")
    else:
        for row in rows:
            print(f"{row[0]} | Borrowed {row[1]} times")
    cursor.close()
    conn.close()

def active_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.name, COUNT(*) as books_borrowed
        FROM borrow_records br
        JOIN users u ON br.user_id = u.user_id
        GROUP BY u.user_id
        ORDER BY books_borrowed DESC
        LIMIT 5
    """)
    rows = cursor.fetchall()
    print("\n=== Top Active Users ===")
    if not rows:
        print("No borrow records found.")
    else:
        for row in rows:
            print(f"{row[0]} | Borrowed {row[1]} books")
    cursor.close()
    conn.close()

def low_stock_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, available_copies 
        FROM books 
        WHERE available_copies < 2
    """)
    rows = cursor.fetchall()
    print("\n=== Low Stock Books (<2 copies) ===")
    if not rows:
        print("All books sufficiently available.")
    else:
        for row in rows:
            print(f"{row[0]} | Available: {row[1]}")
    cursor.close()
    conn.close()

def users_with_fines():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.name, SUM(br.fine) as total_fine
        FROM borrow_records br
        JOIN users u ON br.user_id = u.user_id
        WHERE br.fine > 0
        GROUP BY u.user_id
    """)
    rows = cursor.fetchall()
    print("\n=== Users with Pending Fines ===")
    if not rows:
        print("No users with fines.")
    else:
        for row in rows:
            print(f"{row[0]} | Fine: ₹{row[1]}")
    cursor.close()
    conn.close()

# ================== MAIN MENU ==================
def main():
    while True:
        print("\n=== Library Menu ===")
        print("1. View Books")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Borrowed Books")
        print("6. View Users")
        print("7. Add User")
        print("8. Reports")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            user_id = input("Enter User ID: ")
            isbn = input("Enter Book ISBN: ")
            issue_book(user_id, isbn)
        elif choice == "4":
            borrow_id = int(input("Enter Borrow Record ID: "))
            return_book(borrow_id)
        elif choice == "5":
            view_borrowed_books()
        elif choice == "6":
            view_users()
        elif choice == "7":
            add_user()
        elif choice == "8":
            print("\n=== Reports Menu ===")
            print("1. Top Borrowed Books")
            print("2. Most Active Users")
            print("3. Low Stock Books")
            print("4. Users with Fines")
            print("5. Back to Main Menu")

            report_choice = input("Enter choice: ")
            if report_choice == "1":
                top_borrowed_books()
            elif report_choice == "2":
                active_users()
            elif report_choice == "3":
                low_stock_books()
            elif report_choice == "4":
                users_with_fines()
            elif report_choice == "5":
                continue
            else:
                print("❌ Invalid choice in Reports Menu")

        elif choice == "9":
            print("Exiting Library System. Bye!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
