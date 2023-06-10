from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home(): 
    return render_template("home.html")
