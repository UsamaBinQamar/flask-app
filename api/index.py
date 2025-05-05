from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello World! This Flask app is running on Vercel."