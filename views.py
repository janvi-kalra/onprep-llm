from flask import Blueprint, render_template, request
import chroma, googledocs
from query import get_completion_from_local 

views = Blueprint(__name__, "views")

@views.route("/")
def index(): 
    return render_template("home.html")

@views.route("/submit", methods=["POST"])

def submit(): 
    if request.method == "POST":
        google_link = request.form.get("inputField")
        input_data = googledocs.getContent(google_link)
        chroma.addToCollection(input_data, 'googleDocs')
        return render_template("home.html", process_data=None)


@views.route("/query", methods=["POST"])
def query():
    if request.method == "POST":
        # example: "What might be causing my anxiety?"
        query = request.form.get("queryField")
        resp = chroma.getRelevantResponses(query)
        # completion = get_completion_from_openassistant(query, resp['documents'])
        completion = get_completion_from_local(query, resp['documents'])

        return render_template("home.html", processed_data=completion)