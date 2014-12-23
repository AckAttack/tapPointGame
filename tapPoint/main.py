from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock


class TapPointGame(Widget):
    player1 = NumericProperty(0)
    player2 = NumericProperty(0)
    points = NumericProperty(1)

    def update(self, dt):
        self.points += self.points * 0.01

    def on_touch_down(self, touch):
        if touch.x < self.width / 2:
            self.player1 += int(self.points)
        if touch.x > self.width - self.width/2:
            self.player2 += int(self.points)
        self.points = 1

class TapPointApp(App):
    def build(self):
        game = TapPointGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    TapPointApp().run()
