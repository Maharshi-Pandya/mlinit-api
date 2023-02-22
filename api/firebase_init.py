from firebase_admin import firestore, initialize_app, storage, credentials
from project_creds import creds
    
creds = credentials.Certificate(creds)
admin = initialize_app(creds, {
    "storageBucket": "mlinit-api.appspot.com"
})
db = firestore.client()
bucket = storage.bucket()
