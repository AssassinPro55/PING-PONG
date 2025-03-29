from pygame import *

# Создание и настройка окна
W = 700
H = 500

window = display.set_mode((W, H))
display.set_caption('Пинг понг')
background = (204, 117, 55)
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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < H - 60:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < H - 60:
            self.rect.y += self.speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Текст

player = Player('Player.png', 0, 0, 85, 85, 8)
monster = Enemy('Bot.png', 0, 700, 85, 85, 8)

####### 

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(background)
        player.update()
        monster.update()

        player.reset()
        monster.reset()
    
    display.update()
    clock.tick(FPS)
















    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall1 = Wall(131, 240, 6, 100, 20, 450, 10)
wall2 = Wall(131, 240, 6, 100, 240, 450, 10)
wall3 = Wall(131, 240, 6, 100, 240, 10, 450)



mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

# Текст
font.init()
font = font.Font(None, 70)
win = font.render('YOU SIGMA!', True, (255, 215, 0))
lose = font.render("YOU LOX!(((", True, (180, 0, 0))

player = Player('hero.png', 5, H - 80, 4)
monster = Enemy('cyborg.png', W - 80, 280, 6)
final = GameSprite('treasure.png', W - 120, H - 80, 0)


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

        if (sprite.collide_rect(player, monster) or
        sprite.collide_rect(player, wall1) or
        sprite.collide_rect(player, wall2) or
        sprite.collide_rect(player, wall3)):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
            

