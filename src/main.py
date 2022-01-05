from src.classes.Menu import Menu
from src.classes.Command import Command

mainMenu = Menu("Mood Tracker", [
  Command("new entry", None, lambda: print("make a new entry")),
  Command("quit", None, lambda: None)
])
