import pgzrun
from random import randint

HEIGHT = 400
WIDTH = 400
score = 0
game_over = False
start = False

fox = Actor("fox")
coin = Actor("coin")
btnStart = Actor("start")

btnStart.pos = 200, 200
fox.pos = 100, 100
coin.pos = 200, 200

def draw():
    global start
    screen.fill("blue")
    if not start and not game_over:
        btnStart.draw()
    elif start:
        screen.fill("green")
        fox.draw()
        coin.draw()
        screen.draw.text("Score :" + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Score :" + str(score), color="black", topleft=(10, 10), fontsize=60)
        btnStart.draw()
        

def on_mouse_down(pos):
    global start, game_over, score
    if btnStart.collidepoint(pos) and not start:
        start = True
        game_over = False
        score = 0
        fox.pos = 100, 100
        place_coin()
        clock.schedule(time_up, 5.0)

def place_coin():
    coin.x = randint(20, (WIDTH-20))
    coin.y = randint(20, (HEIGHT-20))

def time_up():
    global game_over, start
    game_over = True
    start = False

def update():
    global score, start

    if start:
        if keyboard.left:
            fox.x = fox.x - 4
        elif keyboard.right:
            fox.x = fox.x + 4
        elif keyboard.up:
            fox.y = fox.y - 4
        elif keyboard.down:
            fox.y = fox.y + 4

        coin_colected = fox.colliderect(coin)

        if coin_colected:
            score = score+10
            place_coin()


place_coin()

pgzrun.go()