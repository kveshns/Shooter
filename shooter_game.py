#Создай собственный Шутер!

from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale( image.load("galaxy.jpg"), (700, 500) )
game = True 
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")
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
    
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
    def fire(self):
            bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15 , 20 , -15)
            bullets.add(bullet)
score = 0    
lost = 0
kill = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost 
        if self.rect.y > 500:
            self.rect.x = randint(80,620)
            self.rect.y = 0
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()
font.init()
font1 = font.SysFont('Arial', 36)
font = font.SysFont('Arial', 40)
text_win = font1.render("WIN", True, (255,215,0))
text_loser = font1.render("LOSE", True, (255,215,0) )



for i in range (1,6):
    monster = Enemy('ufo.png', randint(80,620),0, 65,65, randint(2,3))
    monsters.add(monster)

for i in range (1, 3):
    asteroid = Enemy('asteroid.png', randint(80,620), 0 , 65,65, randint(1,2))
    asteroids.add(asteroid)
player = Player('rocket.png', 100, 400, 65 , 65, 5)
clock = time.Clock()
fps = 100
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False   
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire() 
    if not finish:
        window.blit(background,(0,0))
        player.reset()
        player.update()
        monsters.update()
        bullets.update()
        asteroids.update()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)
        text_lose = font1.render("Пропушено:" + str(lost), 1 , (255,255,255))
        text_kill = font1.render("Счет:" + str(score), 1 , (255,255,255))
        window.blit(text_lose ,(10,50))
        window.blit(text_kill, (10,10))
        collides = sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(80,620),0, 65,65, randint(1,2))
            monsters.add(monsetr)
        if score >= 10:
            finish = True
            window.blit(text_win,(200,200))
        if sprite.spritecollide(player,monsters,False) or sprite.spritecollide(player,asteroids,False) or lost >=25:
            finish = True
            window.blit(text_loser,(200,200))
    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        for a in asteroids:
            a.kill()
        clock.tick(60)
        for i in range(1,6):
            monster = Enemy("ufo.png", randint(80, 700 - 80,), -40, 80, 50, 2)
            monsters.add(monster)
        for i in range (1, 3):
            asteroid = Enemy('asteroid.png', randint(80,620), 0 , 65,65, randint(1,2))
            asteroids.add(asteroid)
    display.update()

clock.tick(fps)
