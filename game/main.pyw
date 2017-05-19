"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller example.

From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

import constants
import levels

from player import Player

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption(":^)v ersion 1.7.478.23.57.00002")
    myfont = pygame.font.SysFont("comic sans ms", 20)
    heartimg = pygame.transform.scale(pygame.image.load("heart.png"), (40,40))

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))
    level_list.append(levels.Level_04(player))
    level_list.append(levels.Level_05(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 140
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # See if button has been pressed
    keypressed = False

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                keypressed = True
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.throw()
                if event.key == pygame.K_DOWN:
                    player.projectileheight += 50

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_DOWN:
                    player.projectileheight -= 50

        # Update the player.
        active_sprite_list.update()
        player.projectilelist.update()

        # Update items in the level
        current_level.update()
        heartdistance=0

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        label = myfont.render("Coin count: {}".format(player.coins), 1, (255,225,0))
        screen.blit(label, (constants.SCREEN_WIDTH-250, 5))
        active_sprite_list.draw(screen)
        player.projectilelist.draw(screen)
        for i in range(player.health):
            screen.blit(heartimg,(heartdistance+5, 10))
            heartdistance+=35
        if player.health<=0:
            gameovertext = "You died, game over!"
            endlabel = myfont.render(gameovertext, 1, (225,50,50))
            text_width = endlabel.get_width()
            text_height = endlabel.get_height()
            screen.blit(endlabel, ((constants.SCREEN_WIDTH-text_width)/2,(constants.SCREEN_HEIGHT-text_height)/2))
            #print(constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2)
        if not keypressed:
            introtext1 = "Use the arrow keys to move and jump around the scrolling screen!"
            introtext2 = "Press space to throw a rock, and hold the down arrow to lower how high you throw it!"
            endlabel1 = myfont.render(introtext1, 1, (50,125,50))
            endlabel2 = myfont.render(introtext2, 1, (50,125,50))
            text_width1 = endlabel1.get_width()
            text_height1 = endlabel1.get_height()
            text_width2 = endlabel2.get_width()
            text_height2 = endlabel2.get_height()
            screen.blit(endlabel1, ((constants.SCREEN_WIDTH-text_width1)/2,(constants.SCREEN_HEIGHT-text_height1)/2-50))
            screen.blit(endlabel2, ((constants.SCREEN_WIDTH-text_width2)/2,(constants.SCREEN_HEIGHT-text_height2)/2+50))

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
