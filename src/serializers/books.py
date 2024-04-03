def serialize_books(books):
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
            "created_by_id" : book.created_by_id
        }
        serialized_books.append(serialize_book)
    return serialized_books


def serialize_book(book):
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
        "categories" : book.categories,
        "tags" : book.tags,
        "rate_count" : book.rate_count,
        "created_by_id" : book.created_by_id
    }
    return serialized_book