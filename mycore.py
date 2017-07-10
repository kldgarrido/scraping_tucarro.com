from bs4 import BeautifulSoup
from model import Car
import requests


def execute(url, tag): # Main Method
    items = parse_url(url, tag) # Get words contained in the tag
    return items


def parse_url(url, tag):
    content = load_url(url) # Download the content of the url
    soup = BeautifulSoup(content, 'html.parser') # Parse the containt

    result = [] # result
    for item_tag in soup.find_all(tag,  class_="results-item article"):
        car = generate_car(item_tag)
        result.append(car)
    return result


def load_url(url): # Download the content of the url
    try:
        r = requests.get(url)
        return r.text
    except requests.exceptions.SSLError:
        return ""




def generate_car(details):
    price = get_field(details, tag_children_name='span', tag_children_attr="ch-price")
    year = get_field_grandchild(details, 'li', 'destaque', 'strong')
    url = getFieldAttr(details, 'div', 'images-viewer', 'item-url' )
    id_car = getFieldAttr(details, 'div', 'rowItem', 'id')
    km = get_field_grandchild_second(details, 'li', 'destaque', 'strong')

    car = Car(price=price, url=url, year=year, id=id_car, km=km)
    return car


def get_field(tag, tag_children_name, tag_children_attr):
    try:
        price = tag.find(tag_children_name, class_=tag_children_attr).text
        return price
    except AttributeError as e:
        return ""


def get_field_grandchild(tag, tag_children_name, tag_children_attr, tag_grandchild_name):
    try:
        return tag.find(tag_children_name,class_=tag_children_attr).find(tag_grandchild_name).text
    except AttributeError:
        return ""

def get_field_grandchild_second(tag, tag_children_name, tag_children_attr, tag_grandchild_name):
    try:
        return tag.find(tag_children_name,class_=tag_children_attr).find_all(tag_grandchild_name)[1].text
    except AttributeError:
        return ""


def getFieldAttr(tag, tag_children_name, tag_children_attr, tag_attr_name):
    try:
        return tag.find(tag_children_name,class_=tag_children_attr).get(tag_attr_name)
    except AttributeError:
        return ""

