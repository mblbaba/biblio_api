from app import db
import uuid
class Device(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    device_name = db.Column(db.String(80))
    api_key = db.Column(db.String(80))
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = True)
    
    def __init__(self, device_name, created_by_id, api_key=None) -> None:
            self.device_name = device_name
            self.api_key = api_key or uuid.uuid4().hex
            self.created_by_id = created_by_id
            
    def json(self):
        return {
            "id": self.id,
            "device_name": self.device_name,
            "api_key": self.api_key
        }
        
    @classmethod
    def find_by_device_name(cls, device_name):
        return cls.query.filter_by(device_name = device_name).first()
    
    @classmethod
    def find_by_api_key(cls, api_key):
        return cls.query.filter_by(api_key = api_key).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()