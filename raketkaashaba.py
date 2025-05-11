
from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
game = True 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, cord, cord1, size_x, size_y, speed1):
        super().__init__()
        self.image = transform.scale( image.load(player_image), (size_x, size_y) )
        self.speed = speed1
        self.rect = self.image.get_rect()
        self.rect.x = cord
        self.rect.y = cord1
    def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.x < 595:
            self.rect.x += self.speed

    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 595:
            self.rect.x += self.speed

for i in range (1):
    Raketka = Raketka('Raketka.png', 1)
    monsters.add(Raketka)

player = Player_1('ashab.png', 100, 400, 65 , 65, 5)
player_2 = Player_1('ashab.png', 100, 400, 65 , 65, 5)
Raketka = Raketka('Raketka', 100, 400, 65 , 65, 5)

clock = time.Clock()
fps = 100
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False   
    if not finish:
        window.blit(background,(0,0))
        player.reset()
        player.update()
        Raketka.update()
        Raketka.draw(window)
        text_lose = font1.render("LOSE!" + str(lost), 1 , (255,255,255))
        window.blit(text_lose ,(10,50))
        collides = sprites_list = sprite.groupcollide(Raketka, True, True)
        for c in collides:
            score += 1
            Raketka = Enemy('Raketka.png', randint(80,620),0, 65,65, randint(1,2))
            Raketka.add(Raketka)
    else:
        finish = False




clock.tick(fps)