import helper
import re
import math
import json
from models.asset import Asset, AssetExterior
from bs4 import BeautifulSoup

weapon_rarity_list = [
    "consumer",
    "industrial",
    "mil-spec",
    "restricted",
    "classified",
    "covert",
    "contraband",
]

exterior_list = [
    "Factory New",
    "Minimal Wear",
    "Field-Tested",
    "Well-Worn",
    "Battle-Scarred",
    "Vanilla",
]


def get_rarity(source: str):
    for rarity in weapon_rarity_list:
        if source.lower().count(rarity):
            return rarity
    return ""


def get_exterior(source: str):
    for exterior in exterior_list:
        if source.lower().count(exterior):
            return exterior
    return ""


def is_stattrak(source: str):
    return source.lower().count("stattrak") > 0


def is_souvenir(source: str):
    return source.lower().count("souvenir") > 0


def to_asset(soup: BeautifulSoup, type: str):
    name = ""
    family_name = ""
    # name
    if type == "gloves":
        title_html = soup.select_one("h2").text
        title = title_html.split("|")
        name = title[0].strip()
        family_name = title[1].strip()
    else:
        title_html = soup.select_one("h2")
        name = title_html.select_one("a").text
        family_name = title_html.select_one("a ~ a").text

    print("Writing {} {}".format(name, family_name))

    # thumbnail
    thumbnail_html = soup.select_one(".result-box > a > img")
    if thumbnail_html == None:
        thumbnail_html = soup.select_one(".result-box img")

    thumbnail = thumbnail_html.attrs["src"]

    # rarity
    rarity_html = soup.select_one(".quality > p").text
    rarity = helper.get_rarity(rarity_html)

    # exteriors
    exterior_table = soup.select_one(".price-details-table-wrapper table")
    base_price = 25415
    rows = exterior_table.select("tbody > tr")
    asset_exterior_list = []
    for row in rows:
        cells = row.select("td")
        skin_quality = cells[0].get_text().strip()
        stattrak = is_stattrak(skin_quality)
        souvenir = is_souvenir(skin_quality)
        price_regex = "[^0-9]"
        steam_price = re.sub(price_regex, "", cells[1].get_text())
        median_price = re.sub(price_regex, "", cells[3].get_text())
        bitskins_price = re.sub(price_regex, "", cells[5].get_text())
        max_price = max(steam_price, median_price, bitskins_price)

        if max_price == "":
            max_price = 0

        final_price = round(float(max_price) / base_price, 2)
        coin = math.floor(final_price * 10)

        if coin < 1:
            coin = 1

        asset_exterior = AssetExterior(
            skin_quality, final_price, coin, stattrak, souvenir
        )
        asset_exterior_list.append(asset_exterior)
    # asset
    asset = Asset(name, family_name, thumbnail, rarity, type, asset_exterior_list)
    return asset


def save_to_file(asset: any, file_name: str):
    json_data = json.dumps(asset, default=lambda o: o.__dict__)
    with open("{}.json".format(file_name), "w") as outfile:
        outfile.write(json_data)
