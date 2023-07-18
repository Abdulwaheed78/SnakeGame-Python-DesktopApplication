#  importing required modules
import pygame
import random
import button

# initialising screen
pygame.mixer.init()
pygame.init()

# definig Colors variables which are used in game
green = (0, 128, 0)
white = (255, 255, 255)
red = (194, 23, 23)
black = (0, 0, 0)
blue = (0, 0, 255)
brown = (165, 42, 42)
yellow = (255, 255, 0)
main = (64, 224, 208)

# another variable which defines snake initial  direction
direction = 'right'

# defining height and wisth of screen or Creating game  window
screen_width = 500  # screen x-axis
screen_height = 400  # screen y-axis

# function to display game screen
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# loading bdground images which  used in the game
bgimg= pygame.image.load("bg1.jpg").convert_alpha()

bgimg2 = pygame.image.load("bg2.png").convert_alpha()

bgimg3 = pygame.image.load("bg3.png").convert_alpha()

bgimg4 = pygame.image.load("bg4.png").convert_alpha()



# loading button images used in game
start_img = pygame.image.load('start_btn.png').convert_alpha()

exit_img = pygame.image.load('exit_btn.png').convert_alpha()

# loading snake parts
img = pygame.image.load('head.png') # snake mouth
Appleimg = pygame.image.load('food.png') # food


# create button instances defined outside of main file
start_button = button.Button(160, 300, start_img, 0.265)
exit_button = button.Button(260, 300, exit_img, 0.3)


# defining snake game caption
pygame.display.set_caption("THE SNAKE GAME")  # this statement is used to   write a heading in the top of game screen
pygame.display.update()  # in this statement updating screen status time to time
clock = pygame.time.Clock()


#defining fonts with different sizes

smallfont = pygame.font.SysFont("comicsansms", 12)
mediumfont = pygame.font.SysFont("comicsansms", 24)
largefont = pygame.font.SysFont("comicsansms", 40)


# definig text screen to show the text on  the game screen

def text_screen(text,color, x, y , size):
    if size=="small":
       screen_text = smallfont.render(text, True, color )
    if size=="medium":
       screen_text = mediumfont.render(text, True, color )
    if size=="large":
       screen_text = largefont.render(text, True, color )
    gameWindow.blit(screen_text, [x, y])


# defining function to plot the snake on main loop

# noinspection PyGlobalUndefined
def plot_snake(gameWindow, color, snk_list, snake_size):
    global head
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)


# show the image on the place of sake head in initial position when game starts

    gameWindow.blit(head, (snk_list[-1][0], snk_list[-1][1]))
    for x,y in snk_list[:-1]:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# defining fuction to pause the screen and showing events
def pause():
    True
    paused =True
    while paused:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
               True
               quit()

        gameWindow.fill(white)
        gameWindow.blit(bgimg3, (0, 0))


        text_screen("Click Start To Continue ", white, 185, 200, size="small")
        text_screen(" OR  ", white, 240, 230,size="small")
        text_screen("Click Exit To Quit Game ", white, 185, 260, size="small")


        if start_button.draw(gameWindow):# it checks if user click start button the it redirect to gameloop() functio
             paused=False

        elif exit_button.draw(gameWindow): # it checks if user click exit button then it redirect to exit the game
            True
            quit()

        pygame.display.update()
        clock.tick(30)



# defining welcome screen when user start game this window will appear first or it is a start screen  of a game

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgimg, (0, 0)) # in this statement we will showing the image as a baground of a screen

        # in this section we will showing text on the screen with different font sizes
        text_screen("Welcome To Snake Game   ", white, 15, 50 , size="large")
        text_screen(" Rules: ", white, 10, 140, size="medium")
        text_screen("1.  don't hit a wall", white, 15, 180, size="small")
        text_screen("2.  don't bite your own tail", white, 15, 200, size="small")
        text_screen("3.  use(left,right) keys to move snake in left,right directions", white, 15, 220, size="small")
        text_screen("4. use(up,down) keys to move snake in up,down directons ", white, 15, 240, size="small")


        # this is the event section of welcome() function
        if start_button.draw(gameWindow):
            gameloop()
        elif exit_button.draw(gameWindow):
            exit_game = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        pygame.display.update()
        clock.tick(30)


#  definig the main game loop()
# in this main section all the classes and functions are executed
# this is the main part of a game

def gameloop():
    global direction # this is the global variable


    #  these all are the Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 10
    velocity_y = 0
    snk_list = []
    snk_length = 1   # initial length of snake

    # below code check if  hiscore .txt file is present in system or not
    #  if not present then it create a .txt file with a name of  hiscore
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0    # this is the initial score
    init_velocity = 5
    snake_size = 20
    fps = 20

    # if game is started then this loop will  executed
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            # text_screen(" message to show on sscreen !", color, x-axis, y-axis)
            gameWindow.fill(black)
            gameWindow.blit(bgimg4, (0, 0))
            text_screen("Score: " + str(score), white, 175, 200, size="medium")
            text_screen("Highscore:" + str(hiscore), white, 175, 250, size="medium")


            if start_button.draw(gameWindow):
                gameloop()

            elif exit_button.draw(gameWindow):

                pygame.mixer.music.load('click.mp3')
                pygame.mixer.music.play()
                exit_game = True

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

              #  this is the main event section of a game where all keys  are defined
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:  # this is for right key is pressed
                    if event.key == pygame.K_RIGHT:
                        direction = 'right'
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT: # this is for left key is pressed
                        direction = 'left'

                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:   # this is for up key is pressed
                        direction = 'up'

                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:     # this is for down key is pressed
                        direction = 'down'

                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:      # this is the cheat or hack  kay to increase score without eating food
                        score += 10
                    if event.key == pygame.K_SPACE:   # here this is the kay of pause game funtion
                        pause()
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:

                pygame.mixer.music.load('click.mp3')  # here loading the music when snake eating food
                pygame.mixer.music.play()
                score += 10    # # here loading the music when snake
                               # eated a  food  length of snake is increased by 10 px
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(black)
            gameWindow.blit(bgimg2, (0, 0))
            text_screen("score: " + str(score), white, 5, 10, size="medium")
            text_screen("Highscore:" + str(hiscore), white, 200, 10, size="medium")
            text_screen("Press Space To Pause The Game ", white, 150, 340, size="small")
            fps=30


            # pygame.draw.rect(gameWindow, black,[food_x, food_y, snake_size, snake_size])
            gameWindow.blit(Appleimg, (food_x, food_y))
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]


            # if snake touch  his body itself then game over funtion is triggered
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()

             # this is the functon to plat the snake body
            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()