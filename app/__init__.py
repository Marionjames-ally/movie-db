from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__)

# setting up configuration
app.config.from_object(DevConfig, instance_relative_config=True)
app.config.from_pyfile('config.py')

from app import views
