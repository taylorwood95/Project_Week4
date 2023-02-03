import pdb 
from models.countries import Country
from models.users import User

import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

user1 = User("Taylor")
user_repository.save(user1)
user2 = User("Mark")
user_repository.save(user2)

user_repository.select_all()
