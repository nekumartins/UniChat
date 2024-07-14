from flask import Flask
from .auth.routes import auth_bp
import os

def create_app():
    app = Flask(__name__)
    
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/')
    def home():
        return "Welcome to the Home Page"

    return app
