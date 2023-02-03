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

# This functions selects all users and creates a new list with users

def select_all():
    users = []

    sql = " SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users