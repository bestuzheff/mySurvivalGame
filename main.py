import pygame

size = widht, height = (960, 540)
screen = pygame.display.set_mode(size)
pygame.init()


def draw():
    screen.fill((255, 255, 255))
    screen.fill(pygame.Color('red'), pygame.Rect(50, 50, 60, 120))

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
