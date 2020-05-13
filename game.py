import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()

display_width = 1000
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

zombie_width = 64
zombie_height = 64
zombie_x = display_width - 150
zombie_y = display_height - zombie_height - 120

#Background
background = pygame.image.load('./images/fon.png')

pygame.display.set_caption("Zombie")
icon = pygame.image.load('./images/zombie.jpg')
pygame.display.set_icon(icon)

#game engine
done = False
while not done:
    pygame.display.flip()
    display.blit (background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(display, (122, 132, 253), (zombie_x, zombie_y, zombie_width, zombie_height))

    pygame.display.update()
    clock.tick(60)

pygame.quit()

