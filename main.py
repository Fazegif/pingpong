from pygame import *
from random import *
from time import time as timer

window = display.set_mode((700, 500))
window.fill((100,100,100))
FPS = 60
game = True
clock = time.Clock()
finish = False

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
    def update_r(self):
        keys = key.het_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,15,20, 5)
        bullets.add(bullet)
    

while game:
    clock.tick(FPS)
    display.update()