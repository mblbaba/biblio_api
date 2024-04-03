import datetime
from app import db


book_categories = db.Table(
    'book_categories',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

book_tags = db.Table(
    'book_tags',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Category(db.Model):
    __tablename__ = "category"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = True)

    def __repr__(self) :
        return f"category : {self.name}"
    
    
class Tag(db.Model):
    __tablename__ = "tag"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = True)

    def __repr__(self) :
        return f"tag : {self.name}"

class Book(db.Model):
    __tablename__ = "book"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    author = db.Column(db.Text, nullable = False)
    release_date = db.Column(db.Text, nullable = True)
    editor = db.Column(db.Text, nullable = True)
    language = db.Column(db.Text, nullable = True)
    genre = db.Column(db.Text, nullable = True)
    resume = db.Column(db.Text, nullable = False)
    page_number = db.Column(db.Integer, nullable = True)
    added_date = db.Column(db.Text, default = datetime.datetime.now(), nullable = True)
    loans_count = db.Column(db.Integer, default = 0, nullable = True)
    banner = db.Column(db.Text, nullable = True)
    rate_count = db.Column(db.Integer, default = 0, nullable = True)
    galeries = db.Column(db.String(255), nullable=True)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = True)
    
    categories = db.relationship('Category', secondary=book_categories, backref=db.backref('books', lazy=True))
    tags = db.relationship('Tag', secondary=book_tags, backref=db.backref('books', lazy=True))
    
    def __repr__(self) :
        return f"book : {self.name} author {self.author} "
    
    
class BookCopy(db.Model):
    __tablename__ = "book_copy"
    
    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable = False, )
    status = db.Column(db.Text, nullable = False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = True)
    available = db.Column(db.Boolean, default = True, nullable = True)
    
    def __repr__(self) :
        return f"book : {self.book_id} status {self.status}"

users_favorites_books = db.Table(
    'users_favorites_books',
    db.Column('favorite_id', db.Integer, db.ForeignKey('favorite.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Favorite(db.Model):
    __tablename__ = "favorite"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    books = db.relationship('Book', secondary=users_favorites_books, backref=db.backref('favorites', lazy=True))

    
    def __repr__(self):
        return f"Favorite(user_id={self.user_id})"

