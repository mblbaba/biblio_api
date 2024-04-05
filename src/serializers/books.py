from src.models.book import Book


def serialize_books(books, is_book_on_user_loans = False):
    serialized_books = []
    for book in books:
        categories = []
        for category in book.categories:
            categories.append(category.name)
        tags = []
        for tag in book.tags:
            tags.append(tag.name)
        serialize_book = {
            "id" : book.id,
            "is_book_on_user_loans" : is_book_on_user_loans,
            "name" : book.name,
            "author" : book.author,
            "release_date" : book.release_date,
            "editor" : book.editor,
            "language" : book.language,
            "genre" : book.genre,
            "resume" : book.resume,
            "page_number" : book.page_number,
            "added_date" : book.added_date,
            "loans_count" : book.loans_count,
            "banner" : book.banner,
            "categories" : categories,
            "tags" : tags,
            "rate_count" : book.rate_count,
            "created_by_id" : book.created_by_id,
            "copy_stock" : book.copy_stock
        }
        serialized_books.append(serialize_book)
    return serialized_books


def serialize_book(book, is_book_on_user_loans = False):
    categories = []
    for category in book.categories:
        categories.append(category.name)
    serialized_book = {
        "id" : book.id,
        "name" : book.name,
        "author" : book.author,
        "release_date" : book.release_date,
        "editor" : book.editor,
        "language" : book.language,
        "genre" : book.genre,
        "resume" : book.resume,
        "page_number" : book.page_number,
        "added_date" : book.added_date,
        "loans_count" : book.loans_count,
        "banner" : book.banner,
        "categories" : categories,
        "tags" : book.tags,
        "rate_count" : book.rate_count,
        "created_by_id" : book.created_by_id,
        "copy_stock" : book.copy_stock,
        "is_book_on_user_loans" : is_book_on_user_loans
    }
    return serialized_book


def serialize_book_copy(book_copy, book = None):
    book = serialize_book(book)
    serialized_book_copy = {
        "id" : book_copy.id,
        "book" : book,
        "status" : book_copy.status,
        "available" : book_copy.available,
        "book_id" : book_copy.book_id
    }
    return serialized_book_copy



def serialize_book_copies(books):
    serialized_books = []
    for copy in books:
        book = Book.query.get(copy.book_id)
        serialized_book = serialize_book_copy(copy, book)
        serialized_books.append(serialized_book)
    return serialized_books