import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
bg = pygame.image.load("BackGround.png")
running = True

while running:
    # Check For Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Render
    screen.blit(bg, bg.get_rect())
    pygame.display.update()

pygame.quit()