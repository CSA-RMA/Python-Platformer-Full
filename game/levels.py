import pygame

import constants
import platforms
import collectables
import enemies

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    collectable_list= None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.collectable_list = pygame.sprite.Group()
        self.player = player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.collectable_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.collectable_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for collectable in self.collectable_list:
            collectable.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_NO_TOP, -70, 530],
                  [platforms.GRASS_NO_TOP, -140, 530],
                  [platforms.GRASS_NO_TOP, -70, 460],
                  [platforms.GRASS_NO_TOP, -140, 460],
                  [platforms.GRASS_NO_TOP, -70, 390],
                  [platforms.GRASS_NO_TOP, -140, 390],
                  [platforms.GRASS_NO_TOP, -70, 320],
                  [platforms.GRASS_NO_TOP, -140, 320],
                  [platforms.GRASS_NO_TOP, -70, 250],
                  [platforms.GRASS_NO_TOP, -140, 250],
                  [platforms.GRASS_NO_TOP, -70, 180],
                  [platforms.GRASS_NO_TOP, -140, 180],
                  [platforms.GRASS_NO_TOP, -70, 110],
                  [platforms.GRASS_NO_TOP, -140, 110],
                  [platforms.GRASS_NO_TOP, -70, 40],
                  [platforms.GRASS_NO_TOP, -140, 40],
                  [platforms.GRASS_NO_TOP, -70, -30],
                  [platforms.GRASS_NO_TOP, -140, -30],
                  [platforms.GRASS_LEFT, 200, 600],
                  [platforms.GRASS_MIDDLE, 270, 600],
                  [platforms.GRASS_RIGHT, 340, 600],
                  [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 570, 500],
                  [platforms.GRASS_RIGHT, 640, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
        collectablelist = [ [collectables.COIN, 800, 200],
                            [collectables.COIN, 1350, 100],
                            ]
        enemylist = [ [enemies.GUMP, 500, 400],
                      [enemies.GUMP, 880, 200],
                      [enemies.GUMP, 1000, 300],
                      ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        for collectable in collectablelist:
            block = collectables.Coin(collectable[0])
            block.rect.x = collectable[1]
            block.rect.y = collectable[2]
            block.player = self.player
            self.collectable_list.add(block)
        for enemy in enemylist:
            block = enemies.Gump()
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.level=self
            block.player = self.player
            self.enemy_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_03(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_NO_TOP, -70, 530],
                  [platforms.GRASS_NO_TOP, -140, 530],
                  [platforms.GRASS_NO_TOP, -70, 460],
                  [platforms.GRASS_NO_TOP, -140, 460],
                  [platforms.GRASS_NO_TOP, -70, 390],
                  [platforms.GRASS_NO_TOP, -140, 390],
                  [platforms.GRASS_NO_TOP, -70, 320],
                  [platforms.GRASS_NO_TOP, -140, 320],
                  [platforms.GRASS_NO_TOP, -70, 250],
                  [platforms.GRASS_NO_TOP, -140, 250],
                  [platforms.GRASS_NO_TOP, -70, 180],
                  [platforms.GRASS_NO_TOP, -140, 180],
                  [platforms.GRASS_NO_TOP, -70, 110],
                  [platforms.GRASS_NO_TOP, -140, 110],
                  [platforms.GRASS_NO_TOP, -70, 40],
                  [platforms.GRASS_NO_TOP, -140, 40],
                  [platforms.GRASS_NO_TOP, -70, -30],
                  [platforms.GRASS_NO_TOP, -140, -30],
                  [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
        collectablelist = [ [collectables.COIN, 800, 200],
                            [collectables.COIN, 1500, 20],
                            ]
        enemylist = [ [enemies.GUMP, 600, 400],
                      [enemies.GUMP, 880, 200],
                      [enemies.GUMP, 1150, 500],
                      ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        for collectable in collectablelist:
            block = collectables.Coin(collectable[0])
            block.rect.x = collectable[1]
            block.rect.y = collectable[2]
            block.player = self.player
            self.collectable_list.add(block)
        for enemy in enemylist:
            block = enemies.Gump()
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.level=self
            block.player = self.player
            self.enemy_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_02(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_NO_TOP, -70, 530],
                  [platforms.GRASS_NO_TOP, -140, 530],
                  [platforms.GRASS_NO_TOP, -70, 460],
                  [platforms.GRASS_NO_TOP, -140, 460],
                  [platforms.GRASS_NO_TOP, -70, 390],
                  [platforms.GRASS_NO_TOP, -140, 390],
                  [platforms.GRASS_NO_TOP, -70, 320],
                  [platforms.GRASS_NO_TOP, -140, 320],
                  [platforms.GRASS_NO_TOP, -70, 250],
                  [platforms.GRASS_NO_TOP, -140, 250],
                  [platforms.GRASS_NO_TOP, -70, 180],
                  [platforms.GRASS_NO_TOP, -140, 180],
                  [platforms.GRASS_NO_TOP, -70, 110],
                  [platforms.GRASS_NO_TOP, -140, 110],
                  [platforms.GRASS_NO_TOP, -70, 40],
                  [platforms.GRASS_NO_TOP, -140, 40],
                  [platforms.GRASS_NO_TOP, -70, -30],
                  [platforms.GRASS_NO_TOP, -140, -30],
                  [platforms.GRASS_LEFT, 200, 500],
                  [platforms.GRASS_MIDDLE, 270, 500],
                  [platforms.GRASS_RIGHT, 340, 500],
                  [platforms.GRASS_LEFT, 500, 300],
                  [platforms.GRASS_MIDDLE, 570, 300],
                  [platforms.GRASS_RIGHT, 640, 300],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
        collectablelist = [ [collectables.COIN, 800, 200],
                            [collectables.COIN, 1350, 100],
                            ]
        enemylist = [ [enemies.GUMP, 500, 400],
                      [enemies.GUMP, 880, 200],
                      [enemies.GUMP, 1000, 300],
                      ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        for collectable in collectablelist:
            block = collectables.Coin(collectable[0])
            block.rect.x = collectable[1]
            block.rect.y = collectable[2]
            block.player = self.player
            self.collectable_list.add(block)
        for enemy in enemylist:
            block = enemies.Gump()
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.level=self
            block.player = self.player
            self.enemy_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1800
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_03(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_NO_TOP, -70, 530],
                  [platforms.GRASS_NO_TOP, -140, 530],
                  [platforms.GRASS_NO_TOP, -70, 460],
                  [platforms.GRASS_NO_TOP, -140, 460],
                  [platforms.GRASS_NO_TOP, -70, 390],
                  [platforms.GRASS_NO_TOP, -140, 390],
                  [platforms.GRASS_NO_TOP, -70, 320],
                  [platforms.GRASS_NO_TOP, -140, 320],
                  [platforms.GRASS_NO_TOP, -70, 250],
                  [platforms.GRASS_NO_TOP, -140, 250],
                  [platforms.GRASS_NO_TOP, -70, 180],
                  [platforms.GRASS_NO_TOP, -140, 180],
                  [platforms.GRASS_NO_TOP, -70, 110],
                  [platforms.GRASS_NO_TOP, -140, 110],
                  [platforms.GRASS_NO_TOP, -70, 40],
                  [platforms.GRASS_NO_TOP, -140, 40],
                  [platforms.GRASS_NO_TOP, -70, -30],
                  [platforms.GRASS_NO_TOP, -140, -30],
                  [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 700, 300],
                  [platforms.GRASS_MIDDLE, 770, 300],
                  [platforms.GRASS_RIGHT, 840, 300],
                  [platforms.GRASS_LEFT, 1100, 450],
                  [platforms.GRASS_MIDDLE, 1170, 450],
                  [platforms.GRASS_RIGHT, 1240, 450],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [platforms.STONE_PLATFORM_LEFT, 1300, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 1370, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 1440, 550],
                  ]
        collectablelist = [ [collectables.COIN, 800, 200],
                            [collectables.COIN, 1500, 20],
                            ]
        enemylist = [ [enemies.GUMP, 600, 400],
                      [enemies.GUMP, 880, 200],
                      [enemies.GUMP, 1150, 500],
                      ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        for collectable in collectablelist:
            block = collectables.Coin(collectable[0])
            block.rect.x = collectable[1]
            block.rect.y = collectable[2]
            block.player = self.player
            self.collectable_list.add(block)
        for enemy in enemylist:
            block = enemies.Gump()
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.level=self
            block.player = self.player
            self.enemy_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_04(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_NO_TOP, -70, 530],
                  [platforms.GRASS_NO_TOP, -140, 530],
                  [platforms.GRASS_NO_TOP, -70, 460],
                  [platforms.GRASS_NO_TOP, -140, 460],
                  [platforms.GRASS_NO_TOP, -70, 390],
                  [platforms.GRASS_NO_TOP, -140, 390],
                  [platforms.GRASS_NO_TOP, -70, 320],
                  [platforms.GRASS_NO_TOP, -140, 320],
                  [platforms.GRASS_NO_TOP, -70, 250],
                  [platforms.GRASS_NO_TOP, -140, 250],
                  [platforms.GRASS_NO_TOP, -70, 180],
                  [platforms.GRASS_NO_TOP, -140, 180],
                  [platforms.GRASS_NO_TOP, -70, 110],
                  [platforms.GRASS_NO_TOP, -140, 110],
                  [platforms.GRASS_NO_TOP, -70, 40],
                  [platforms.GRASS_NO_TOP, -140, 40],
                  [platforms.GRASS_NO_TOP, -70, -30],
                  [platforms.GRASS_NO_TOP, -140, -30],
                  [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 680, 450],
                  [platforms.GRASS_MIDDLE, 750, 450],
                  [platforms.GRASS_RIGHT, 820, 450],
                  [platforms.GRASS_LEFT, 1100, 600],
                  [platforms.GRASS_MIDDLE, 1170, 600],
                  [platforms.GRASS_RIGHT, 1240, 600],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 380],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 380],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 380],
                  ]
        collectablelist = [ [collectables.COIN, 800, 200],
                            [collectables.COIN, 1500, 20],
                            ]
        enemylist = [ [enemies.GUMP, 600, 400],
                      [enemies.GUMP, 880, 200],
                      [enemies.GUMP, 1150, 100],
                      ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        for collectable in collectablelist:
            block = collectables.Coin(collectable[0])
            block.rect.x = collectable[1]
            block.rect.y = collectable[2]
            block.player = self.player
            self.collectable_list.add(block)
        for enemy in enemylist:
            block = enemies.Gump()
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.level=self
            block.player = self.player
            self.enemy_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_05(Level):
    """ Definition for level 5. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -3500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_NO_TOP, -70, 530],
                  [platforms.GRASS_NO_TOP, -140, 530],
                  [platforms.GRASS_NO_TOP, -70, 460],
                  [platforms.GRASS_NO_TOP, -140, 460],
                  [platforms.GRASS_NO_TOP, -70, 390],
                  [platforms.GRASS_NO_TOP, -140, 390],
                  [platforms.GRASS_NO_TOP, -70, 320],
                  [platforms.GRASS_NO_TOP, -140, 320],
                  [platforms.GRASS_NO_TOP, -70, 250],
                  [platforms.GRASS_NO_TOP, -140, 250],
                  [platforms.GRASS_NO_TOP, -70, 180],
                  [platforms.GRASS_NO_TOP, -140, 180],
                  [platforms.GRASS_NO_TOP, -70, 110],
                  [platforms.GRASS_NO_TOP, -140, 110],
                  [platforms.GRASS_NO_TOP, -70, 40],
                  [platforms.GRASS_NO_TOP, -140, 40],
                  [platforms.GRASS_NO_TOP, -70, -30],
                  [platforms.GRASS_NO_TOP, -140, -30],
                  [platforms.GRASS_LEFT, 200, 500],
                  [platforms.GRASS_MIDDLE, 270, 500],
                  [platforms.GRASS_RIGHT, 340, 500],
                  [platforms.GRASS_LEFT, 500, 300],
                  [platforms.GRASS_MIDDLE, 570, 300],
                  [platforms.GRASS_RIGHT, 640, 300],
                  [platforms.GRASS_LEFT, 800, 250],
                  [platforms.GRASS_MIDDLE, 870, 250],
                  [platforms.GRASS_RIGHT, 940, 250],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [platforms.GRASS_NO_TOP, -70+3500, 530],
                  [platforms.GRASS_NO_TOP, -140+3500, 530],
                  [platforms.GRASS_NO_TOP, -70+3500, 460],
                  [platforms.GRASS_NO_TOP, -140+3500, 460],
                  [platforms.GRASS_NO_TOP, -70+3500, 390],
                  [platforms.GRASS_NO_TOP, -140+3500, 390],
                  [platforms.GRASS_NO_TOP, -70+3500, 320],
                  [platforms.GRASS_NO_TOP, -140+3500, 320],
                  [platforms.GRASS_NO_TOP, -70+3500, 250],
                  [platforms.GRASS_NO_TOP, -140+3500, 250],
                  [platforms.GRASS_NO_TOP, -70+3500, 180],
                  [platforms.GRASS_NO_TOP, -140+3500, 180],
                  [platforms.GRASS_NO_TOP, -70+3500, 110],
                  [platforms.GRASS_NO_TOP, -140+3500, 110],
                  [platforms.GRASS_NO_TOP, -70+3500, 40],
                  [platforms.GRASS_NO_TOP, -140+3500, 40],
                  [platforms.GRASS_NO_TOP, -70+3500, -30],
                  [platforms.GRASS_NO_TOP, -140+3500, -30],
                  [platforms.GRASS_NO_TOP, -70+3640, 530],
                  [platforms.GRASS_NO_TOP, -140+3640, 530],
                  [platforms.GRASS_NO_TOP, -70+3640, 460],
                  [platforms.GRASS_NO_TOP, -140+3640, 460],
                  [platforms.GRASS_NO_TOP, -70+3640, 390],
                  [platforms.GRASS_NO_TOP, -140+3640, 390],
                  [platforms.GRASS_NO_TOP, -70+3640, 320],
                  [platforms.GRASS_NO_TOP, -140+3640, 320],
                  [platforms.GRASS_NO_TOP, -70+3640, 250],
                  [platforms.GRASS_NO_TOP, -140+3640, 250],
                  [platforms.GRASS_NO_TOP, -70+3640, 180],
                  [platforms.GRASS_NO_TOP, -140+3640, 180],
                  [platforms.GRASS_NO_TOP, -70+3640, 110],
                  [platforms.GRASS_NO_TOP, -140+3640, 110],
                  [platforms.GRASS_NO_TOP, -70+3640, 40],
                  [platforms.GRASS_NO_TOP, -140+3640, 40],
                  [platforms.GRASS_NO_TOP, -70+3640, -30],
                  [platforms.GRASS_NO_TOP, -140+3640, -30],
                  ]
        collectablelist = [ [collectables.COIN, 800, 50],
                            [collectables.COIN, 1350, 100],
                            ]
        enemylist = [ [enemies.GUMP, 800, 400],
                      [enemies.GUMP, 1280, 200],
                      [enemies.GUMP, 1500, 300],
                      [enemies.GUMP, 900, 400],
                      [enemies.GUMP, 1380, 200],
                      [enemies.GUMP, 1600, 300],
                      [enemies.GUMP, 800, 400],
                      [enemies.GUMP, 1280, 200],
                      [enemies.GUMP, 1500, 300],
                      [enemies.GUMP, 700, 400],
                      [enemies.GUMP, 1180, 200],
                      [enemies.GUMP, 1400, 300],
                      [enemies.GUMP, 600, 400],
                      [enemies.GUMP, 1080, 200],
                      [enemies.GUMP, 1300, 300],
                      [enemies.GUMP, 1000, 400],
                      [enemies.GUMP, 1480, 200],
                      [enemies.GUMP, 1700, 300],
                      [enemies.GUMP, 1100, 400],
                      [enemies.GUMP, 1580, 200],
                      [enemies.GUMP, 1800, 300],
                      [enemies.GUMP, 1200, 400],
                      [enemies.GUMP, 1780, 200],
                      [enemies.GUMP, 1900, 300],
                      [enemies.GUMP, 1300, 400],
                      [enemies.GUMP, 1880, 200],
                      [enemies.GUMP, 2000, 300],
                      [enemies.GUMP, 1400, 400],
                      [enemies.GUMP, 1980, 200],
                      [enemies.GUMP, 2100, 300],
                      [enemies.GUMP, 1400, 400],
                      [enemies.GUMP, 2080, 200],
                      [enemies.GUMP, 2200, 300],
                      [enemies.GUMP, 1500, 400],
                      [enemies.GUMP, 2180, 200],
                      [enemies.GUMP, 2300, 300],
                      ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        for collectable in collectablelist:
            block = collectables.Coin(collectable[0])
            block.rect.x = collectable[1]
            block.rect.y = collectable[2]
            block.player = self.player
            self.collectable_list.add(block)
        for enemy in enemylist:
            block = enemies.Gump()
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.level=self
            block.player = self.player
            self.enemy_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
