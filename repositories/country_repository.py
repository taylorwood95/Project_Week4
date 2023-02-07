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

# Thus function selects all countries and creates a list of them

def select_all():
    countries = []

    sql = " SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        user  = user_repository.select(row['user_id'])
        country = Country(row['name'], row['capital'], row['currency'], row['review'], user, row['id'])
    
        countries.append(country)
      
        
    return countries

# This function selects a specific country by ID

def select(id):
    country = None 
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    # pdb.set_trace()

    if result is not None:
        user = user_repository.select(result['user_id'])
        country = Country(result['name'], result['capital'], result['currency'], result['review'], user , result['id'])
    return country

# This function deletes a specifiv country by ID

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# This function allows you to edit a country by ID 

def update(country):
    sql = "UPDATE countries SET (name, capital, currency, review, user_id) = (%s,%s,%s,%s,%s) WHERE id = %s"
    values = [country.name, country.capital, country.currency, country.review, country.user.id, country.id]
    pdb.set_trace()
    run_sql(sql, values)    
    print(values)