from flask import Flask
from flask import render_template

# Flask instance acts as a central object/ registry (WSGI application)
app = Flask(__name__)

# By default go to home page (About section)
@app.route("/")
def home_page():
    return render_template("base.html")

# Projects page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Experience page
@app.route("/experience")
def experience():
    return render_template("experience.html")

if __name__=="__main__":
    app.run(debug=True)