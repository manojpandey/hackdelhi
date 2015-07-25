from flask import Flask
from flask.ext.script import Manager
app = Flask(__name__)
from app import views

manager = Manager(app)