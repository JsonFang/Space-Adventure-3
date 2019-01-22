"""
Author: Jason Fang
Date: May 5, 2017
Description: This contains all the sprites needed for the game
"""

import pygame
import random
 
 
class Space(pygame.sprite.Sprite):
    """This class defines the sprite for the scrolling background"""
    def __init__(self, screen):
        # Call the parent init() method
        pygame.sprite.Sprite.__init__(self)
        
        self.screen =  screen
        
        self.image = pygame.image.load("spacebackgroundlong.png")
        self.rect = self.image.get_rect()        
        self.rect.left = 0
        self.rect.bottom = 480
        self.__dy = 2
 
    def update(self):
        """This method will be called automatically to reposition the 
        background on the screen"""
        self.rect.top += self.__dy
        if self.rect.bottom == 3748:
            self.rect.bottom = 530        
        
 
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player 1 and Player 2'''
    def __init__(self, screen, player_num):
        '''This initializer takes a screen surface, and player number as
        parameters.  Depending on the player number it loads the appropriate
        image and positions it on the left or right end of the court'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.width = screen.get_width()
 
        # If we are initializing a sprite for player 1, 
        # position it 150 pixels from screen left.
        if player_num == 1:
            self.image = pygame.image.load("player1.png")
            self.rect = self.image.get_rect()            
            self.rect.left = 150
        # Otherwise, position it 150 pixels from the right of the screen.
        else:
            self.image = pygame.image.load("player2.png")
            self.rect = self.image.get_rect()                
            self.rect.right = screen.get_width()-150
 
        # Center the player vertically (and a little lower) in the window.
        self.rect.top = screen.get_height()-50
        self.__screen = screen
        self.__dy = 0
        self.__dx = 0
      
    def change_direction(self, xy_change):
        '''This method takes a (x,y) tuple as a parameter, extracts the 
        y element from it, and uses this to set the players y direction.'''
        
        if ((self.rect.top > 270) and (xy_change[1] > 0)) or\
           ((self.rect.bottom < self.__screen.get_height()) and (xy_change[1] < 0)):
            self.rect.top -= xy_change[1]
            
        if ((self.rect.left > 0) and (xy_change[0] > 0)) or\
           ((self.rect.right < self.__screen.get_width()) and (xy_change[0] < 0)):
            self.rect.right -= xy_change[0]
        
    def change_right(self, player_num):
        """This method takes the player_num as a parameter and sets the image 
        to a right image accordingly"""
        if player_num == 1:
            self.image = pygame.image.load("player1_right.png")
        else:
            self.image = pygame.image.load("player2_right.png")
        
    def change_left(self, player_num):
        """This method takes the player_num as a parameter and sets the image 
        to a left image accordingly"""        
        if player_num == 1:
            self.image = pygame.image.load("player1_left.png")
        else:
            self.image = pygame.image.load("player2_left.png")
    
    def change_forward(self, player_num):
        """This method takes the player_num as a parameter and sets the image 
        to a forward image accordingly"""        
        if player_num == 1:
            self.image = pygame.image.load("player1_forward.png")
        else:
            self.image = pygame.image.load("player2_forward.png")
    
    def freeze_state(self, player_num):
        """This method takes the player_num as a parameter and sets the image 
        to a freeze image accordingly"""        
        if player_num == 1:
            self.image = pygame.image.load("player1_frozen.png")
        else:
            self.image = pygame.image.load("player2_frozen.png")
    
    def normal_state(self, player_num):
        """This method takes the player_num as a parameter and sets the image 
        to a normal(neutral) image accordingly"""        
        if player_num == 1:
            self.image = pygame.image.load("player1.png")    
        if player_num == 2:
            self.image = pygame.image.load("player2.png")   
    
    def invincible(self, player_num):
        """This method takes the player_num as a parameter and sets the image 
        to a invincible (unfreeze) image accordingly"""        
        if player_num == 1:
            self.image = pygame.image.load("player1_invincible.png")    
        if player_num == 2:
            self.image = pygame.image.load("player2_invincible.png") 
            
    def get_pos(self, player_num):
        """This method returns the position of the player."""
        if player_num==1:
            return (self.rect.left+18, self.rect.bottom-33)
        elif player_num==2:
            return (self.rect.left, self.rect.bottom) 
        
        
