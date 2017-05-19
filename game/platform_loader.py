import pygame
class PlatformLoader():
    """ Class used to grab platforms out of a platform sheet. """
    # This points to our platform sheet image
    platform_sheet = None
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the platform sheet. """

        # Load the platform sheet.
        display = pygame.display.set_mode([50,50])
        self.platform_sheet = pygame.image.load(file_name).convert()
        width = self.platform_sheet.get_width()
        height = self.platform_sheet.get_height()
        print(width)
        print(height)
loader = PlatformLoader("tiles_spritesheet.png")
        
