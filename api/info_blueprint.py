import http
from flask import Blueprint, jsonify, request

from utils import firebase as fbutil
from analyses import info as dataset_info

# information blueprint
info_bp = Blueprint("info_bp", __name__)

# route
@info_bp.route("/", methods=["POST"])
def info():
    url_params = request.args
    api_key = url_params.get("apiKey", type=str)
    
    # default response
    response = {
        "error": "unauthorized",
        "statusCode": http.HTTPStatus.BAD_REQUEST
    }
    
    if fbutil.check_api_key_valid(api_key, "apiKeys", "users"):
        try:
            req_body = request.json
            dataset_url = req_body["URL"]
            
            # got the url, do something with it
            inf = dataset_info.Info(dataset_url)
            inf._read_url()
            result = inf.perform_info()
            
        except Exception as e:
            response = {
                "error": "bad request",
                "statusCode": http.HTTPStatus.BAD_REQUEST
            }
            return jsonify(response), http.HTTPStatus.BAD_REQUEST
        
        response = {
            "datasetInfo": result,
            "statusCode": http.HTTPStatus.OK
        }
        
        return jsonify(response), http.HTTPStatus.OK
    
    else:
        return jsonify(response), http.HTTPStatus.BAD_REQUEST
