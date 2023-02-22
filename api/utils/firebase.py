import firebase_init
from utils import crypt

admin = firebase_init.admin
db = firebase_init.db
bucket = firebase_init.bucket

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