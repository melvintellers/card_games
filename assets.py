from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import List
from pygame import Vector2


class Suit(int, Enum):
    SPADE = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3


class Rank(int, Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Color(int, Enum):
    BLACK = 0
    RED = 1


class Card(BaseModel):
    suit: Suit
    rank: Rank

    @property
    def color(self) -> Color:
        return Color(self.suit % 2)


class CardCluster(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    cards: List[Card]
    reveal: bool
    position: Vector2

class CardPosition(BaseModel):
    cluster: List[CardCluster]
    


if __name__ == "__main__":
    print(Card(rank=5, suit=3))
