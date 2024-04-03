from flask import jsonify, make_response, request
from src.serializers.books import serialize_books
from src.models.book import Book, Favorite
from src.models.user import User
from src.serializers.users import serialize_user, serialize_users
from utils import get_missing_par, get_unkown_params, make_response_if_unknown_params_or_missing_params


def register_users_route(app, db):
    @app.route('/users', methods = ['GET'])
    def users():
        users = User.query.all()
        serialized_users = serialize_users(users)
        return serialized_users
    
    @app.route('/users/add', methods = ['POST'])
    def add_user():
        data = request.get_json()
        params = ["id","username", "email", "fisrt_name", "last_name", "is_staff", "is_superuser", "avatar_url", "password"]
        make_response_if_unknown_params_or_missing_params(params, data)
        
        user = User(
            username = data['username'],
            email = data['email'],
            fisrt_name = data['fisrt_name'],
            last_name = data['last_name'],
            is_staff = data['is_staff'],
            is_superuser = data['is_superuser'],
            avatar_url = data['avatar_url'],
            password = data['password']
        )
        db.session.add(user)
        db.session.commit()
        response = {
            "success" : 1,
            "message" : "User added successfully",
            "data" : serialize_user(user)
        }
        return make_response(response, 201)
    
    
    
    @app.route('/users/<int:id>', methods = ['GET'])
    def get_user(id):
        user = User.query.get(id)
        if not user:
            response = {
                "success" : -1,
                "message" : "User not found",
                "data" : {}
            }
            return make_response(response, 404)
        serialized_user = serialize_user(user)
        return serialized_user
    
    @app.route("/users/delete/<int:id>", methods = ['DELETE'])
    def delete_user(id):
        user = User.query.get(id)
        if not user:
            response = {
                "success" : -1,
                "message" : "User not found",
                "data" : {}
            }
            return make_response(response, 404)
        db.session.delete(user)
        db.session.commit()
        response = {
            "success" : 1,
            "message" : "User deleted successfully",
            "data" : {}
        }
        return make_response(response, 200)
    
    
    @app.route('/users/update/<int:id>', methods = ['PUT'])
    def update_user(id):
        data = request.get_json()
        user = User.query.get(id)
        if not user:
            response = {
                "success" : -1,
                "message" : "User not found",
                "data" : {}
            }
            return make_response(response, 404)
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        response = {
            "success" : 1,
            "message" : "User updated successfully",
            "data" : serialize_user(user)
        }
        return make_response(response, 200)
    
    @app.route('/users/<int:id>/favorites', methods = ['GET'])
    def get_user_favorites_books(id):
        user = User.query.get(id)
        print(user)
        if not user:
            response = {
                "success" : -1,
                "message" : "User not found",
                "data" : {}
            }
            return make_response(response, 404)
        favorites = Favorite.query.filter(Favorite.user_id == id).first()
        print(favorites)
        books = favorites.books
        serialized_books = serialize_books(books)
        return serialized_books
    
    @app.route('/users/<int:id>/favorite/add', methods=['POST'])
    def add_user_favorite(id):
        params = ["books_ids"]
        data = request.get_json()
        
        err = make_response_if_unknown_params_or_missing_params(params, data)
        if err:
            return err
        
        books_ids = data.get('books_ids', [])
        
        books = Book.query.filter(Book.id.in_(books_ids)).all()
        
        for book in books:
            print(book.id)
        favorite = Favorite(user_id=id)
        favorite.books.extend(books)
        
        db.session.add(favorite)
        db.session.commit()
        return "ok"

        
        
        
        