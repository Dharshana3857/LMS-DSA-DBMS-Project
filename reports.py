from db import get_connection

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
    for row in rows:
        print(f"{row[0]} | Borrowed {row[1]} books")
    cursor.close()
    conn.close()
