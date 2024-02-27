import arcade

# основа
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Star Wars"


class Millennium_Falcon(arcade.Sprite):

    def __init__(self):
        super().__init__('StarWars/falcon.png', 0.3)

        self.center_x = SCREEN_WIDTH / 2

        self.center_y = 100


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('StarWars/background.jpg')
        # jтрисовка сокола
        self.falcon = Millennium_Falcon()
        self.setup()

    # размещение объектов на сцене при запуске игры
    def setup(self):
        pass
    # отрисовкa
    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        # отричовка фалкона
        self.falcon.draw()
    # обновление кадра
    def update(self, delta_time):
        pass

#
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
