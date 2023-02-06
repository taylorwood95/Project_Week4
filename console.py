import pdb 
from models.countries import Country
from models.users import User

import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

user1 = User("Taylor")
user_repository.save(user1)
user2 = User("Mark")
user_repository.save(user2)

# user_repository.select_all()

# result = user_repository.select(5)

# user_repository.delete(5)

# user3 = user_repository.select(6)
# user3.name = "Brian"
# user_repository.update(user3)

country1 = Country("Netherlands", "Amsterdam", "EURO", "The cheese is amazing!", user1)
country_repository.save(country1)
country2 = Country("Scotland", "Edinburgh", "pound", "It never stopped raining !", user2)
country_repository.save(country2)

# country_repository.select_all()
# pdb.set_trace()

# country_repository.select(5)
# pdb.set_trace()

# country_repository.delete(5)

# country3 = country_repository.select(3)
# country3.capital = 'The Hague'
# country_repository.update(country3)

