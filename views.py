from flask import Blueprint, render_template, request
import embed

views = Blueprint(__name__, "views")

@views.route("/")
def index(): 
    return render_template("home.html")

@views.route("/submit", methods=["POST"])
def submit(): 
    print('IN SUBMIT')
    if request.method == "POST":
        input_data = request.form.get("inputField")
        # Process the input_data with your Python code here
        processed_data = embed.test(input_data)  # Replace with your own processing logic
        return render_template("result.html", processed_data=processed_data)
