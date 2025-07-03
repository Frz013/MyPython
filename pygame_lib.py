import pygame

# init
pygame.init()

#display
panjang = 500
lebar = 500
window = pygame.display.set_mode((panjang, lebar))

# user input
is_run = True
while is_run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False
pygame.quit()

# update assets
# render dispaly