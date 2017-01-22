import pygame

pygame.init()

displaySize = (1024,768)
display = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Aquarium")

fpsClock = pygame.time.Clock()

# load ressources
backGround_raw = pygame.image.load("underwater.jpg").convert()
backGround = pygame.transform.scale(backGround_raw, displaySize)

fish_raw = pygame.image.load("fish.png").convert_alpha()
fish = pygame.transform.scale(fish_raw, (200,150))

fish_position_x = -300
fish_position_y = 400

running = True
while running:
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == 27:
            running = False

    
    fish_position_x += 1
    
    display.blit(backGround,(0,0))
    display.blit(fish,(fish_position_x, fish_position_y))

    
    pygame.display.update()
    fpsClock.tick(60)

    
