from flask import Blueprint, render_template, request
import embed, chroma

views = Blueprint(__name__, "views")

@views.route("/")
def index(): 
    return render_template("home.html")

@views.route("/submit", methods=["POST"])
def submit(): 
    if request.method == "POST":
        input_data = request.form.get("inputField")
        # Process the input_data with your Python code here
        chroma.addToCollection(input_data, 'none')
        return render_template("result.html", processed_data='Loaded this content')


@views.route("/query", methods=["POST"])
def query():
    if request.method == "POST":
        question = request.form.get("queryField")
        print(question)
        relevant_data = chroma.getRelevantResponses(question)
        # todo: query Open Assistant with original query and related journal entries
        return render_template("result.html", processed_data=relevant_data)