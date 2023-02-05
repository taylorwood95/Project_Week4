from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.countries import Country
from models.users import User
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users/new")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", all_users=users)

@users_blueprint.route("/users", methods=["POST"])
def create_user():
    name = request.form['name']
    user = User(name)
    user_repository.save(user)
    return redirect("/users")


