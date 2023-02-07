from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.countries import Country
from models.users import User
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

countries_blueprint = Blueprint("countries", __name__)

# GET countries
@countries_blueprint.route("/countries")
def show_countries():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    return render_template(
        "/countries/new_country.html", all_countries=countries, all_users=users
    )


# ADD countries
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    user_id = request.form["user_id"]
    name = request.form["name"]
    capital = request.form["capital"]
    currency = request.form["currency"]
    review = request.form["review"]

    user = user_repository.select(user_id)
    country = Country(name, capital, currency, review, user)
    country_repository.save(country)
    return redirect("/countries")


@countries_blueprint.route("/countries/<int:id>", methods=["GET"])
def show_country(id):

    country = country_repository.select(id)

    return render_template("/countries/show.html", country=country)


@countries_blueprint.route("/countries/<int:id>/edit", methods=["GET"])
def edit_country(id):
    country = country_repository.select(id)
    users = user_repository.select_all()
    return render_template("countries/edit.html", country=country, user=users)


@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    # user_id = request.form["user_id"]
    name = request.form["name"]
    capital = request.form["capital"]
    currency = request.form["currency"]
    review = request.form["review"]
    user = user_repository.select(request.form["user_id"])
    # user = user_repository.select(user_id)
    country = Country(name, capital, currency, review, user, id)
    country_repository.update(country)
    return redirect("/countries")


@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")
