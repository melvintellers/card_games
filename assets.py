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

    def draw(self, screen: pygame.Surface, rect: pygame.Rect, font):

        pygame.draw.rect(
            screen,
            "white",
            rect,
            border_radius=7,
        )

        pygame.draw.rect(
            screen,
            "black",
            rect,
            width=5,
            border_radius=7,
        )

        screen.blit(
            font.render(f"{self.rank.name} - {self.suit.name}", True, (255, 0, 0)),
            (rect.x + 25, rect.y + 25),
        )


class CardCluster(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    cards: List[Card]
    rects: List[pygame.Rect] = []
    # reveal: bool = True
    position: pygame.Vector2

    def update_rects(self):
        if len(self.rects) != len(self.cards):
            self.rects = [
                pygame.Rect(self.position.x, self.position.y + 50 * i, 250, 350)
                for i in range(len(self.cards))
            ]
            # print(self.rects)

        else:
            for i, rect in enumerate(self.rects):
                rect.x, rect.y = self.position.x, self.position.y + 50 * i

    def split(self, index: int) -> "CardCluster":
        new_cluster = CardCluster(
            cards=self.cards[index:],
            position=pygame.Vector2(
                self.rects[index].x,
                self.rects[index].y,
            ),
        )
        self.cards = self.cards[:index]

        self.update_rects()
        new_cluster.update_rects()

        return new_cluster

    def join(self, cluster: "CardCluster") -> None:
        self.cards.extend(cluster.cards)
        self.update_rects()

    def draw(self, screen: pygame.Surface, font):
        self.update_rects()

        for i, (card, rect) in enumerate(zip(self.cards, self.rects)):
            card.draw(
                screen,
                rect,
                font,
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
