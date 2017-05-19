import pygame
import constants
class Rock(pygame.sprite.Sprite):
    """ This class represents the rock . """

    # Set speed vector of the rock
    change_x = 12
    change_y = -8
    direction = "R"
    level = None
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill((100,100,100,0))
 
        self.rect = self.image.get_rect()
        #self.direction = indir
        print("rock initialized")
        
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .8

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
 
    def update(self):
        """ Move the rock. """
        self.calc_grav()
        if self.direction=="R":
            self.rect.x += self.change_x
        else:
            if self.direction=="L":
                self.rect.x -= self.change_x
        self.rect.y += self.change_y

        """Collisions moved to player.py under #for projectile in self.projectilelist.sprites():#"""
        #block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        #for block in block_hit_list:
            # If we hit a block, destroy ourself
        #    self = None
        #enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, True)
        #for enemy in enemy_hit_list:
        #    self = None
            
