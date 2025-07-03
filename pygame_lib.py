import pygame

# init
pygame.init()

#display
panjang = 500
lebar = 500
window = pygame.display.set_mode((panjang, lebar))

#object
#posisi
x = 250
y = 250

#ukuran
panjang_object = 25
lebar_object = 25

#kecepatan
speed = 1


is_run = True
while is_run:
    # user input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False

    #input keyboard press
    keys = pygame.key.get_pressed()

    #geser
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    if keys[pygame.K_RIGHT] and x < lebar - lebar_object:
        x += speed

    if keys[pygame.K_DOWN] and y < panjang - panjang_object:
        y += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed
    # update assets
    window.fill((255,255,255))
    pygame.draw.rect(window, (0,0,255),(x,y,panjang_object,lebar_object))
    # render dispaly
    pygame.display.update()
pygame.quit()

