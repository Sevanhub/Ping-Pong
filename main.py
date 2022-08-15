from pygame import *

win_width = 800
win_height = 500

back = (200, 255, 255)
mw = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
mw.fill(back)
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
     
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
      
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 485:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        pass





game = True
fps = 60

while True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(fps)
    

