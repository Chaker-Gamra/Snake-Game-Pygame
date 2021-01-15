from gameObjects import *

pygame.init()

screen = pygame.display.set_mode((500, 500))
bg = pygame.image.load("BackGround.png")
clock = pygame.time.Clock()
font = pygame.font.SysFont('tahoma', 32)

game_over_sound = pygame.mixer.Sound("game_over.wav")
apple = Apple()
snake = Snake(250, 250)

BLACK = (0, 0, 0)
RED = (255, 0, 0)

running = True
game_over = False

while running:
    # Check For Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snake.motion[1] == 0:
                snake.motion = [0, 1]
            elif event.key == pygame.K_UP and snake.motion[1] == 0:
                snake.motion = [0, -1]
            elif event.key == pygame.K_LEFT and snake.motion[0] == 0:
                snake.motion = [-1, 0]
            elif event.key == pygame.K_RIGHT and snake.motion[0] == 0:
                snake.motion = [1, 0]

    # Update
    snake.update(apple)
    if snake.hit_itself():
        game_over = True
        game_over_sound.play()

    # Render
    screen.blit(bg, bg.get_rect())
    apple.render(screen)
    snake.render(screen)
    screen.blit(font.render('Score: '+ str(snake.score), True, (0,0,0)), (10,5))
    pygame.display.update()
    clock.tick(10)

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                    apple = Apple()
                    snake = Snake(250, 250)
                if event.key == pygame.K_q:
                    running = False
                    game_over = False

        # Update

        # Render
        screen.blit(bg, bg.get_rect())
        apple.render(screen)
        snake.render(screen)
        screen.blit(font.render('Score: ' + str(snake.score), True, BLACK), (10, 5))
        screen.blit(font.render('Game Over', True, RED), (150, 250))
        screen.blit(font.render('Press r To Replay or q To Quit', True, BLACK), (40, 200))
        pygame.display.update()
        clock.tick(10)

pygame.quit()
