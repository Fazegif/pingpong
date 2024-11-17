from pygame import *
from random import *
from time import time as timer

window = display.set_mode((700, 500))
window.fill((100,100,100))
FPS = 60
game = True
clock = time.Clock()
finish = False
speed_x = 3
speed_y = 3
font.init()
font1 = font.SysFont(None, 36)

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
rocket1 = Player('7-157.jpg', 30, 150, 80, 80, 10)
rocket2 = Player('7-157.jpg', 570, 150, 80, 80, 10)
ball = GameSprite('images (2).jpg', 0, 0, 40, 40, 15)
finish = False

while game:
    window.fill((100,100,100))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        rocket1.update_l()
        rocket2.update_r()
        rocket1.reset()
        rocket2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *= -1
        if ball.rect.x < 0:
            text_lose1 = font1.render('PLAYER 1 LOST', 1, (255, 0, 0))
            window.blit(text_lose1, (250, 100))
        if ball.rect.x > 700:
            text_lose2 = font1.render('player 2 LOST', 1, (255, 0, 0))
            window.blit(text_lose2, (250, 100))
    clock.tick(FPS)
    display.update()
