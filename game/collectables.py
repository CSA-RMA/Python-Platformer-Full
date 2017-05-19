import pygame

from spritesheet_functions import SpriteSheet

# These constants define our collectable types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

COIN  = (0, 720, 70, 70)
class Coin(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        # Grab the image for this collectable
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
