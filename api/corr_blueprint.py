import http
from flask import Blueprint, jsonify, request

from utils import firebase as fbutil
from analyses import corr as dataset_corr

# information blueprint
corr_bp = Blueprint("corr_bp", __name__)

# route
@corr_bp.route("/", methods=["POST"])
def correlation():
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
            summ = dataset_corr.Correlation(dataset_url)
            summ._read_url()
            result = summ.perform_corr()
            
        except Exception as e:
            response = {
                "error": "bad request",
                "statusCode": http.HTTPStatus.BAD_REQUEST
            }
            return jsonify(response), http.HTTPStatus.BAD_REQUEST
        
        response = {
            "datasetCorrelation": result,
            "statusCode": http.HTTPStatus.OK
        }
        
        return jsonify(response), http.HTTPStatus.OK
    
    else:
        return jsonify(response), http.HTTPStatus.BAD_REQUEST