class Alien(pygame.sprite.Sprite):
    """This class defines the alien sprites"""
    def __init__(self, screen, position, value):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.width = screen.get_width()
        
        if value == 1:
            self.image = pygame.image.load("alien1.png")
            self.__value = 10
        elif value == 2:
            self.image = pygame.image.load("alien2.png")
            self.__value = 20
        elif value == 3:
            self.image = pygame.image.load("alien3.png")
            self.__value = 30
        elif value == 4:
            self.image = pygame.image.load("alien4.png")
            self.__value = 40
        elif value == 5:
            self.image = pygame.image.load("alien5.png")
            self.__value = 50
        elif value == 6:
            self.image = pygame.image.load("alien6.png")
            self.__value = 60
        elif value == 7:
            self.image = pygame.image.load("alien7.png")
            self.__value = 70
        elif value == 8:
            self.image = pygame.image.load("alien8.png")
            self.__value = 80        
        
        self.rect = self.image.get_rect() 
        self.__dy = 1
        self.rect.left = position[0]
        self.rect.bottom = position[1]
        
    def get_value(self):
        """This method returns the value of the alien"""
        return self.__value
    
    def get_pos(self):
        """This method returns the position of the alien"""
        return (self.rect.left+8, self.rect.bottom)    
    
    def update(self):
        """This method will be called automatically to repostion the alien sprites and kill the alien sprites if they move off screen"""
        self.rect.top += self.__dy
        
        if (self.rect.bottom >= 640):
            self.kill()    
    
class Boss(pygame.sprite.Sprite):
    '''This class defines the sprite for the boss'''
    def __init__(self, screen):
        # Call the parent init() method
        pygame.sprite.Sprite.__init__(self)
        
        self.screen =  screen
        
        self.image = pygame.image.load("alienboss.png")
        self.rect = self.image.get_rect()        
        self.rect.left = 110
        self.rect.bottom = 0
        self.__movement = 0
 
    def start_movement(self):
        """This method starts the movement for the boss"""
        self.__movement = 2
    
    def get_pos_all(self):
        """This method returns the position of the whole boss"""
        return (self.rect.left+random.randrange(0,401,20),self.rect.bottom-20)    
    
    def get_pos_left(self):
        """This method returns the position of the left of the boss"""
        return (self.rect.left+random.randrange(5,29),self.rect.bottom-35) 
        
    def get_pos_right(self):
        """This method returns the position of the right of the boss"""
        return (self.rect.left+random.randrange(359,389),self.rect.bottom-35)  
        
    def get_pos_eye(self):
        """This method returns the position of the eye"""
        return (self.rect.left+random.randrange(195,198),self.rect.bottom-85)
        
    def get_pos_rightcannons(self):
        """This method returns the position of the right cannons"""
        return (self.rect.left+random.randrange(260,350,15),self.rect.bottom-20)
    
    def get_pos_leftcannons(self):
        """This method returns the position of the left cannons"""
        return (self.rect.left+random.randrange(50,140,15),self.rect.bottom-20) 
    
    def get_pos_front(self):
        """This method returns the position of the front of the boss"""
        return(self.rect.left+179, self.rect.bottom)
 
    def update(self):
        """This method will be called automatically to reposition the boss sprite and stop it from moving too far down"""
        if self.__movement > 0:
            self.rect.centery += self.__movement
        if self.rect.top > 30:
            self.__movement = 0
            
class BossHealth(pygame.sprite.Sprite):
    '''This class defines the sprite for the boss health'''
    def __init__(self, screen):
        # Call the parent init() method
        pygame.sprite.Sprite.__init__(self)

        self.screen =  screen
        
        self.image = pygame.image.load("bossHealth.png")
        self.rect = self.image.get_rect()        
        self.rect.left = 620
        self.rect.bottom = 0
        self.__movement = 0
        
    def start_movement(self):
        """This method starts the movement for the boss health"""
        self.__movement = 2
    
    def get_bottom(self):
        """This method returns the bottom of the boss health"""
        return self.rect.bottom
    
    def move_down(self):
        """This method moves the boss health down"""
        self.rect.bottom -= 1
    
    def update(self):
        """This method will be called automatically to reposition the bossHealth sprite and prevent it from moving too far down"""
        if self.__movement > 0:
            self.rect.centery += self.__movement
        if self.rect.top > -130:
            self.__movement = 0    
    
