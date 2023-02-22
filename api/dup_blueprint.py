import http
from flask import Blueprint, jsonify, request

from utils import firebase as fbutil
from analyses import dup as dataset_dup

# information blueprint
dup_bp = Blueprint("dup_bp", __name__)

# route
@dup_bp.route("/", methods=["POST"])
def dup():
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
            summ = dataset_dup.Duplicate(dataset_url)
            summ._read_url()
            result = summ.perform_dup()
            
        except Exception as e:
            response = {
                "error": "bad request",
                "statusCode": http.HTTPStatus.BAD_REQUEST
            }
            return jsonify(response), http.HTTPStatus.BAD_REQUEST
        
        response = {
            "datasetSummary": result,
            "statusCode": http.HTTPStatus.OK
        }
        
        return jsonify(response), http.HTTPStatus.OK
    
    else:
        return jsonify(response), http.HTTPStatus.BAD_REQUEST
