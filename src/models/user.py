from sqlalchemy import func
from app import db

class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key = True, index=True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    fisrt_name = db.Column(db.String(80), nullable = True)
    last_name = db.Column(db.String(80), nullable = True)
    is_staff = db.Column(db.Boolean, default = False)
    is_superuser = db.Column(db.Boolean, default = False)
    avatar_url = db.Column(db.Text, nullable = True)
    password = db.Column(db.Text, nullable = False)
        
    
    def __repr__(self):
        return f"user : {self.username} email {self.email} "
    
class Notification(db.Model):
    __tablename__ = "notification"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    icon = db.Column(db.Text, nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    read = db.Column(db.Boolean, nullable=False, default=False)
