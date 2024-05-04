import pygame
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618,359))
pygame.display.set_caption("First Game")

icon = pygame.image.load('mygame/console_icon.png')

pygame.display.set_icon(icon)

back_gr = pygame.image.load('mygame/back_gr.png').convert_alpha()

walk_right = [pygame.image.load('mygame/player_move/right1.png').convert_alpha(),
              pygame.image.load('mygame/player_move/right2.png').convert_alpha(),
              pygame.image.load('mygame/player_move/right3.png').convert_alpha(),
              pygame.image.load('mygame/player_move/right4.png').convert_alpha(),]


walk_left = [pygame.image.load('mygame/player_move/left4.png').convert_alpha(),
              pygame.image.load('mygame/player_move/left3.png').convert_alpha(),
              pygame.image.load('mygame/player_move/left2.png').convert_alpha(),
              pygame.image.load('mygame/player_move/left1.png').convert_alpha(),]


enemy = pygame.image.load('mygame/roomba.png').convert_alpha()

devil_list_in_game = []

game_sound = pygame.mixer.Sound('mygame/mario.mp3')
game_sound.play()

player_anim_count = 0

player_Speed = 5
player_x = 150
player_y = 250
back_x = 0
is_jump = False
jump_count = 10

devil_timer = pygame.USEREVENT + 1
pygame.time.set_timer(devil_timer,3000)

label = pygame.font.Font('mygame/leter.ttf',45)
lose_laber = label.render("You Lose! ",False,('white')) 
restart_label = label.render("Restart ",False,('green'))
rest_label = restart_label.get_rect(topleft=(210,200))
bullet = pygame.image.load('mygame/bullet.png').convert_alpha()
enemy_count = 0
enemy_speed = 30
bullets_left = 5
bullets = []
gameplay = True

running = True
while running:
    


    clock.tick(enemy_speed)
    
    screen.blit(back_gr,(back_x,0))
    screen.blit(back_gr,(back_x + 618,0))

    if gameplay:

        player_rect = walk_left[0].get_rect(topleft = (player_x,player_y))

        if devil_list_in_game:
            
            for (i ,el) in enumerate(devil_list_in_game):
                screen.blit(enemy,el)
                el.x -= 10
                

                if el.x < -10:
                    devil_list_in_game.pop(i)
                    enemy_count += 1
                    if enemy_count % 2 == 0:
                        enemy_speed += 5

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 25:
            player_x -= player_Speed

        elif keys[pygame.K_RIGHT] and player_x < 359:
            player_x += player_Speed


        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
                game_sound = pygame.mixer.Sound('mygame/jump.mp3')
                game_sound.play()
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y  -= (jump_count**2) / 2
                else:
                    player_y  += (jump_count**2) / 2
                jump_count -= 1 
            else:
                is_jump = False
                jump_count = 10



        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[int(player_anim_count)],(player_x,player_y))
        else:
            screen.blit(walk_right[int(player_anim_count)],(player_x,player_y))

        if player_anim_count >= 3:

            player_anim_count = 0
        else:
            player_anim_count += 0.25

        back_x -= 2

        if back_x == -618:
            back_x = 0

        
        if bullets:
            for (i,bul) in enumerate(bullets):
            
                screen.blit(bullet,(bul.x,bul.y))
                bul.x += 4

                if bul.x > 630:
                    bullets.pop(i)



                if devil_list_in_game:
                    for(index,devils) in enumerate(devil_list_in_game):
                        if bul.colliderect(devils):
                            devil_list_in_game.pop(index)
                            bullets.pop(i)

    else:
        screen.fill(('black'))
        screen.blit(lose_laber,(199,140))
        screen.blit(restart_label,rest_label)

        mouse = pygame.mouse.get_pos()

        if rest_label.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 120
            devil_list_in_game.clear()
            bullets_left = 5




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
        if event.type == devil_timer:
            devil_list_in_game.append(enemy.get_rect(topleft=(620,250)))
        
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT and bullets_left > 0:

            bullets.append(bullet.get_rect(topleft =(player_x + 30,player_y+10)))
            bullets_left -= 1 



print(enemy_count)