class Bullet(pygame.sprite.Sprite):
    """This class defines the bullet sprites for player 1 and player 2"""
    def __init__(self, player_num, xy_pos):
        # Call the parent init() method
        pygame.sprite.Sprite.__init__(self)                
        self.__player_num = player_num
        
        if self.__player_num==1:
            self.image=pygame.image.load("Bullet1.png")
            self.__dy=5
        
        elif self.__player_num==2:
            self.image=pygame.image.load("Bullet2.png")
            self.__dy=5
        
        self.rect = self.image.get_rect()
        self.rect.left = xy_pos[0]
        self.rect.bottom = xy_pos[1]
    
    def get_pos(self):
        """This method returns the position of the bullet"""
        return (self.rect.left,self.rect.bottom)
        
    def update(self):
        """This method will be called automatically to reposition the bullet sprites and kill them if they move off screen"""
        self.rect.top -= self.__dy
        
        if (self.rect.top <= 0):
            self.kill()
 
class AlienBullet(pygame.sprite.Sprite):
    """This class defines the alien bullet sprites"""
    def __init__(self, xy_pos, rank):
        # Call the parent init() method
        pygame.sprite.Sprite.__init__(self)
        
        if rank == "boss1":
            self.image = pygame.image.load("bossBullet1.png")
            self.__value = 50
            self.__dy = 3
            self.__dx = 0
        
        elif rank == "boss2":
            self.image = pygame.image.load("bossBullet2.png")
            self.__value = 50
            self.__dy = 3
            self.__dx = random.randrange(-3,4)
            
        elif rank == "boss3":
            self.image = pygame.image.load("bossBullet3.png")
            self.__value = 50
            self.__dy = random.randrange(-2,3,4)
            self.__dx = random.randrange(-4,4)            
        
        elif rank == "boss4":
            self.image = pygame.image.load("bossBullet4.png")
            self.__value = 50   
            self.__dy = random.randrange(-2,3,4)
            self.__dx = random.randrange(-4,4)            
            
        elif rank == "boss5":
            self.image = pygame.image.load("bossBullet5.png")
            self.__value = 250    
            self.__dy = 5
            self.__dx = 0
            
        else:
            self.image = pygame.image.load("alienBullet.png")
            self.__value = 30
            self.__dy = 3
            self.__dx = 0            


        self.rect = self.image.get_rect()
        self.rect.left = xy_pos[0]
        self.rect.bottom = xy_pos[1]  
        
    def get_value(self):
        """This method returns the value of the alienBullet"""
        return self.__value
    
    def get_pos(self):
        """This method returns the position of the alienBullet"""
        return (self.rect.left,self.rect.bottom) 
    
    def update(self):
        """This method will be called automatically to reposition the alien bullet sprites and kill them if they move off screen"""
        self.rect.top += self.__dy 
        self.rect.left += self.__dx
        if self.rect.bottom > 640:
            self.kill()
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the custom font "Font", and
        sets the starting score to 0 for player 1 and player 2'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.SysFont("arial", 30)
        self.__player1_score = 0
        self.__player2_score = 0  
        self.__alien_value = 0
        self.__lifeCount1 = 3
        self.__lifeCount2 = 3
        self.__bossAlive = True
        self.__myCustomFont = pygame.font.Font("Font.ttf", 25)
 
    def player_scored(self, player_num, value):
        '''This method adds to the score for the player1 and player2'''
        if player_num == 1:
            self.__player1_score += value
            self.__alien_value = value
        else:
            self.__player2_score += value
            self.__alien_value = value            
        
    def player_crash(self, player_num, value):
        '''This method deducts points for player1 and player2'''
        if player_num == 1:
            self.__player1_score -= value
            self.__alien_value = value  
        else:
            self.__player2_score -= value
            self.__alien_value = value 
            
    def lose_lives(self, player_num):
        """This method deducts lives for player1 and player2"""
        if player_num == 1:
            self.__lifeCount1 -= 1
            if self.__lifeCount1 == 0:
                self.__player1_score -= 1000
        else:
            self.__lifeCount2 -= 1        
            if self.__lifeCount2 == 0:
                self.__player2_score -= 1000   
                
    def get_lives(self, player_num):
        """This method returns the life count for player1 and player2"""
        if player_num == 1:
            return self.__lifeCount1
        else:
            return self.__lifeCount2
        
    def get_score(self, player_num):
        """This method returns the score for player1 and player2"""
        if player_num == 1:
            return self.__player1_score
        else:
            return self.__player2_score       
        
    def boss_damaged(self, position, player_num):
        """This method checks if the boss has been damaged enough to die. If the boss has been damaged enough, the player who last hit the boss will recieve 1000 points"""
        if position == 1 and player_num == 1:
            self.__player1_score += 1000
        if position == 1 and player_num == 2:
            self.__player2_score += 1000
        if position == 1:
            self.__bossAlive = False
    
    def check_bossAlive(self):
        """This method returns whether or not the boss is alive"""
        if self.__bossAlive == False:
            return False
        else:
            return True
        
    def get_winner(self):
        """This method will return which player has more points"""
        if self.__player1_score > self.__player2_score:
            return 1
        else:
            return 2            
        
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "PLAYER 1: %d        PLAYER 2: %d "  %\
                (self.__player1_score, self.__player2_score)
        self.image = self.__myCustomFont.render(message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)   
        
