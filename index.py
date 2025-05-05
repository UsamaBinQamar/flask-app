from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello World! This Flask app is running on Vercel."

# This is important - DO NOT add app.run() here