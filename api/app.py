# imports
from flask import Flask
from flask_cors import CORS

# custom modules
from info_blueprint import info_bp
from des_blueprint import des_bp
from dup_blueprint import dup_bp
from out_blueprint import out_bp
from corr_blueprint import corr_bp

# init flask app
app = Flask(__name__)
CORS(app)

# information
app.register_blueprint(info_bp, url_prefix="/info")

# describe
app.register_blueprint(des_bp, url_prefix="/des")

# duplicates
app.register_blueprint(dup_bp, url_prefix="/dup")

# outliers
app.register_blueprint(out_bp, url_prefix="/out")

# correlation
app.register_blueprint(corr_bp, url_prefix="/corr")