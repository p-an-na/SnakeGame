import random
import pygame

pygame.init()

dis_size = 500
snake_color = (252, 152, 3)
snake_block = 10
snake_speed = 10
black = (0, 0,0)
red = (255, 0 ,0)
blue = (0,0,255)
yellow = (255,255, 102)
font_style = pygame.font.SysFont('arial', 20)

dis = pygame.display.set_mode((dis_size,dis_size))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()



def gameLoop():

    game_close = False
    game_over = False

    x1 = dis_size / 2
    y1 = dis_size / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_size - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_size - snake_block) / 10.0) * 10.0


    while not game_close:
        while game_over == True:
            dis.fill(black)
            message('Game over! Press A-Quit or C-Play Again', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                    game_over = False
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_close=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_size or  x1 < 0 or y1 >= dis_size or y1 <0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]


        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        our_snake(snake_block, snake_list)
        score_player(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_size - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_size - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)



    pygame.quit()
    quit()


def score_player(score):
    value = font_style.render('Score: ' + str(score), True, yellow)
    dis.blit(value, [0,0])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])
def message(msg,color):
    msg = font_style.render(msg,True, color)
    dis.blit(msg, [dis_size/6, dis_size/3])