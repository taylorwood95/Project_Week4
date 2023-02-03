from db.run_sql import run_sql
from models.users import User

# This function saves new users to database

def save(user):
    sql = "INSERt INTO users (name) VALUES (%s) RETURNING *"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user