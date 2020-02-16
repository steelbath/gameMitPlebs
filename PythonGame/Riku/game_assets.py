

class GameSettings():
    screen_width = 1024
    screen_height = 768
    bg_color = (50,50,50)


class GameState:
    MAIN_MENU = 0
    RUNNING = 1


class Game():
    state = GameState.MAIN_MENU
    player = None
