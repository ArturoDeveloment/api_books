from flask import Flask
from config import server

app = Flask(__name__)

def create_app():
    return app