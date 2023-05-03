from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

post = [
    {
        "name": "Jack Black",
        "address": "123 street",
        "amount_packages": "14"
    },

    {
        "name": "Carl Black",
        "address": "6420 Sun",
        "amount_packages": 12
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=post)

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/about")
def about():
    return render_template('about.html', title="about")

if __name__ == '__main__':
    app.debug = True
    app.run()