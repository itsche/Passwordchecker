from flask import Flask, render_template, request
from model.password_model import check_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    if request.method == "POST":
        pw = request.form.get("password", "")
        strength = check_strength(pw)
    return render_template("password_views.html", strength=strength)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
