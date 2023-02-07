class Country:
    def __init__(self, name, capital, currency, review, user, visited=False, id=None):
        self.name = name
        self.capital = capital
        self.currency = currency
        self.review = review
        self.user = user
        self.id = id
        self.visited = visited