class PlayerHealth1(pygame.sprite.Sprite):
    '''This class defines the sprite for player1's health'''
    def __init__(self, screen):
        # Call the parent init() method
        pygame.sprite.Sprite.__init__(self)
        
        self.screen =  screen
        
        self.image = pygame.image.load("hearts.png")
        self.rect = self.image.get_rect()        
        self.rect.left = 0
        self.rect.bottom = 480
        self.__hp = 3
 
    def change_health(self, value):
        """This method takes a value as a parameter and changes the self.__hp to the value"""
        self.__hp = value
 
    def update(self):
        """This method will be called automatically to reposition the player1 health sprite"""
        if self.__hp == 2:
            self.rect.left = -16
        if self.__hp == 1:
            self.rect.left = -32
        if self.__hp == 0:
            self.rect.left = -48   
            
class PlayerHealth2(pygame.sprite.Sprite):
    '''This class defines the sprite for the player2's health'''
    def __init__(self, screen):
        # Call the parent init() method
        pygame.sprite.Sprite.__init__(self)
        
        self.screen =  screen
        
        self.image = pygame.image.load("hearts2.png")
        self.rect = self.image.get_rect()        
        self.rect.left = 594
        self.rect.bottom = 480
        self.__hp = 3
 
    def change_health(self, value):
        """This method takes a value as a parameter and changes the self.__hp to the value"""
        self.__hp = value
 
    def update(self):
        """This method will be called automatically to reposition the player2 health sprite"""
        if self.__hp == 2:
            self.rect.left = 610
        if self.__hp == 1:
            self.rect.left = 626
        if self.__hp == 0:
            self.rect.left = 640    
        
class Explosion(pygame.sprite.Sprite):
    '''This class defines the sprite for the explosions'''
    def __init__(self, center, unit_type):
        # Call the parent init() method
        pygame.sprite.Sprite.__init__(self)
        
        if unit_type == "alien":
            self.images = []
            for image_number in range(25):
                image = pygame.image.load("explosion " + str(image_number+1) + ".png")
                self.images.append(image)
        
        if unit_type == "player":
            self.images = []
            for image_number in range(36):
                image = pygame.image.load("explosions " + str(image_number+1) + ".png")
                self.images.append(image) 
                
        if unit_type == "boss":
            self.images = []
            for image_number in range(17):
                image = pygame.image.load("bossplode " + str(image_number+1) + ".png")
                self.images.append(image)            
            
        self.__unitType = unit_type
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.__image_number = 1

    def update(self):
        """This method will automatically update the images for the explosion sprites
        and kill them once all the images have been shown"""
        self.__image_number += 1
        self.image = self.images[self.__image_number-1]
        if self.__unitType == "alien" and self.__image_number == 25:
            self.kill()
        if self.__unitType == "player" and self.__image_number == 36:
            self.kill()
        if self.__unitType == "boss" and self.__image_number == 17:
            self.kill()