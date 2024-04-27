import requests
import re
import helper
from bs4 import BeautifulSoup
from models.case import Case

"""
Gloves:
extraodiary: mau do

Agent:
master: do
superior: hong
exceptional: tim
distinguished: xanh dam

Knife:
covert: do

Weapon:
consumer: xam
industrial: xanh nhat
mil-spec: xanh dam
restricted: tim
classified: hong
covert: do
contraband: vang

Sticker:
contraband: vang
extraodiary: mau do
exotic: hong
remarkable: tim
high-grade: xanh
"""

parser = "html.parser"


def save_assets():
    response = requests.get("https://csgostash.com/gloves?page=2")
    soup = BeautifulSoup(response.content, parser)
    links = soup.select(".result-box > a")
    assets = []
    for link in links:
        url = link.attrs["href"]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, parser)
        asset = helper.to_asset(soup, "gloves")
        assets.append(asset)
        print("Write {} - {} successful".format(asset.name, asset.family_name))
        print("-------------------------------------------")
    helper.save_to_file(assets, "gloves-2")


def save_cases():
    response = requests.get("https://totalcsgo.com/skins/cases")
    soup = BeautifulSoup(response.content, parser)
    items = soup.select(".results-container .masonry-item")
    cases = []
    for item in items:
        title = item.select_one(".title").text
        price = item.select_one(".price-outer-container").text
        final_price = float(price.replace("$", ""))
        case = Case(title, "", final_price)
        cases.append(case)
    helper.save_to_file(cases, "cases")


save_cases()
