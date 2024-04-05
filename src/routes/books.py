from flask import make_response, request

from src.models.loan import Loan
from src.routes.auth.security.login_required import login_required
from src.routes.auth.security.api_required import api_required
from src.models.book import Book, BookCopy, Category
from src.serializers.books import serialize_book, serialize_book_copies, serialize_book_copy, serialize_books
from src.serializers.only_name import serialize_only_name, serialize_only_names
from utils import make_response_if_not_instance_of_model, make_response_if_unknown_params_or_missing_params

def resgiter_books_route(app, db):
    
    
    
    
    @app.route('/books', methods = ['GET'])
    def books():
        is_book_on_user_loans = False
        uid = request.args.get("uid", None)
        books = Book.query.all()
        if uid != None and uid.isdigit():
            for book in books :
                try :
                    loned_book = Loan.query.filter(Loan.book_id == book.id, Loan.user_id == uid).first()
                    if (loned_book) : 
                       is_book_on_user_loans = True
                       break
                except Exception as e :
                    print("une erreur s'est produite")
        else:
            print("not uid")
        print(is_book_on_user_loans)
        serialized_books = serialize_books(books, is_book_on_user_loans)
        limit = request.args.get('limit')
        if limit and limit.isdigit():
            serialized_books = serialized_books[:int(limit)]
        return serialized_books
    
    @app.route("/books/add", methods = ['POST'])
    # @api_required
    # @login_required
    def add_book():
        data = request.get_json()
        params = ["name", "author", "release_date", "editor", "language", "genre", "resume", "page_number", "loans_count", "banner", "categories", "tags", "rate_count", "created_by_id", "copy_stock"]
        err = make_response_if_unknown_params_or_missing_params(params, data)
        if err :
            return err
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
    
    @app.route("/books/search", methods = ['GET'])
    def seach_books():
        query = request.args.get('q', None)
        category = request.args.get('category', None)
        
        if not query:
            return "Please enter a query"
        if not category:
            books = Book.query.filter(Book.name.contains(query)).all()
            serialized_book = serialize_books(books)
            return serialized_book
        
        books = Book.query.filter(Book.name.contains(query), Book.categories.any(Category.name == category)).all()
        
        serialized_book = serialize_books(books)
        
        return serialized_book
    
    
    @app.route("/books/copies", methods = ['GET'])
    def books_copies():
        try :
            books = BookCopy.query.all()
            serialized_books = serialize_book_copies(books)
            return serialized_books
        except Exception as e:
            print(e)
            response = {}
            return make_response(response, 500)
    
    @app.route("/books/<int:id>/copies", methods = ['GET'])
    def get_book_copies(id):
        try :
            book_copies = BookCopy.query.filter(BookCopy.book_id == id).all()
            serialized_book_copies = serialize_book_copies(book_copies)
            return serialized_book_copies
        except Exception as e:
            print(e)
            response = {}
            return make_response(response, 500)
    
        
    @app.route("/books/<int:id>/copy/add", methods=['POST'])
    def add_book_copy(id):
        try :
            book = Book.query.get(id)
            if not book:
                response = {
                    "success": -1,
                    "message": "Book not found",
                    "data": {}
                }
                return make_response(response, 404)

            # Créer une nouvelle copie du livre
            book_copy = BookCopy(
                book_id=book.id,
                status="available",
                available=True,
                created_by_id=book.created_by_id
            )
            db.session.add(book_copy)

            if book.copy_stock is None: book.copy_stock = 1
            else: book.copy_stock = book.copy_stock + 1
            
            db.session.commit()

            serialized_book_copy = serialize_book_copy(book_copy, book)

            response = {
                "success": 1,
                "message": "Book copy added successfully",
                "data": serialized_book_copy
            }
            return make_response(response, 200)
        except Exception as e:
            print(e)
            response = {
                "success": -1,
                "message": "Something went wrong",
                "data": {}
            }
            return make_response(response, 500)
    @app.route("/books/<int:id>/copy/delete", methods=['DELETE'])
    def delete_book_copy(id):
        book = Book.query.get(id)
        copy = BookCopy.query.filter(BookCopy.book_id == id).first()
        if not copy:
            response = {
                "success": -1,
                "message": "Book does not exist or has no copies",
                "data": {}
            }
            return make_response(response, 404)
        db.session.delete(copy)
        if book.copy_stock is None: book.copy_stock = 0
        else: book.copy_stock = book.copy_stock - 1
        db.session.commit()
        response = {
            "success": 1,
            "message": "Book copy deleted successfully",
            "data": {
                "book": serialize_book(book)
            }
        }
        return make_response(response, 200)


