import requests
from bs4 import BeautifulSoup

category_730_Weapon = [
  "tag_weapon_ak47",
  "tag_weapon_aug",
  "tag_weapon_awp",
  "tag_weapon_bayonet",
  "tag_weapon_knife_survival_bowie",
  "tag_weapon_knife_butterfly",
  "tag_weapon_knife_css",
  "tag_weapon_cz75a",
  "tag_weapon_deagle",
  "tag_weapon_elite",
  "tag_weapon_knife_falchion",
  "tag_weapon_famas",
  "tag_weapon_fiveseven",
  "tag_weapon_knife_flip",
  "tag_weapon_g3sg1",
  "tag_weapon_galilar",
  "tag_weapon_glock",
  "tag_weapon_knife_gut",
  "tag_weapon_knife_tactical",
  "tag_weapon_knife_karambit",
  "tag_weapon_knife_kukri",
  "tag_weapon_m249",
  "tag_weapon_m4a1_silencer",
  "tag_weapon_m4a1",
  "tag_weapon_knife_m9_bayonet",
  "tag_weapon_mac10",
  "tag_weapon_mag7",
  "tag_weapon_mp5sd",
  "tag_weapon_mp7",
  "tag_weapon_mp9",
  "tag_weapon_knife_gypsy_jackknife",
  "tag_weapon_negev",
  "tag_weapon_knife_outdoor",
  "tag_weapon_nova",
  "tag_weapon_hkp2000",
  "tag_weapon_p250",
  "tag_weapon_p90",
  "tag_weapon_knife_cord",
  "tag_weapon_bizon",
  "tag_weapon_revolver",
  "tag_weapon_sawedoff",
  "tag_weapon_scar20",
  "tag_weapon_sg556",
  "tag_weapon_knife_push",
  "tag_weapon_knife_skeleton",
  "tag_weapon_ssg08",
  "tag_weapon_knife_stiletto",
  "tag_weapon_knife_canis",
  "tag_weapon_knife_widowmaker",
  "tag_weapon_tec9",
  "tag_weapon_ump45",
  "tag_weapon_knife_ursus",
  "tag_weapon_usp_silencer",
  "tag_weapon_xm1014",
  "tag_weapon_taser"
]
category_730_Exterior = [
  "tag_WearCategory0",
  "tag_WearCategory1",
  "tag_WearCategory2",
  "tag_WearCategory3",
  "tag_WearCategory4",
]

response = requests.get("https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_Tournament%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Type%5B%5D=any&category_730_Weapon%5B%5D=tag_weapon_ak47&category_730_Exterior%5B%5D=tag_WearCategory0&appid=730#p1_price_asc")
soup = BeautifulSoup(response.content, "html.parser")

filters = soup.find(id="searchResultsTable")

print(filters)