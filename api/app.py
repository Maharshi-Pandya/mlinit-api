# imports
import http
import json
from flask import Flask, request, jsonify
from firebase_admin import firestore, initialize_app, credentials, storage

# custom modules
from utils import crypt
from project_creds import creds
from analyses import info as dataset_info

# init flask and firebase admin
app = Flask(__name__)
creds = credentials.Certificate(creds)
admin = initialize_app(creds, {
    "storageBucket": "mlinit-api.appspot.com"
})
db = firestore.client()
bucket = storage.bucket()

# ------------------ helpers ------------------------

def check_api_key_valid(api_key: str, api_coll_name: str, users_coll_name: str) -> bool:
    """
        helper function to check if a given api key exists
        and belongs to a valid user
        
        params:
        
        api_key: the api key
        api_coll_name: collection representing apis
        users_coll_name: collection representing users
    """
    if api_key is not None:
        valid = False
        
        # verify api-key
        hashed_api_key = crypt.hash_api_key(api_key)
        
        api_doc_ref = db.collection(api_coll_name).document(hashed_api_key)
        api_doc = api_doc_ref.get()
        
        if api_doc.exists:
            fields = api_doc.to_dict()
            
            # get user id
            user_id = fields[hashed_api_key]
            user_ref = db.collection(users_coll_name).document(user_id)
            user = user_ref.get()
            
            if user.exists:
                user_fields = user.to_dict()
                valid = user_fields["apiKey"] == hashed_api_key
        
        if valid:
            return True
        
    return False

# ------------------- routes -----------------------

@app.route("/info", methods=["POST"])
def info():
    url_params = request.args
    api_key = url_params.get("apiKey", type=str)
    
    # default response
    response = {
        "error": "unauthorized",
        "statusCode": http.HTTPStatus.BAD_REQUEST
    }
    
    if check_api_key_valid(api_key, "apiKeys", "users"):
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
            "URL": dataset_url,
            "statusCode": http.HTTPStatus.OK
        }
        
        return jsonify(response), http.HTTPStatus.OK
    
    else:
        return jsonify(response), http.HTTPStatus.BAD_REQUEST
