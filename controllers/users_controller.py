from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.countries import Country
from models.users import User
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)
 # GET users
@users_blueprint.route("/users")
def show_users():
    users = user_repository.select_all()
    return render_template("/users/new_user.html", all_users=users)

# Add user
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    name = request.form['name']
    user = User(name)
    user_repository.save(user)
    return redirect("/users")

# GET user by ID
@users_blueprint.route("/users/<id>", methods=['GET'])
def show_user_by_id(id):
    user = user_repository.select(id)
    return render_template("users/<id>", methods=['GET'], user=user)

@users_blueprint.route("/users/<id>/delete", methods=["POST"])
def delete_user(id):
    user = user_repository.delete(id)
    return redirect("/users")