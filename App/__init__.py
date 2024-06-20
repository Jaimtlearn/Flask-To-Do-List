from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '085c7f29d2d74642'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo_db'

    client = MongoClient(app.config['MONGO_URI'])
    app.db = client.todo_db

    from App.routes import main
    app.register_blueprint(main)

    return app
