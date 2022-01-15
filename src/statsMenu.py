from src.classes.Menu import Menu
from src.classes.Command import Command
import src.stats

statsMenu = Menu("Stats", [
  Command("graph", [], "Graph statuses", src.stats.graph),
  Command("last <activity>", [], "Show date of the last occurrence of <activity>", src.stats.lastActivity)
])
