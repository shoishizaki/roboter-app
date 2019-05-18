class Restaurant():
    def __init__(self, restaurant, count):
        self.restaurant = restaurant
        self.count = count

    def get_restaurant(self):
        return self.restaurant

    def get_count(self):
        return self.count

    def set_count(self, count):
        self.count = count
