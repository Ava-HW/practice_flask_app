from flask import Flask, render_template

# Create the application instance
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def hello_world():
    return render_template("index.html")