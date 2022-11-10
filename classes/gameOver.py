import pyglet
from utils import Utils

class GameOver:
   def __init__(self):
      self.utils = Utils()

   def draw(self, correctWord: str):
      x = self.utils.width // 2 + 225
      y = self.utils.height // 2 + 100

      self.gameOver = pyglet.text.Label(
         f"Game over",
         font_name="Config Rounded Bold",
         font_size=48,
         color=(255, 46, 52, 255),
         x=x,
         y=y,
         anchor_x="center",
         anchor_y="center",
      )

      self.pressEnter = pyglet.text.Label(
         f"Aperte enter para sair",
         font_name="Config Rounded Bold",
         font_size=36,
         color=(255, 255, 255, 255),
         x=x - 225,
         y=y - 400,
         anchor_x="center",
         anchor_y="center",
      )

      self.correctWord = pyglet.text.Label(
         f"A palavra correta é: " + correctWord.upper(),
         font_name="Config Rounded Bold",
         font_size=32,
         color=(255, 255, 255, 255),
         x=x,
         y=y - 90,
         anchor_x="center",
         anchor_y="center",
      )

      self.gameOver.draw()
      self.pressEnter.draw()
      self.correctWord.draw()

   def press(self, key: str):
      if(key == '－'):
         pyglet.app.exit()


