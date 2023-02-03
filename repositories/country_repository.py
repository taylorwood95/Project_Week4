import pdb
from db.run_sql import run_sql
from models.users import User
from models.countries import Country
import repositories.user_repository as user_repository

# This function saves new countries to database

def save(country):
    sql = "INSERT INTO countries (name, capital, currency, review, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [country.name, country.capital, country.currency, country.review, country.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []

    sql = " SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country_id  = user_repository.select(row['user_id'])
        country = Country(row['name'], row['capital'], row['currency'], row['review'], country_id)
        countries.append(country)
    return countries
