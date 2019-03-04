import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_cloud():
    """ draw cloud """
    arcade.draw_circle_filled(290, 400, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(410, 400, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(350, 450, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(350, 350, 60, arcade.color.WHITE)

def rolling_hills():
    """ draw rolling hills """


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()