# Example file showing a circle moving on screen
import pygame
from assets import CardCluster, Card
from typing import List
import random
import sys

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))

MARGIN = 50

clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

pygame.display.set_caption("52 Card Pickup")


## Setup
active_box = None
clusters: List[CardCluster] = []
cluster = CardCluster(
    cards=[], position=pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
)

for i in range(5):
    cluster.cards.append(Card(suit=0, rank=i + 1))

    # x = random.randint(MARGIN, screen.get_width()-MARGIN - 250)
    # y = random.randint(MARGIN, screen.get_height() - MARGIN - 350)
    # box = pygame.Rect(x, y, 250, 350)
    # cards.append(box)

clusters.append(cluster)
#####

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         for num, box in enumerate(clusters):
        #             if box.collidepoint(event.pos):
        #                 out = clusters.pop(num)
        #                 clusters.append(out)
        #                 active_box = len(clusters) - 1
        #                 break

        # if event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:
        #         for num, box in enumerate(clusters):
        #             if box.collidepoint(event.pos):
        #                 out = clusters.pop(num)
        #                 clusters.append(out)
        #                 active_box = len(clusters) - 1
        #                 break

        #         active_box = None

        # if event.type == pygame.MOUSEMOTION:
        #     if active_box != None:
        #         clusters[active_box].move_ip(event.rel)

        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(pygame.Color(0, 128, 0))

    # update and draw items
    for cluster in clusters:
        cluster.draw(screen)
    # pygame.draw.circle(screen, "black", player_pos, 40)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_DOWN]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_LEFT]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_RIGHT]:
    #     player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
