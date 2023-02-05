from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.countries import Country
from models.users import User
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

