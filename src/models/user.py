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