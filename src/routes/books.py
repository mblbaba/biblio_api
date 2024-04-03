from flask import make_response, request

from src.models.book import Book, Category
from src.serializers.books import serialize_book, serialize_books
from src.serializers.only_name import serialize_only_name, serialize_only_names
from utils import make_response_if_not_instance_of_model, make_response_if_unknown_params_or_missing_params

def resgiter_books_route(app, db):
    @app.route('/books', methods = ['GET'])
    def books():
        books = Book.query.all()
        serialized_books = serialize_books(books)
        return serialized_books
    
    @app.route("/books/add", methods = ['POST'])
    def add_book():
        data = request.get_json()
        params = ["name", "author", "release_date", "editor", "language", "genre", "resume", "page_number", "loans_count", "banner", "categories", "tags", "rate_count", "created_by_id"]
        make_response_if_unknown_params_or_missing_params(params, data)
        category_ids = data.get('categories', [])

        categories = Category.query.filter(Category.id.in_(category_ids)).all()

        book = Book(
            name=data['name'],
            author=data['author'],
            release_date=data['release_date'],
            editor=data['editor'],
            language=data['language'],
            genre=data['genre'],
            resume=data['resume'],
            page_number=data['page_number'],
            loans_count=data['loans_count'],
            banner=data['banner'],
            rate_count=data['rate_count'],
            created_by_id=data['created_by_id'],
        )
        book.categories.extend(categories)
        db.session.add(book)
        db.session.commit()
        
        response = {
            "success" : 1,
            "message" : "Book added successfully",
            "data" : serialize_book(book)
        }
        
        return response
    
    
    @app.route("/books/delete/<int:id>", methods = ['DELETE'])
    def delete_book(id):
        book = Book.query.get(id)
        err = make_response_if_not_instance_of_model(book, "Book")
        if err:
            return err
        print("okay")
        db.session.delete(book)
        db.session.commit()
        response = {
            "success" : 1,
            "message" : "Book deleted successfully",
            "data" : {}
        }
        return make_response(response, 200)
    
    @app.route("/books/<int:id>", methods = ['GET'])
    def get_book(id):
        book = Book.query.get(id)
        err = make_response_if_not_instance_of_model(book, "Book")
        if err:
            return err
        return serialize_book(book)
    
    @app.route("/books/update/<int:id>", methods = ['PUT'])
    def update_book(id):
        data = request.get_json()
        book = Book.query.get(id)
        err = make_response_if_not_instance_of_model(book, "Book")
        if err:
            return err
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        response = {
            "success" : 1,
            "message" : "Book updated successfully",
            "data" : serialize_book(book)
        }
        return make_response(response, 200)
    
    
    
    @app.route("/books/filter", methods = ['GET'])
    def filter_books_by_category():
        category_id = request.args.get('category_id')
        books = Book.query.filter(Book.categories.any(Category.id == category_id)).all()
        return serialize_books(books)
    
    @app.route("/categories/add", methods = ['POST'])
    def add_category():
        params=["name", "created_by_id"]
        data = request.get_json()
        err = make_response_if_unknown_params_or_missing_params(params, data)
        if err:
            return err
        category = Category(
            name = data['name'],
            created_by_id = data['created_by_id']
        )
        db.session.add(category)
        db.session.commit()
        response = {
            "success" : 1,
            "message" : "Category added successfully",
            "data" : serialize_only_name(category)
        }
        return make_response(response, 201)
    
    
    @app.route("/categories", methods = ['GET'])
    def categories():
        categories = Category.query.all()
        return serialize_only_names(categories)