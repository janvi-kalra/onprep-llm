from flask import Blueprint, render_template, request
import embed

views = Blueprint(__name__, "views")

@views.route("/")
def index(): 
    return render_template("home.html")

@views.route("/submit", methods=["POST"])
def submit(): 
    if request.method == "POST":
        input_data = request.form.get("inputField")
        # Process the input_data with your Python code here
        processed_data = embed.test(input_data)  # Replace with your own processing logic
        return render_template("result.html", processed_data=processed_data)


@views.route("/query", methods=["POST"])
def query():
    if request.method == "POST":
        input_data = request.form.get("inputField")
        # todo:query chroma embeddings database with text to get stored journal entries with related embeddings
        # todo: query Open Assistant with original query and related journal entries
        return render_template("result.html", processed_data="Congrats, this will soon work for you!")
