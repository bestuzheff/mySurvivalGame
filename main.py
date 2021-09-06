import pygame

size = widht, height = (960, 540)
screen = pygame.display.set_mode(size)

def load_image(image_file_name):
    full_image_file_name = 'data' + '/' + 'images' + '/' + image_file_name
    try:
        image = pygame.image.load(full_image_file_name).convert()
    except any:
        print("Ошибка загрузка изображения:", image_file_name)
        raise SystemExit()
    return image




pygame.init()


def draw():
    screen.fill((255, 255, 255))
    screen.fill(pygame.Color('red'), pygame.Rect(50, 50, 60, 120))

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
