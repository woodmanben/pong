import os
import time
import keyboard
import random as rand

width = 57
length = 11
game = True
end_message = "Classic"

class Paddle():
    def __init__(self, y = length // 2, scr = 0):
        self.y = y
        self.scr = scr
    def move_up(self):
        if self.y > 0:
            self.y -= 1
    def move_down(self):
        if self.y < length - 1:
            self.y += 1
    def score(self):
        self.scr += 1

class Ball():
    def __init__(self, x = width // 2, y = length // 2, x_vel = 1, y_vel = 1):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel

    def hit_paddle(self):
        self.x_vel = -1 * self.x_vel

    def hit_wall(self):
        self.y_vel = -1 * self.y_vel
         
player1 = Paddle()
player2 = Paddle()
ball = Ball()

while True:
    count = 0
    while game:
        if keyboard.is_pressed('q'):
            player1.move_up()
        if keyboard.is_pressed('a'):
            player1.move_down()
        if keyboard.is_pressed('o'):
            player2.move_up()
        if keyboard.is_pressed('l'):
            player2.move_down()
        if ball.x == 1:
            if ball.y in [player1.y - 1, player1.y, player1.y + 1]:
                ball.hit_paddle()
            else:
                player2.score()
                break
        if ball.x == width - 2:
            if ball.y in [player2.y - 1, player2.y, player2.y + 1]:
                ball.hit_paddle()
            else:
                player1.score()
                break
        if ball.y == 0 or ball.y == length - 1:
            ball.hit_wall()
        ball.x += ball.x_vel
        ball.y += ball.y_vel
        os.system("clear")
        print("=" * width)
        for i in range(length):
            if i == player1.y and i == player2.y and i == ball.y:
                print("|" + " " * (ball.x - 1) + "o" + " " * (width - ball.x - 2) + "|")
            elif i == player1.y and i == ball.y:
                print("|" + " " * (ball.x - 1) + "o" + " " * (width - ball.x - 1))
            elif i == player2.y and i == ball.y:
                print(" " * ball.x + "o" + " " * (width - ball.x - 2) +  "|")
            elif i == ball.y:
                print(" " * ball.x + "o" + " " * (width - ball.x - 1))
            elif i == player1.y and i == player2.y:
                print("|" + " " * (width - 2) + "|")
            elif i == player1.y:
                print("|" + " " * (width - 1))
            elif i == player2.y:
                print(" " * (width - 1) + "|")
            else:
                print(" ")
        print("=" * width)
        print(str(player1.scr) + " " * (width - 2) + str(player2.scr))
        time.sleep(0.05)

    os.system("clear")
    print("=" * width)
    for i in range(length):
        if i == length // 2:
            print(" " * ((width - len(end_message)) // 2) + end_message)
        else:
            print(" ")
    print("=" * width)
    print(str(player1.scr) + " " * (width - 2) + str(player2.scr))

    if player1.scr < 10 and player2.scr < 10:
        if input("Press any key when ready (ctrl z if you're done):"):
            player1 = Paddle(length // 2, player1.scr)
            player2 = Paddle(length // 2, player2.scr)
            ball = Ball(width // 2, length // 2, rand.randrange(-1, 2, 2), rand.randrange(-1, 2, 2))
            game = True
        else:
            break
    else:
        if player1.scr == 10:
            if input("Player 1 Wins! Press any key to restart (ctrl z if you're done):"):
                player1 = Paddle()
                player2 = Paddle()
                ball = Ball()
                game = True
            else:
                break
        else:
            if input("Player 1 Wins! Press any key to restart (ctrl z if you're done):"):
                player1 = Paddle()
                player2 = Paddle()
                ball = Ball()
                game = True
            else:
                break









