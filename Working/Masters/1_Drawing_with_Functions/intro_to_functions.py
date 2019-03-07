import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_cloud():
    """ draw cloud """
    arcade.draw_circle_filled(100, 450, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(220, 450, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(160, 500, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(160, 400, 60, arcade.color.WHITE)

def draw_rolling_hills():
    """ draw rolling hills """
    arcade.draw_circle_filled(100, 50, 200, arcade.color.BROWN_NOSE)
    arcade.draw_circle_filled(700, 50, 200, arcade.color.BROWN_NOSE)
    arcade.draw_circle_filled(400, 50, 200, arcade.color.BROWN_NOSE)

def draw_tree():
    """ draw tree """
    arcade.draw_rectangle_filled(660, 300, 100, 300, arcade.color.CHESTNUT)
    arcade.draw_circle_filled(720, 450, 60, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(600, 450, 60, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(660, 500, 60, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(660, 400, 60, arcade.color.DARK_SPRING_GREEN)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_rolling_hills()
    draw_tree()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()