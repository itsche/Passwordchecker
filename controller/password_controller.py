# controller/password_controller.py
from flask import Flask, render_template, request
from model.password_model import check_strength
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "../templates"))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    result = {}
    if request.method == "POST":
        password = request.form.get("password", "")
        result = check_strength(password)
    return render_template("password_views.html",
                           password=password,
                           strength=result.get("strength", ""),
                           feedback=result.get("feedback", ""))

if __name__ == "__main__":
    app.run(debug=True)

