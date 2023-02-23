# imports
from flask import Flask

# custom modules
from info_blueprint import info_bp
from des_blueprint import des_bp
from dup_blueprint import dup_bp
from out_blueprint import out_bp

# init flask app
app = Flask(__name__)

# information
app.register_blueprint(info_bp, url_prefix="/info")

# describe
app.register_blueprint(des_bp, url_prefix="/des")

# duplicates
app.register_blueprint(dup_bp, url_prefix="/dup")

# outliers
app.register_blueprint(out_bp, url_prefix="/out")