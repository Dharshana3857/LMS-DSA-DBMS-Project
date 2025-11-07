import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from db import get_connection

def send_due_email_reminders():
    conn = get_connection()
    cursor = conn.cursor()
    today = datetime.now().date()

    # Fetch all users with books due today
    cursor.execute("""
        SELECT u.email, u.name, b.title, br.due_date
        FROM borrow_records br
        JOIN users u ON br.user_id = u.user_id
        JOIN books b ON br.isbn = b.isbn
        WHERE br.return_date IS NULL AND br.due_date = %s
        ORDER BY u.email
    """, (today,))
    reminders = cursor.fetchall()

    if not reminders:
        print("✅ No books due today.")
        return

    # Sender credentials (library Gmail)
    sender_email = "dharshanavijay7@gmail.com"       # <-- your Gmail
    sender_password = "ojhorwomofvlzbwh"      # <-- your App Password

    # Group books by user
    user_books = {}
    for email, name, title, due_date in reminders:
        if email not in user_books:
            user_books[email] = {"name": name, "books": []}
        user_books[email]["books"].append((title, due_date))

    # Send one email per user
    for email, data in user_books.items():
        name = data["name"]
        books = data["books"]

        subject = "📚 Library Due Reminder"
        body = f"Hello {name},\n\nThe following books are due today:\n\n"
        for title, due_date in books:
            body += f" - {title} (Due: {due_date})\n"

        body += "\nPlease return them to avoid fines.\n\nRegards,\nLibrary Management System"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = email

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print(f"✅ Reminder sent to {email}")
        except Exception as e:
            print(f"❌ Failed to send email to {email}: {e}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("\n=== Sending Email Reminders ===")
    send_due_email_reminders()
