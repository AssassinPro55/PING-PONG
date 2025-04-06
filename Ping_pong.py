from pygame import *

# Создание и настройка окна
W = 900
H = 500

window = display.set_mode((W, H))
display.set_caption('Пинг понг')
background = (35, 115, 33)
window.fill(background)

FPS = 60
clock = time.Clock()

# Классы

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < H - 60:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < H - 60:
            self.rect.y += self.speed

class Ping_Ball(GameSprite):
    def update(self):
        pass
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Текст

player1 = Player1('Player.png', 0, H//2, 85, 85, 8)
player2 = Player2('Bot.png', 820, H//2, 85, 85, 8)
ball = Ping_Ball('Ball.png', W//2, H//2, 60, 60, 0)

#Музыка

mixer.init()
mixer.music.load('blinding-lights.ogg')
mixer.music.play()
mixer.music.set_volume(0.2)

kick = mixer.Sound('Ydar.ogg')

#Текст
font.init()
font = font.Font(None, 250)
win_Player_1 = font.render('Player 1 WINS!!!', True, (190, 204, 35))
win_Player_2 = font.render("Player 2 WINS!!!", True, (190, 204, 35))

#Игровой цикл

speed_x = 5
speed_y = 5

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if (sprite.collide_rect(player1, ball)) or (sprite.collide_rect(player2, ball)):
        kick.set_volume(0.1)
        kick.play()

    if finish != True:
        window.fill(background)

        ball.rect.y += speed_y
        ball.rect.x += speed_x
        
        player1.update()
        player2.update()
        ball.update()

        player1.reset()
        player2.reset()
        ball.reset()

        #Отскок

        if ball.rect.y > H-50 or ball.rect.y < 0:
            speed_y += -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x += -1
            speed_y += 1
    
    display.update()
    clock.tick(FPS)




            
