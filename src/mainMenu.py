from src.classes.Menu import Menu
from src.classes.Command import Command
from src.newEntry import newEntry
from src.statsMenu import statsMenu

mainMenu = Menu("Mood Tracker", [
  Command("new entry", ["n"],  "", newEntry),
  Command("stats", [], "", statsMenu.enter)
])
