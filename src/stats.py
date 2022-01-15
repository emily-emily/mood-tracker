import src.server
import matplotlib.pyplot as plt

def lastActivity(prevCommand):
  activity = prevCommand.split(" ")[1]
  print("activity:", activity)
  lastOccurrence = src.server.getLastActivityOccurrrence(activity)
  if lastOccurrence:
    print(lastOccurrence)

def graph(prevCommand):
  res = src.server.getPlotData("mood")
  x = res["x"]
  y = res["y"]
  
  plt.plot(x, y, label="mood")
  
  plt.xlabel('date')
  plt.ylabel('value')
  plt.ylim(0,10)
  
  plt.title('Graph')
  
  plt.show()
