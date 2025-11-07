from datetime import datetime
from db import get_connection

# ================== ISSUE BOOK ==================
def issue_book(user_id, isbn):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if book is available
    cursor.execute("SELECT available_copies FROM books WHERE isbn=%s", (isbn,))
    result = cursor.fetchone()
    if not result or result[0] <= 0:
        print("❌ Book not available")
        return

    issue_date = datetime.now().date()

    # Ask user/admin to set due date manually
    due_date_input = input("Enter Due Date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format! Use YYYY-MM-DD.")
        return

    # Insert record with chosen due date
    cursor.execute("""
        INSERT INTO borrow_records (user_id, isbn, issue_date, due_date)
        VALUES (%s, %s, %s, %s)
    """, (user_id, isbn, issue_date, due_date))

    # Reduce available copies
    cursor.execute("""
        UPDATE books SET available_copies = available_copies - 1 WHERE isbn = %s
    """, (isbn,))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Book issued! Due on {due_date}")


# ================== RETURN BOOK ==================
def return_book(borrow_id):
    conn = get_connection()
    cursor = conn.cursor()

    # Get borrow record
    cursor.execute("""
        SELECT isbn, due_date 
        FROM borrow_records 
        WHERE id=%s AND return_date IS NULL
    """, (borrow_id,))
    row = cursor.fetchone()
    if not row:
        print("❌ Invalid borrow ID or book already returned")
        return

    isbn, due_date = row
    return_date = datetime.now().date()

    # Fine: ₹10/day late
    fine = 0
    if return_date > due_date:
        fine = (return_date - due_date).days * 10

    # Update borrow record
    cursor.execute("""
        UPDATE borrow_records 
        SET return_date=%s, fine=%s 
        WHERE id=%s
    """, (return_date, fine, borrow_id))

    # Increase available copies
    cursor.execute("""
        UPDATE books SET available_copies = available_copies + 1 WHERE isbn = %s
    """, (isbn,))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Book returned! Fine: ₹{fine}")
