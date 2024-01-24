import sys
from settings import Settings
from point import *
from pygame.sprite import Group
from PAKU import Paku
from enemy import *

def time_function(enemy):
    enemy.weakness = False
    enemy.image = pygame.image.load('images/enemy.png')
    if enemy.horizontal == False:
        enemy.flip_image(horizontal = True)
    return enemy.weakness

def timer_respawn(enemy,paku):
    enemy.die = False
    if paku.rect.x > 400:
        enemy.rect.x = 30
        enemy.moving = True
        enemy.flip_image(horizontal=True)
    else:
        enemy.rect.x = 770
        enemy.moving = False


    return  enemy

def run_game():
    pygame.init()
    paku_settings = Settings()
    screen = pygame.display.set_mode((paku_settings.screen_width, paku_settings.screen_height))
    pygame.display.set_caption('PAKU')
    clock = pygame.time.Clock()
    points = Group()
    enemy = Enemy(screen)
    enemies = Group()
    enemies.add(enemy)
    paku = Paku(screen)
    pakues = Group()
    pakues.add(paku)
    TIMER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENT, 5000)
    clock = pygame.time.Clock()
    high_score = 0
    x = 0
    tickrate = 60

    while True:
        p = enemy.moving
        screen.fill(paku_settings.bg_color)
        pygame.draw.line(screen, (255, 255, 255), (0, 100), (800, 100), (3))
        pygame.draw.line(screen, (255, 255, 255), (0, 200), (800, 200), (3))
        pygame.draw.line(screen, (255, 255, 255), (0, 110), (800, 110), (3))
        pygame.draw.line(screen, (255, 255, 255), (0, 190), (800, 190), (3))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and paku.moving and paku_settings.game_status:
                    paku.moving = False 
                    paku.flip_image(horizontal = True)
                elif event.key == pygame.K_SPACE and not paku.moving and  paku_settings.game_status:
                    paku.moving = True
                    paku.flip_image(horizontal = True)
                elif event.key == pygame.K_ESCAPE and paku_settings.game_status:
                    paku_settings.game_status = 0
                elif event.key == pygame.K_ESCAPE and paku_settings.game_status == 0:
                    paku_settings.game_status = 1
            if event.type == TIMER_EVENT:
                if enemy.weakness:
                    time_function(enemy)
                if enemy.die:
                    timer_respawn(enemy, paku)

        points.draw(screen)
        pakues.draw(screen)
        enemies.draw(screen)
        if paku_settings.game_status:
            paku.update(enemy)
            enemy.update()
            colisions = pygame.sprite.groupcollide(pakues, points, False, True)
            colisions_enemy = pygame.sprite.groupcollide(pakues, enemies, False, False)
            if str(colisions_enemy) == '{<Paku Sprite(in 1 groups)>: [<Enemy Sprite(in 1 groups)>]}' and enemy.weakness == False:
                colisions = pygame.sprite.groupcollide(pakues, enemies, True, True)
                enemy = Enemy(screen)
                enemies.add(enemy)
                paku = Paku(screen)
                pakues.add(paku)
                points.empty()
                x = 0
                if high_score < paku_settings.point:
                    high_score = paku_settings.point
                paku_settings.point = 0
                paku_settings.game_status = 0
                tickrate = 60
            if str(colisions_enemy) == '{<Paku Sprite(in 1 groups)>: [<Enemy Sprite(in 1 groups)>]}' and enemy.weakness == True:
                colisions_enemy = pygame.sprite.groupcollide(pakues, enemies, False, True)
                enemy = Enemy(screen)
                enemy.rect.x =900
                enemies.add(enemy)
                enemy.die = True
                paku_settings.point += 10 * x
                x += 1
                tickrate += 5
            if str(colisions) != '{}':
                paku_settings.point += (1*x)
            if str(colisions) == "{<Paku Sprite(in 1 groups)>: [<Super_point Sprite(in 0 groups)>]}" and enemy.horizontal == True:
                enemy.weakness = True
                enemy.image = pygame.image.load('images/w_enemy.png')
                enemy.flip_image(horizontal = True)
            elif str(colisions) == "{<Paku Sprite(in 1 groups)>: [<Super_point Sprite(in 0 groups)>]}" and enemy.horizontal == False:
                enemy.weakness = True
                enemy.image = pygame.image.load('images/w_enemy.png')
        clock.tick(tickrate)

        if len(points) == 0:
            points_draw(screen, points, paku)
            x += 1
            tickrate += 5

        text = paku_settings.font.render(f'Score: {paku_settings.point}', True, (255, 255, 255))
        screen.blit(text, (10, 10))
        text = paku_settings.font.render(f' X : {x}', True, (255, 255, 255))
        screen.blit(text, (3, 30))
        text = paku_settings.font.render(f' High Score : {high_score}', True, (255, 255, 255))
        screen.blit(text, (393, 30))

        if paku_settings.game_status == 0:
            text = paku_settings.font.render(f'Prees Esc to Start / Continue', True, (255, 255, 255))
            screen.blit(text, (400, 10))
        pygame.display.flip()
        
run_game()