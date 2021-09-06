import pygame

size = widht, height = (1024, 768)
screen = pygame.display.set_mode(size)


def load_image(image_file_name):
    full_image_file_name = 'data' + '/' + 'images' + '/' + image_file_name
    try:
        image = pygame.image.load(full_image_file_name).convert_alpha()
        # image = pygame.transform.scale(image, (64, 64)).convert() #Изменение размера картинки
    except any:
        print("Ошибка загрузка изображения:", image_file_name)
        raise SystemExit()
    return image


bg = load_image('bg.png')

tree = load_image('tree_9.png')
for x in range(4):
    for y in range(3):
        screen.blit(bg, (x*256, y*256))

screen.blit(tree, (126, 200))

pygame.init()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
