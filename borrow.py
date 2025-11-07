class BorrowRecord:
    def __init__(self, record_id, user_id, isbn, issue_date, due_date, return_date, fine):
        self.record_id = record_id
        self.user_id = user_id
        self.isbn = isbn
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine = fine

    def __str__(self):
        return f"BorrowRecord #{self.record_id} | User: {self.user_id}, Book: {self.isbn}, Fine: {self.fine}"
