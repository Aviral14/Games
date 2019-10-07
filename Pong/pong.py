from superwires import games, color

games.init(screen_width=1305, screen_height=629, fps=50)


class Ball(games.Sprite):
    time = 100
    tt = 0
    image = games.load_image("ball.png")

    def __init__(self):
        super(Ball, self).__init__(image=self.image, x=650, y=325,
                                   dx=4.5, dy=4.5)
        if Ball.time == 100:
            self.show_time = games.Text(value=Ball.time, size=40,
                                        color=color.red, x=652.5, y=35)
            games.screen.add(self.show_time)

    def update(self):
        if self.bottom > games.screen.height or self.top < 62:
            self.dy = -self.dy
        if self.right > games.screen.width:
            p1.score.value += 10
            p1.score.x -= 1
            self.x = 650
            self.y = 325
        if self.left < 0:
            p2.score.value += 10
            p2.score.x -= 1
            self.x = 650
            self.y = 325

        if Ball.time != 0:
            Ball.tt += 1
        self.check_time()

    def end_game(self):
        self.dy = 0
        self.dx = 0
        if p1.score.value > p2.score.value:
            self.win_message = games.Message(value="Player 1 Won!!!", size=200,
                                             color=color.red, x=640, y=250,
                                             lifetime=5000,
                                             after_death=games.screen.quit())
            games.screen.add(self.win_message)
        elif p2.score.value > p1.score.value:
            self.win_message = games.Message(value="Player 2 Won!!!", size=200,
                                             color=color.red, x=640, y=250,
                                             lifetime=5000,
                                             after_death=games.screen.quit())
            games.screen.add(self.win_message)
        else:
            self.win_message = games.Message(value="Game Tied!!!", size=200,
                                             color=color.red, x=640, y=250,
                                             lifetime=5000,
                                             after_death=games.screen.quit())
            games.screen.add(self.win_message)

    def handle_caught(self, change):
        self.dx = -self.dx
        self.dy += change

    def check_time(self):
        if Ball.tt == 50:
            Ball.time -= 1
            self.show_time.value -= 1
            Ball.tt = 0
        if Ball.time == 0:
            self.end_game()


class Bar(games.Sprite):

    def __init__(self, pos, scorex, images, a, b):
        super(Bar, self).__init__(image=images, y=games.screen.height/2, x=pos)
        self.score = games.Text(value=0, size=60, color=color.black,
                                x=scorex, y=35)
        games.screen.add(self.score)
        self.change = 0
        self.key = 0
        self.t = a
        self.g = b

    def update(self):
        if games.keyboard.is_pressed(self.g):
            self.y += 8
            self.key = 1
        elif games.keyboard.is_pressed(self.t):
            self.y -= 8
            self.key = -1
        else:
            self.key = 0
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height
        if self.top < 62:
            self.top = 62
        self.check_caught()

    def check_caught(self):
        for ball in self.overlapping_sprites:

            if ball.dy*self.key > 0:
                self.change = -3
            elif ball.dy*self.key < 0:
                self.change = +3
            else:
                self.change = 0
            ball.handle_caught(self.change)


bg_image = games.load_image("bg.png", transparent=False)
games.screen.background = bg_image


text1 = games.Text(value="Player-1(W,S)", size=40, color=color.red, x=0, y=35)
text1.left = 0
games.screen.add(text1)
text2 = games.Text(value="Player-2(up,down)", size=40, color=color.red,
                   x=613, y=35)
text2.left = 800
games.screen.add(text2)

image1 = games.load_image("bar.png", transparent=False)
image2 = games.load_image("bar.png", transparent=False)
p1 = Bar(pos=0, scorex=350, images=image1, a=games.K_w, b=games.K_s)
p1.left = 0
games.screen.add(p1)
p2 = Bar(pos=games.screen.width, scorex=1175, images=image2, a=games.K_UP,
         b=games.K_DOWN)
p2.right = games.screen.width
games.screen.add(p2)

ball = Ball()
games.screen.add(ball)

games.screen.mainloop()
