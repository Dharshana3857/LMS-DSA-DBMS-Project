class User:
    def __init__(self, user_id, name, email, phone, max_books):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.max_books = max_books

    def __str__(self):
        return f"User: {self.name} ({self.user_id}) | Max Books: {self.max_books}"
