from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import List
import pygame


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

    def draw(self, screen: pygame.Surface, position: pygame.Rect):
        pygame.draw.rect(
            screen,
            "white",
            position,
            border_radius=7,
        )

        pygame.draw.rect(screen, "black", position, width=5, border_radius=7)


class CardCluster(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    cards: List[Card]
    # reveal: bool = True
    position: pygame.Vector2

    def draw(self, screen: pygame.Surface):
        for i, card in enumerate(self.cards):
            card.draw(
                screen, pygame.Rect(self.position.x, self.position.y + 25 * i, 250, 350)
            )
        #     pygame.draw.rect(
        #         screen,
        #         "white",
        #         rect,
        #         border_radius=7,
        #     )
        # pygame.draw.rect(
        #     screen,
        #     "black",
        #     box,
        #     width=5,
        #     border_radius=7,
        # )


class CardPosition(BaseModel):
    cluster: List[CardCluster]


if __name__ == "__main__":
    print(Card(rank=5, suit=3))
