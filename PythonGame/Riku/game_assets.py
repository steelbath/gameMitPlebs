

class GameSettings():
    screen_width = 1024
    screen_height = 768
    bg_color = (50,50,50)

    @classmethod
    def screen_size(cls):
        return (cls.screen_width, cls.screen_height)


class GameState:
    MAIN_MENU = 0
    RUNNING = 1


class Game():
    state = GameState.MAIN_MENU
    player = None
    running = False
