from flask import Flask, request, jsonify
from bson.json_util import dumps
from pymongo import MongoClient
from .auth.routes import auth_bp
from pymongo.errors import PyMongoError

import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    mongo = MongoClient(app.config['MONGO_URI'])
    

    
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/')
    def home():
        return "Welcome to the Home Page"
    


    @app.route('/add_user', methods=['GET', 'POST'])
    def add_user():
        if request.method == 'POST':
            # test database connection with atlas
            try:
                mongo.db.command('ping')
                return "Database connection successful."
            except PyMongoError as e:
                return f"Database connection failed: {str(e)}"
        else:
            # Handle GET request or inform the user about the correct usage
            return "This route expects a POST request with user data."
        
    @app.route('/get_users', methods=['GET'])
    def get_users():
        users = mongo.db.users.find()
        return dumps(users)

    return app
