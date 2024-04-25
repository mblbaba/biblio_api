from flask import make_response, request
from src.models.book import BookCopy
from src.serializers.loans import serialize_loan, serialize_loans
from src.models.loan import Loan
from utils import get_missing_par, get_unkown_params

def register_loans_route(app, db):

    
    @app.route("/loans", methods = ['GET'])
    def loans():
        try :
            loans = Loan.query.all()
            serialized_loans = serialize_loans(loans)
            return serialized_loans
        except Exception as e:
            print(e)
            response = {}
            return make_response(response, 500)
    
    @app.route("/loans/add", methods = ['POST'])
    def loan_book():
        data = request.get_json()
        r_params = ["book_id", "user_id"]
        a_params = r_params + ["loan_date", "return_date", "created_by_id", "loan_status", "loan_duration", "fine_amount", "fine_paid", "loan_notes", "loan_type"]
        m_p = get_missing_par(r_params, data)
        if m_p:
            return make_response({"success": -1, "message": "Missing parameters: " + ", ".join(m_p)}, 200)
        u_p = get_unkown_params(a_params, data)
        if u_p:
            return make_response({"success": -1, "message": "Unknown parameters: " + ", ".join(u_p)}, 200)
        copy_book = BookCopy.query.filter(BookCopy.book_id == data["book_id"], BookCopy.available == True).first()
        if not copy_book:
            return make_response({"success": -1, "message": "Book not available"}, 200)
        
        user_loans = Loan.query.filter(Loan.book_id == data["book_id"], Loan.user_id == data["user_id"]).first()
        if user_loans:
            return make_response({"success": -1, "message": "Book already loaned"}, 200)
        
        
        
        loan = Loan(
            book_id = data["book_id"],
            user_id = data["user_id"],
            copy_book_id  = copy_book.id,
            loan_date = data.get("loan_date", None),
            return_date = data.get("return_date", None),
            created_by_id = data.get("created_by_id", None),
            loan_status = data.get("loan_status", None),
            loan_duration = data.get("loan_duration", None),
            fine_amount = data.get("fine_amount", None),
            fine_paid = data.get("fine_paid", None),
            loan_notes = data.get("loan_notes", None),
            loan_type = data.get("loan_type", None)
        )
        db.session.add(loan)
        db.session.commit()
        response = {
            "success": 1,
            "message": "Loan added successfully",
            "data": serialize_loan(loan)
        }
        return make_response(response, 201)
    
    @app.route("/loans/user/<int:user_id>", methods = ['GET'])
    def get_user_loans(user_id):
        try :
            loan_status = request.args.get('status', None)
            if not loan_status:
                loans = Loan.query.filter(Loan.user_id == user_id).all()
            else:
                loans = Loan.query.filter(Loan.user_id == user_id, Loan.loan_status == loan_status).all()
            serialized_loans = serialize_loans(loans)
            return serialized_loans
        except Exception as e:
            print(e)
            response = {}
            return make_response(response, 500)
        
        
    @app.route("/loans/delete")
    def delete_loans():
        loans = Loan.query.all()
        for loan in loans:
            db.session.delete(loan)
        db.session.commit()
        response = {
            "success" : 1,
            "message" : "Loans deleted successfully",
            "data" : {}
        }
        return make_response(response, 200)
        
        
    @app.route("/loans/<int:loan_id>/manage", methods = ['POST'])
    def manage_loan(loan_id):
        loan = Loan.query.get(loan_id)
        action = request.args.get('action', None)
        actions = ["confirm", "cancel", "return"]
        if not action:
            response = {
                "success": -1,
                "message": f"Need to specify an action {actions}",
                "data": {}
            }
            return make_response(response, 404)
        if not loan:
            response = {
                "success": -1,
                "message": "Loan not found",
                "data": {}
            }
            return make_response(response, 404)
        
        loan.loan_status = f"{action}ed".capitalize()
        copybook = BookCopy.query.get(loan.copy_book_id)
        print(copybook)
        if action == "cancel" or action == "return":
            copybook.available = True
        else:
            copybook.available = False
        db.session.commit()
        response = {
            "success": 1,
            "message": "Loan confirmed successfully",
            "data": serialize_loan(loan)
        }
        return make_response(response, 200)
    

        
    