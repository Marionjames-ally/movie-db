from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
# Initializing application
app = Flask(__name__)

# setting up configuration
app.config.from_object(DevConfig, instance_relative_config=True)
app.config.from_pyfile('config.py')

from app import views
