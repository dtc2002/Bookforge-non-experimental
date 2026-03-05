class BookManager:
    def __init__(self, app):
        self.app = app
        self.books = []
        self.current_book = None

    def load_books(self):
        # Load books from SQLite store
        pass

    def select_book(self, book_id):
        self.current_book = book_id
        self.app.update_ui()

    def add_book(self, book_data):
        # Add new book to SQLite store
        pass