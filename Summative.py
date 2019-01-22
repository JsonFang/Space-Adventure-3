"""
Author: Jason Fang
Date: June 1, 2017
Description: The game is called "Space Adventure 3" and is a two player game. 
Players rack up score when they kill enemy aliens and will freeze if they fall 
below a certain score (-1000). Players will be able to unfreeze each other (and 
gain points for doing so) via bullets but only as many times as their life count 
will allow them. At the end there will be a boss and the player with the most 
points at the end wins.
"""

# I - IMPORT AND INITIALIZE
import pygame, SummativeSprites, random
pygame.init()
pygame.mixer.init()
     
def instructions():
    '''This function defines the "instructions" for my game.'''
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Instructions")    
    exit = False
    instructions = pygame.image.load("instructions.png").convert() 
    screen.blit(instructions, (0,0))
    pygame.display.flip()
    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                exit = True
                
def main():
    '''This function defines the 'mainline logic' for my game.'''  
    # DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Space Adventure 3!")
    # ENTITIES
    background = pygame.image.load("spacebackground.jpg")
    background = background.convert()
    screen.blit(background, (0, 0)) 
    player1 = SummativeSprites.Player(screen, 1)
    player2 = SummativeSprites.Player(screen, 2)
    boss =  SummativeSprites.Boss(screen)
    bossHealth = SummativeSprites.BossHealth(screen)
    bulletGroup = pygame.sprite.Group()
    bulletGroup2 = pygame.sprite.Group()
    bulletGroup3 = pygame.sprite.Group()
    score_keeper = SummativeSprites.ScoreKeeper()
    playerHealth1 = SummativeSprites.PlayerHealth1(screen)
    playerHealth2 = SummativeSprites.PlayerHealth2(screen)
    space = SummativeSprites.Space(screen)
    explosions = pygame.sprite.Group()
    allSprites = pygame.sprite.Group(space, score_keeper, playerHealth1, playerHealth2, player1, player2, bulletGroup, bulletGroup2, boss, explosions)    
    
    #FIRST ALIEN GROUP, LARGER THAN THE REST AND MORE CENTERED
    alienGroup = pygame.sprite.Group()
    value = random.randrange(5,10)
    alien_y = -200
    wall_length = random.randrange(8,18)
    wall_height = random.randrange(4,6)
    wall_start = random.randrange(0, 356, 35)
    for y in range(1, wall_height):
        alien_x = wall_start
        alien_y += 20
        value -= 1
        for x in range(1, wall_length):
            alienGroup.add(SummativeSprites.Alien(screen, (alien_x, alien_y), value))
            alien_x += 20
    
    allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions) 
    
    # Background Music and Sound Effects
    pygame.mixer.music.load("BackgroundMusic.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    playerBullet_sound = pygame.mixer.Sound("laser.wav")
    playerBullet_sound.set_volume(0.3)
    alienBullet_sound = pygame.mixer.Sound("alien shooting.wav")
    alienBullet_sound.set_volume(0.1)
    alienDeath_sound = pygame.mixer.Sound("alien death.wav")
    alienDeath_sound.set_volume(0.2)
    bossBullet_sound = pygame.mixer.Sound("boss shooting1.wav")
    bossBullet_sound.set_volume(0.2)  
    bossHealthGain_sound = pygame.mixer.Sound("bossHealthGain.wav")
    bossHealthGain_sound.set_volume(0.4)    
    bossRedBullet_sound = pygame.mixer.Sound("boss shooting2.wav")
    bossRedBullet_sound.set_volume(0.4)       
    bossBigBullet_sound = pygame.mixer.Sound("boss shooting3.wav")
    bossBigBullet_sound.set_volume(0.4)    
    freezing_sound = pygame.mixer.Sound("ice change.wav")
    freezing_sound.set_volume(0.5)
    unfreezing_sound = pygame.mixer.Sound("ice break.wav")
    unfreezing_sound.set_volume(0.5)
    death_sound = pygame.mixer.Sound("ice death.wav")
    death_sound.set_volume(1.0)   
    bossDeath_sound = pygame.mixer.Sound("boss death.wav")
    bossDeath_sound.set_volume(1.0)       
    gameOver_sound = pygame.mixer.Sound("game over.wav")
    gameOver_sound.set_volume(1.0)
    victory_sound = pygame.mixer.Sound("victory.wav")
    victory_sound.set_volume(1.0)    
    
    
    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
    count = 0
    count2 = 0
    faster_bullet = 50
    double_speed = 4
    final_countdown = 14
    change = False
    boss_visible = False
    penalty_timer1 = 0
    penalty_timer2 = 0
    still_timer1 = 0
    still_timer2 = 0
    invincible_timer1 = 0
    invincible_timer2 = 0
    player_frozen1 = False
    player_frozen2 = False
    dead1 = False
    dead2 = False
    explosion_timer = -5
    boss_dead = False
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
     
    # LOOP
    while keepGoing:
         
            # TIME
            clock.tick(60)
         
            # EVENT HANDLING: Player 1 uses:a,s,w,d,g and Player 2 uses arrow keys and p
            count += 5
            count2 += 6
            penalty_timer1 -= 5
            penalty_timer2 -= 5 
            still_timer1 -= 5
            still_timer2 -= 5
            invincible_timer1 -= 5
            invincible_timer2 -= 5
            explosion_timer -= 5
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
            
            #PLAYER1 MOVEMENT
            key = pygame.key.get_pressed()
 
            if key[pygame.K_a] and player_frozen1 == False:
                player1.change_left(1)
                player1.change_direction((double_speed, 0))
                still_timer1 = 50               
            if key[pygame.K_d] and player_frozen1 == False:
                player1.change_right(1)
                player1.change_direction((-double_speed, 0))
                still_timer1 = 50
            if key[pygame.K_w] and player_frozen1 == False:
                player1.change_forward(1)
                player1.change_direction((0, double_speed))
                still_timer1 = 50
            if key[pygame.K_s] and player_frozen1 == False:
                player1.normal_state(1)
                player1.change_direction((0, -double_speed)) 
                still_timer1 = 50
            if key[pygame.K_g] and penalty_timer1 < 0 and count%faster_bullet == 0 and player_frozen1 == False:
                playerBullet_sound.play()
                bulletGroup.add(SummativeSprites.Bullet(1, player1.get_pos(1)))  
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)
                
            if still_timer1 == 0 and player_frozen1 == False:
                player1.normal_state(1)
                
            #PLAYER2 MOVEMENT
            if key[pygame.K_LEFT] and player_frozen2 == False:
                player2.change_left(2)
                player2.change_direction((double_speed, 0))
                still_timer2 = 50
            if key[pygame.K_RIGHT] and player_frozen2 == False:
                player2.change_right(2)
                player2.change_direction((-double_speed, 0))
                still_timer2 = 50
            if key[pygame.K_UP] and player_frozen2 == False:
                player2.change_forward(2)
                player2.change_direction((0, double_speed)) 
                still_timer2 = 50
            if key[pygame.K_DOWN] and player_frozen2 == False:
                player2.normal_state(2)
                player2.change_direction((0, -double_speed))
                still_timer2 = 50
            if key[pygame.K_p] and penalty_timer2 < 0 and count%faster_bullet == 0 and player_frozen2 == False:
                playerBullet_sound.play()
                bulletGroup2.add(SummativeSprites.Bullet(2, player2.get_pos(1))) 
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)
             
            if still_timer2 == 0 and player_frozen2 == False:
                player2.normal_state(2)              
            
            #CHECKS IF BOTH PLAYERS ARE FROZEN, IF BOTH ARE FROZEN ENDS GAME
            if (player_frozen1 == True) and (player_frozen2 == True):
                boss.rect.right = 2000
                player2.rect.right = 2000
                player1.rect.right = 2000
                space.kill()
                allSprites.clear(screen, background) 
                gameOver_sound.play()
                background = pygame.Surface(screen.get_size())
                background = pygame.image.load("Owen Wilson.png")
                background = background.convert()
                screen.blit(background, (0, 0)) 
                keepGoing = False
            
            #UPDATING PLAYER1 HEARTS
            playerHealth1.change_health(score_keeper.get_lives(1))
            if score_keeper.get_lives(1) == 0 and dead1 == False:
                death_sound.play()
                explosions.add(SummativeSprites.Explosion(player1.rect.center, "player"))
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)             
                dead1 = True
                player1.rect.right = 2000
                
            #UPDATING PLAYER2 HEARTS
            playerHealth2.change_health(score_keeper.get_lives(2))
            if score_keeper.get_lives(2) == 0 and dead2 == False:
                death_sound.play()
                explosions.add(SummativeSprites.Explosion(player2.rect.center, "player"))
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)               
                dead2 = True
                player2.rect.right = 2000
            
            #PLAYER1 UNFREEZING
            player1_help = pygame.sprite.spritecollide(player1, bulletGroup2, False)
            for help in player1_help:
                if player_frozen1 == True and (score_keeper.get_score(1) < -1000) and dead1 == False:
                    player_frozen1 = False
                    penalty_timer1 = 500
                    score_keeper.player_scored(2, 500)
                    player1.invincible(1)
                    unfreezing_sound.play()
                    invincible_timer1 = 500

            #PLAYER2 UNFREEZING    
            player2_help = pygame.sprite.spritecollide(player2, bulletGroup, False)
            for help in player2_help:   
                if player_frozen2 == True and (score_keeper.get_score(2) < -1000) and dead2 == False:
                    player_frozen2 = False
                    penalty_timer2 = 500
                    score_keeper.player_scored(1, 500)
                    player2.invincible(2)
                    unfreezing_sound.play()
                    invincible_timer2 = 500
            
            #PLAYER1 AND ALIEN COLLISION
            player1_hits = pygame.sprite.spritecollide(player1, alienGroup, False)
            for hits in player1_hits:
                if invincible_timer1 < 0 and dead1 == False:
                    explosions.add(SummativeSprites.Explosion(hits.rect.center, "alien"))
                    allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)                     
                    score_keeper.player_crash(1, hits.get_value())
                    player1.freeze_state(1)
                    alienDeath_sound.play()
                    hits.kill()       
                    if score_keeper.get_score(1) < -1000 and player_frozen1 == False:
                        player_frozen1 = True 
                        freezing_sound.play()
                        score_keeper.lose_lives(1)
            
            #PLAYER2 AND ALIEN COLLISION
            player2_hits = pygame.sprite.spritecollide(player2, alienGroup, False)
            for hits in player2_hits:
                if invincible_timer2 < 0 and dead2 == False:
                    explosions.add(SummativeSprites.Explosion(hits.rect.center, "alien"))
                    allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)                     
                    score_keeper.player_crash(2, hits.get_value())
                    player2.freeze_state(2)
                    alienDeath_sound.play()
                    hits.kill()
                    if score_keeper.get_score(2) < -1000 and player_frozen2 == False:
                        player_frozen2 = True
                        freezing_sound.play()
                        score_keeper.lose_lives(2)

            #PLAYER1 AND ALIEN BULLET COLLISION
            player1_shot = pygame.sprite.spritecollide(player1, bulletGroup3, False)
            for shots in player1_shot:
                if invincible_timer1 < 0 and dead1 == False:
                    score_keeper.player_crash(1, shots.get_value())
                    player1.freeze_state(1)                
                    shots.kill()    
                    if score_keeper.get_score(1) < -1000 and player_frozen1 == False:
                        player_frozen1 = True      
                        freezing_sound.play()
                        score_keeper.lose_lives(1)
            
            #PLAYER2 AND ALIEN BULLET COLLISION   
            player2_shot = pygame.sprite.spritecollide(player2, bulletGroup3, False)
            for shots in player2_shot:
                if invincible_timer2 < 0 and dead2 == False:
                    score_keeper.player_crash(2, shots.get_value())
                    player2.freeze_state(2) 
                    shots.kill() 
                    if score_keeper.get_score(2) < -1000 and player_frozen2 == False:
                        player_frozen2 = True 
                        freezing_sound.play()
                        score_keeper.lose_lives(2)
            
            #PLAYER1 BULLET AND ALIEN COLLISION        
            for bullet in bulletGroup:
                alien_hit_list = pygame.sprite.spritecollide(bullet, alienGroup, False)
        
                for alien in alien_hit_list: 
                    score_keeper.player_scored(1, alien.get_value())   
                    alienDeath_sound.play()
                    explosions.add(SummativeSprites.Explosion(alien.rect.center, "alien"))
                    allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)         
                    alien.kill()
                    bullet.kill() 
             
            #PLAYER2 BULLET AND ALIEN COLLISION       
            for bullet in bulletGroup2:
                alien_hit_list = pygame.sprite.spritecollide(bullet, alienGroup, False)
        
                for alien in alien_hit_list: 
                    score_keeper.player_scored(2, alien.get_value())   
                    alienDeath_sound.play()
                    explosions.add(SummativeSprites.Explosion(alien.rect.center, "alien"))
                    allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)        
                    alien.kill()
                    bullet.kill()            
            
            #BOSS AND PLAYER1 BULLET COLLISION        
            boss_hits = pygame.sprite.spritecollide(boss, bulletGroup, False)
            for hits in boss_hits:
                score_keeper.boss_damaged(bossHealth.get_bottom(),1)
                bossHealth.move_down()
                hits.kill()               
            
            #BOSS AND PLAYER2 BULLET COLLISION    
            boss_hits2 = pygame.sprite.spritecollide(boss, bulletGroup2, False)
            for hits in boss_hits2:
                score_keeper.boss_damaged(bossHealth.get_bottom(),2)
                bossHealth.move_down()
                hits.kill()         
            
            #KILL BOSS AND CHECK FOR WINNER
            if score_keeper.check_bossAlive() == False and boss_dead == False:
                explosion_timer = 150
                bossDeath_sound.play()
                boss_dead = True
                explosions.add(SummativeSprites.Explosion(boss.rect.center, "boss"))
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)
            
            #ENDS GAME AFTER BOSS EXPLODES AND CHANGES THE WINNER SCREEN ACCORDING TO WHO GOT THE MOST POINTS    
            if explosion_timer == 0:
                space.kill()
                boss.rect.right = 2000
                allSprites.clear(screen, background) 
                background = pygame.Surface(screen.get_size())
                if score_keeper.get_winner() == 1:
                    background = pygame.image.load("player winner1.png")
                else:
                    background = pygame.image.load("player winner2.png")
                screen.blit(background, (0, 0))   
                victory_sound.play()
                keepGoing = False  

            #RANDOM ALIEN SHOOTING       
            for aliens in alienGroup:
                if (random.randrange(2000) == 273):
                    bulletGroup3.add(SummativeSprites.AlienBullet(aliens.get_pos(),"not boss"))
                    alienBullet_sound.play()
                    allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)  
                    
            #SPAWN ALIEN HORDE RIGHT
            if count%700 == 0 and final_countdown > 0:
                final_countdown -= 1
                value = random.randrange(5,10)
                alien_y = -200
                wall_length = random.randrange(6,12)
                wall_height = random.randrange(4,6)
                wall_start = random.randrange(320, 470, 35)
                for y in range(1, wall_height):
                    alien_x = wall_start
                    alien_y += 20
                    value -= 1
                    for x in range(1, wall_length):
                        alienGroup.add(SummativeSprites.Alien(screen, (alien_x, alien_y), value))
                        alien_x += 20
                        
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)
                
            #SPAWN ALIEN HORDE LEFT
            if count2%1260 == 0 and final_countdown > 0:
                final_countdown -= 1
                value = random.randrange(1,5)
                alien_y = -200
                wall_length = random.randrange(8,12)
                wall_height = random.randrange(4,6)
                wall_start = random.randrange(0, 50, 35)
                for y in range(1, wall_height):
                    alien_x = wall_start
                    alien_y += 20
                    value += 1
                    for x in range(1, wall_length):
                        alienGroup.add(SummativeSprites.Alien(screen, (alien_x, alien_y), value))
                        alien_x += 20
                        
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)
                
            #BRINGS DOWN BOSS
            if final_countdown == 0 and boss_visible == False:
                boss_visible = True
                boss.start_movement()
                bossHealth.start_movement()
                bossHealthGain_sound.play()
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)    
             
            #BOSS FIRING   
            if random.randrange(1000)%10 == 0 and boss_visible == True:
                bulletGroup3.add(SummativeSprites.AlienBullet(boss.get_pos_right(), "boss2"))    
                bulletGroup3.add(SummativeSprites.AlienBullet(boss.get_pos_left(), "boss2")) 
                bulletGroup3.add(SummativeSprites.AlienBullet(boss.get_pos_eye(), "boss3"))
                bulletGroup3.add(SummativeSprites.AlienBullet(boss.get_pos_eye(), "boss4"))
                bossBullet_sound.play()
                if random.randrange(10) == 1:
                    bulletGroup3.add(SummativeSprites.AlienBullet(boss.get_pos_leftcannons(), "boss1"))
                    bulletGroup3.add(SummativeSprites.AlienBullet(boss.get_pos_rightcannons(), "boss1")) 
                    bossRedBullet_sound.play()
                    if random.randrange(5) == 1:
                        bulletGroup3.add(SummativeSprites.AlienBullet(boss.get_pos_front(), "boss5"))
                        bossBigBullet_sound.play()
                allSprites = pygame.sprite.OrderedUpdates(space, score_keeper, playerHealth1, playerHealth2, bossHealth, player1, player2, alienGroup, boss, bulletGroup, bulletGroup2, bulletGroup3, explosions)
            
                
            # REFRESH SCREEN
            screen.blit(background, (0, 0))            
            allSprites.clear(screen, background) 
            allSprites.update()
            allSprites.draw(screen) 
            pygame.display.flip()

    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
 
    # Close the game window  
    pygame.time.delay(4000)
    pygame.quit()     
     
# Call the main function
instructions()
main()    
