# imports
from flask import Flask

# custom modules
import firebase_init
from info_blueprint import info_bp
from des_blueprint import des_bp

# init flask and firebase admin
app = Flask(__name__)
admin = firebase_init.admin
db = firebase_init.db
bucket = firebase_init.bucket

# ------------------- INFORMATION ------------------
app.register_blueprint(info_bp, url_prefix="/info")

# ------------------ DESCRIBE -----------------------
app.register_blueprint(des_bp, url_prefix="/des")