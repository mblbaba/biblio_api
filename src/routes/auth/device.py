from flask import make_response, request
from src.models.device import Device
from flask_jwt_extended import jwt_required

from utils import make_response_if_unknown_params_or_missing_params

def register_device_route(app, db):
    
    
    @app.route('/auth/device', methods = ['POST'])
    @jwt_required()
    def register_device():
        params = ["device_name", "created_by_id"]
        data = request.get_json()
        err = make_response_if_unknown_params_or_missing_params(params, data)
        if err:
            return err
        if Device.find_by_device_name(data['device_name']):
            return make_response({"success": -1, "message": "Device already exists"}, 400)
        device = Device(
            device_name = data['device_name'],
            created_by_id = data['created_by_id']
        )
        db.session.add(device)
        db.session.commit()
        response = {
            "success" : 1,
            "message" : "Device added successfully",
            "data" : device.json()
        }
        return make_response(response, 201)