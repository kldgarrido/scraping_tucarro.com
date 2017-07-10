
class Car:
    def __init__(self, id, url, price, year, km):
        self.id = id
        self.url = url
        self.price = price
        self.year = year
        self.km = km

    def __str__(self):
        return '"'+self.price+'","'+self.year+'","'+self.km+'"'

class Tagmodel:
    def __init__(self, tag_children_name, tag_children_attr):
        self.tag_children_name = tag_children_name
        self.tag_children_attr = tag_children_attr



