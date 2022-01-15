import time
import src.server as server

def newEntry(prevCommand):
  entry = {
    "date": int(time.time()),
    "mood": 0,
    "statuses": [],
    "activities": []
  }

  # fetch statuses from server
  statuses = list(map(lambda x: x["name"], server.getStatuses()))
  if not isinstance(statuses, list):
    print("Could not get statuses from server.")
    return
  elif not statuses:
    print("No statuses found.")
  print("statuses:", statuses)

  # fetch activities from server
  activities = list(map(lambda x: x["name"], server.getActivities()))
  if not isinstance(activities, list):
    print("Could not get activities from server.")
    return
  elif not activities:
    print("No statuses found.")
  print("activities:", activities)

  # input status data
  entry["mood"] = getStatus("mood")
  for s in statuses:
    entry["statuses"].append({ "name": s, "value": getStatus(s) })

  # input activities
  print("Enter activities (return empty activity to finish):")
  while True:
    print("Current activities:", entry["activities"])
    a = input("> ")

    # finish
    if a == "":
      print("Finish entering activities? (enter again to confirm)")
      if input("> ") == "":
        break
    
    # remove entered activity
    elif a.startswith("remove ") or a.startswith("rm "):
      toRemove = a.split(" ")[1]
      if toRemove in entry["activities"]:
        entry["activities"].remove(toRemove)

    # add activity
    elif a in entry["activities"]:
      print(a + " has already been added.")
    elif a not in activities:
      print(a + " is not a valid activity.")
    else:
      entry["activities"].append(a)
    
  # send to server
  server.saveEntry(entry)

def getStatus(name):
  print(name + ":")
  val = 0
  while True:
    val = input("> ")

    try:
      val = float(val)
    except ValueError:
      print("Please enter a number from 1 to 10")
      continue

    if 1 <= val <= 10:
      break
    else:
      print("Please enter a number from 1 to 10")
  return val
