from app import db
from sqlalchemy.sql import func

class Loan(db.Model):
    __tablename__ = "loan"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    loan_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    return_date = db.Column(db.DateTime(timezone=True), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated_at = db.Column(db.DateTime(timezone=True),  onupdate=func.now(), nullable=True)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    copy_book_id = db.Column(db.Integer, db.ForeignKey('book_copy.id'), nullable=False)
    loan_status = db.Column(db.Text, nullable=True, default="Pending")  
    loan_duration = db.Column(db.Integer, nullable=True)  
    fine_amount = db.Column(db.Float, nullable=True)  
    fine_paid = db.Column(db.Boolean, nullable=True)  
    renewal_count = db.Column(db.Integer, nullable=True, default=0)  
    renewal_date = db.Column(db.DateTime(timezone=True), nullable=True)  
    loan_notes = db.Column(db.Text, nullable=True)  
    loan_type = db.Column(db.Text, nullable=True, default="Normal")  
    notification_sent = db.Column(db.Boolean, nullable=True, default=False)  
    late_return = db.Column(db.Boolean, nullable=True, default=False)
