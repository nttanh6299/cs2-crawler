from typing import List


class AssetExterior:
    def __init__(
        self, exterior: str, price: float, coin: int, stattrak: bool, souvenir: bool
    ):
        self.exterior = exterior
        self.price = price
        self.coin = coin
        self.stattrak = stattrak
        self.souvenir = souvenir


class Asset:
    def __init__(
        self,
        name: str,
        family_name: str,
        thumbnail: str,
        rarity: str,
        asset_type: str,
        exteriors: List[AssetExterior],
    ):
        self.name = name
        self.family_name = family_name
        self.thumbnail = thumbnail
        self.rarity = rarity
        self.type = asset_type
        self.exteriors = exteriors
