from src.models.book import Book, BookCopy
from src.models.user import User
from src.serializers.books import serialize_book_copy
from src.serializers.users import serialize_user


def serialize_loan(loan):
    book_copy = BookCopy.query.get(loan.copy_book_id)
    user = User.query.get(loan.user_id)
    book = Book.query.get(loan.book_id)
    
    serialized_book_copy = serialize_book_copy(book_copy, book)
    serialized_user = serialize_user(user)
    
    serialized_loan = {
        "id" : loan.id,
        "book_id" : loan.book_id,
        "user_id" : loan.user_id,
        "loan_date" : loan.loan_date,
        "return_date" : loan.return_date,
        "created_at" : loan.created_at,
        "updated_at" : loan.updated_at,
        "created_by_id" : loan.created_by_id,
        "copy_book_id" : loan.copy_book_id,
        "loan_status" : loan.loan_status,
        "loan_duration" : loan.loan_duration,
        "fine_amount" : loan.fine_amount,
        "fine_paid" : loan.fine_paid,
        "renewal_count" : loan.renewal_count,
        "renewal_date" : loan.renewal_date,
        "loan_notes" : loan.loan_notes,
        "loan_type" : loan.loan_type,
        "notification_sent" : loan.notification_sent,
        "late_return" : loan.late_return,
        "book_copy" : serialized_book_copy,
        "user" : serialized_user
        }
    return serialized_loan


def serialize_loans(loans):
    serialized_loans = []
    for loan in loans:
        serialized_loan = serialize_loan(loan)
        serialized_loans.append(serialized_loan)
    return serialized_loans