import pygame  

game_height = 600
game_width = 600

paddle_height = 50
paddle_width = game_width/2.5

paddle_space = 10
displacement = 1

player_1_color = (106,90,205)
player_2_color = (176,224,230)
ball_color = (255,255,255)

p1_x =(game_width - paddle_width)/2
p2_x = (game_width - paddle_width)/2

ball_size = 20

player_2_ball_y = paddle_space + paddle_height + ball_size
player_1_ball_y = game_height - paddle_space - paddle_height - ball_size

ball_x = (game_width)/2
ball_y = player_2_ball_y

ball_speed = 1

ball_x_displacement = ball_speed
ball_y_displacement = ball_speed

pygame.init()  
screen = pygame.display.set_mode((game_height,game_width))  
done = False 
playing = False


while not done:  
    #pygame.time.delay(1000)
    screen.fill((0,0,0))

    player_1_rect = (p1_x,game_height - paddle_height - paddle_space, paddle_width, paddle_height) #x, y, width, height
    player_2_rect = (p2_x, paddle_space, paddle_width, paddle_height) #x, y, width, height

    pygame.draw.rect(screen,player_1_color,player_1_rect)
    pygame.draw.rect(screen,player_2_color,player_2_rect)
    pygame.draw.circle(screen,ball_color,(ball_x,ball_y), ball_size, 5)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True 

    keys = pygame.key.get_pressed()
    #Player1 Movement
    if keys [pygame.K_LEFT] and (game_width - p1_x) < game_width:
        p1_x -= displacement
    if keys [pygame.K_RIGHT] and (game_width - p1_x) > paddle_width:
        p1_x += displacement

    #Player2 Movement
    if keys [pygame.K_a] and (game_width - p2_x) < game_width:
        p2_x -= displacement
    if keys [pygame.K_d] and (game_width - p2_x) > paddle_width:
        p2_x += displacement

    # Start game
    if keys [pygame.K_SPACE]:
        ball_x = (game_width)/2
        ball_y = player_2_ball_y
        p1_x = p2_x =(game_width - paddle_width)/2
        playing = True
    
    # Restart
    
    if not playing:
        pygame.display.flip()
        continue
    
    # ----- Ball Logic ------- #

    # Paddle logic
    within_pd1x_range = ball_x >= p1_x and ball_x <= p1_x + paddle_width # Directly above Paddle 1
    within_pd1x_range = within_pd1x_range and ball_y >= player_1_ball_y

    hit_paddle1_left = ball_x >= p1_x and ball_x <= p1_x + paddle_width/2

    within_pd2x_range = ball_x >= p2_x and ball_x <= p2_x + paddle_width # Directly above Paddle 2
    within_pd2x_range = within_pd2x_range and ball_y <= player_2_ball_y

    hit_paddle2_left = ball_x >= p2_x and ball_x <= p2_x + paddle_width/2

    # Logic for left wall
    hit_left = ball_x <= 0

    # Logic for right wall
    hit_right = ball_x >= game_width

    # Logic for upper and Lower wall
    p1_miss = ball_y >= (game_height - paddle_space)
    p2_miss = ball_y <= paddle_space

    #Ball hits paddle 1
    if within_pd1x_range:
        ball_y_displacement = -ball_speed
        if hit_paddle1_left:
             ball_x_displacement = -ball_speed
        else:
            ball_x_displacement = ball_speed

    #Ball hits paddle 2
    if within_pd2x_range:
        ball_y_displacement = ball_speed
        if hit_paddle2_left:
             ball_x_displacement = +ball_speed
        else:
            ball_x_displacement = -ball_speed
    
    #Ball hits wall
    if hit_left:
        ball_x_displacement = ball_speed
    elif hit_right:
        ball_x_displacement = -ball_speed
    
    if p1_miss or p2_miss:
        ball_x_displacement = 0
        ball_y_displacement = 0
    
    ball_x += ball_x_displacement
    ball_y += ball_y_displacement

    pygame.display.flip() 