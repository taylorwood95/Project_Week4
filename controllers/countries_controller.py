from flask import FLask, render_template, request, redirect
from flask import Blueprint
from models.countries import Country
from models.users import User
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select()
    return render_template("counties/index.html, all_countries=countries")



