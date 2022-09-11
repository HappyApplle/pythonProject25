from pygame import *

window = display.set_mode((500, 500))
display.set_caption('пинг понг')
window.fill((1,50,50))

font.init()

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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

ball = GameSprite('ball.png', 200, 300, 50, 50, 10)
platform_1 = Player('platform.png', 100, 300, 30, 100, 10)
platform_2 = Player('platform.png', 400, 300, 30, 100, 10)

speed_x = 3
speed_y = 3

font_1 = font.Font(None, 35)
lose_left = font_1.render('ЛЕВЫЙ ИГРОК ПРОИГРАЛ!', True, (0,0,0))
lose_right = font_1.render('ПРАВЫЙ ИГРОК ПРОИГРАЛ!', True, (0,0,0))

clock = time.Clock()
FPS = 60

game = True
while game:
    window.fill((1, 50, 50))
    ball.reset()
    platform_1.reset()
    platform_1.update_r()
    platform_2.reset()
    platform_2.update_l()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y < 0 or ball.rect.y > 450:
        speed_y *= -1
    if sprite.collide_rect(ball, platform_1):
        speed_x *= -1
    if sprite.collide_rect(ball, platform_2):
        speed_x *= -1
    if ball.rect.x > 450:
        window.blit(lose_right, (50,200))
    if ball.rect.x < 0:
        window.blit(lose_left, (50, 200))
    for e in event.get():
        if e.type == QUIT:
            exit()

    display.update()
    clock.tick(FPS)
