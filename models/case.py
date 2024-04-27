from typing import List


class Case:
    def __init__(
        self,
        name: str,
        thumbnail: str,
        price: float,
    ):
        self.name = name
        self.thumbnail = thumbnail
        self.price = price
