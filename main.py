from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! First page"

@app.route("/<name>")
def user(name):
    return f'hello {name}'

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/about")
def about():
    return f'about page'

if __name__ == "__main__":
    app.run()