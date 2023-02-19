import os
from dotenv import load_dotenv

load_dotenv()

# get the secrets from .env file
private_key_id = os.environ.get("PRIVATE_KEY_ID")
private_key = os.environ.get("PRIVATE_KEY")

creds = {
    "type": "service_account",
    "project_id": "mlinit-api",
    "private_key_id": private_key_id,
    "private_key": private_key,
    "client_email": "firebase-adminsdk-hxkx8@mlinit-api.iam.gserviceaccount.com",
    "client_id": "115654890607707303673",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-hxkx8%40mlinit-api.iam.gserviceaccount.com"
}