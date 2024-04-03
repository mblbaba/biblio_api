from flask import make_response


def get_missing_par(params : list, data : dict):
    missing_params = []
    for param in params :
        if param not in data.keys():
            missing_params.append(param)
    return missing_params
    
    
def get_unkown_params(params : list, data : dict):
    unkn_parms = []
    for key in data.keys():
        if key not in params :
            unkn_parms.append(key)
    return unkn_parms


def make_response_if_unknown_params_or_missing_params(params, data):
    missing_params = get_missing_par(params, data)
    unkn_params = get_unkown_params(params, data)
    if missing_params :
        response = {
            "success" : -1,
            "message" : f"Missing parameters : {missing_params}",
            "data" : {}
            
        }
        return make_response(response, 400)
    
    if unkn_params :
        response = {
            "success" : -1,
            "message" : f"Unknown parameters : {unkn_params}",
            "data" : {}
            
        }
        return make_response(response, 400)
    
    
def make_response_if_not_instance_of_model(instance, model_instance):
    print(instance)
    if not instance:
        print("not instance")
        response = {
                "success" : -1,
                "message" : f"{model_instance} not found",
                "data" : {}
        }
        return make_response(response, 404)