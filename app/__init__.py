from flask import Flask  
from config import Config
from flask_sqlalchemy import SQLAlchemy
import cloudinary
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


app.config.from_object(Config)
db = SQLAlchemy(app)
cloud=cloudinary.config(
    cloud_name = "hendra2000",
    api_key = "296483255647495",
    api_secret = "K762LAJ6CAWSdzwD3dGY0YgNnOY"
)
jwt = JWTManager(app)



from app.models import makananModel, userModel
from app import routes