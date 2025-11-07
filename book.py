class Book:
    def __init__(self, isbn, title, author, publisher, year, total_copies, available_copies, category):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.category = category

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) | {self.available_copies}/{self.total_copies} available"
