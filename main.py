from pygame import *

win_width = 800
win_height = 500

back = (200, 255, 255)
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
window.fill(back)
clock = time.Clock()

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))

lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

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
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed


racket1 = Player('raketka.png', 10, 250, 40, 150, 5)
racket2 = Player('raketka.png', 750, 250, 40, 150, 5)
ball = Player('tennis ball.png', 400, 250, 50, 50, 5)

game = True
fps = 60
finish = False
speed_x = 5
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
       ball.rect.x += speed_x
       ball.rect.y += speed_y
   
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            
    if ball.rect.y < 0 or ball.rect.y > win_height - 50:
        speed_y *= -1
    
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    
    if ball.rect.x > win_width - 50:
       finish = True
       window.blit(lose2, (200, 200))


    window.fill(back)
    racket1.reset()
    racket1.update()
    racket2.reset()
    racket2.update2()
    ball.reset()
    
    display.update()
    clock.tick(fps)
    

