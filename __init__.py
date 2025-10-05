from flask import Flask

# Initialize the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Import the routes after app is created to avoid circular imports
from app import routes