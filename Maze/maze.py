#Модули
from pygame import *
font.init()

#Окно игры
clock = time.Clock()
FPS =65 
x1 = 550
y1 = 350
x2 = 150
y2 = 350
step = 10
window = display.set_mode((1000, 500))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (1000, 500))

#Классы
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
     def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 10
        if keys_pressed[K_s]:
            self.rect.y += 10
        if keys_pressed[K_d]:
            self.rect.x += 10
        if keys_pressed[K_a]:
            self.rect.x -= 10

class Enemy(GameSprite):
    direction = 'left'
    a = "right"  
    def update(self):  
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction != "left":
            self.rect.x += self.speed
        if self.rect.x >= 800:
            self.direction = "left"
        if self.rect.x <= 400:
            self.direction = "right"

class Wall(sprite.Sprite):
        def __init__(self, color_1, color_2, color_3, wall_x, wall_y, widht, height):
            super().__init__()
            self.color_1 = color_1
            self.color_2 = color_2
            self.color_3 = color_3
            self.width = widht
            self.height = height
            self.image = Surface((self.width, self.height))
            self.image.fill((color_1, color_2, color_3))
            self.rect = self.image.get_rect()
            self.rect.x = wall_x
            self.rect.y = wall_y
        def draw_wall(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
        
#Объекты
Wizard = Player("Wizard.png", 150, 350, 5 )
Rogue = Enemy("Rogue.png", 550, 350, 5 ) 
Portal =  GameSprite("Portal.png", 880, 380, 0)
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('GAME OVER!', True, (255, 215, 0))
W1 = Wall(70, 130, 180, 500, 200, 200, 20)
W2 = Wall(70, 130, 180, 200, 130, 20, 200)
W3 = Wall(70, 130, 180, 50, 10, 20, 400)
W4 = Wall(70, 130, 180, 850, 350, 200, 20)

#Игровой цикл
game = True
finish = False
while game:
    clock.tick(FPS)
    

    display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0)) 
        Wizard.update()
        Rogue.update()

        Wizard.reset()
        Rogue.reset()
        Portal.reset()

        W1.draw_wall()
        W2.draw_wall()
        W3.draw_wall()
        W4.draw_wall()

        if sprite.collide_rect(Wizard, Portal):
            window.blit(win,(255, 215)) 
            finish = True
        if sprite.collide_rect(Wizard, Rogue):
            window.blit(lose,(255, 215)) 
            finish = True
        if sprite.collide_rect(Wizard, W1):
            window.blit(lose,(255, 215)) 
            finish = True
        if sprite.collide_rect(Wizard, W2):
            window.blit(lose,(255, 215)) 
            finish = True
        if sprite.collide_rect(Wizard, W3):
            window.blit(lose,(255, 215)) 
            finish = True
        if sprite.collide_rect(Wizard, W4):
            window.blit(lose,(255, 215)) 
            finish = True

        




