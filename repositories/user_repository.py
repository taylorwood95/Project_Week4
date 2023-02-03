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

# This function selects all users and creates a new list with users

def select_all():
    users = []

    sql = " SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users

# This function selects a specific user by ID

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values =  [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user =  User(result['name'], result['id'])
    return user

# This function deletes a specific user by iID

def delete(id):
    sql = "DELETE FROM users WHERE  id = %s"
    values = [id]
    run_sql(sql,values)