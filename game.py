import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1063, 598))

#Background
background = pygame.image.load('./images/fon.png')

pygame.display.set_caption("Zombie")
icon = pygame.image.load('./images/zombie.png')
pygame.display.set_icon(icon)

#game engine
done = False
while not done:
    pygame.display.flip()
    screen.blit (background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()

