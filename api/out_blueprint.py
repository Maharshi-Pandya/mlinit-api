import http
from flask import Blueprint, jsonify, request

from utils import firebase as fbutil
from analyses import out as dataset_out

# outliers blueprint
out_bp = Blueprint("out_bp", __name__)

# routes
@out_bp.route("/", methods=["POST"])
def outliers():
    url_params = request.args
    api_key = url_params.get("apiKey", type=str)
    out_method = url_params.get("method", type=str)    
    
    # default response
    response = {
        "error": "unauthorized",
        "statusCode": http.HTTPStatus.BAD_REQUEST
    }
    
    if fbutil.check_api_key_valid(api_key, "apiKeys", "users"):
        try:
            req_body = request.json
            dataset_url = req_body["URL"]
            
            # method check
            if out_method != "zscore" and out_method != "quantiles":
                raise
            
            # got the url, do something with it
            outl = dataset_out.Outliers(dataset_url)
            outl._read_url()
            result = outl.perform_out(method=out_method)
            
        except Exception as e:
            response = {
                "error": "bad request",
                "statusCode": http.HTTPStatus.BAD_REQUEST
            }
            return jsonify(response), http.HTTPStatus.BAD_REQUEST
        
        response = {
            "datasetOutliers": result,
            "statusCode": http.HTTPStatus.OK
        }
        
        return jsonify(response), http.HTTPStatus.OK
    
    else:
        return jsonify(response), http.HTTPStatus.BAD_REQUEST
