import json
import requests
from dateutil import parser

config = json.load(open('config.json', 'r'))

def printError(res):
  print("Error: " + str(res.status_code) + " " + res.reason)
  print(res.content)

def getStatuses():
  res = requests.get(url=config["server_url"] + "/status/item")
  if not res.ok:
    printError(res)
  else:
    return res.json()

def getActivities():
  res = requests.get(url=config["server_url"] + "/activity")
  if not res.ok:
    printError(res)
  else:
    return res.json()

def saveEntry(entry):
  res = requests.post(url=config["server_url"] + "/entry", json=[entry])
  if not res.ok:
    printError(res)
  else:
    print("Entry successfully created.")

def getLastEntryDate():
  res = requests.get(url=config["server_url"] + "/stats/lastEntryDate")
  if not res.ok:
    printError(res)
  else:
    return parser.parse(res.json())

def getLastActivityOccurrrence(activity):
  res = requests.get(url=config["server_url"] + "/stats/lastActivityOccurrence", json={ "activity": activity })
  if not res.ok:
    printError(res)
  else:
    return parser.parse(res.json())

try:
  print("Last entry:", getLastEntryDate().strftime("%A %B %d, %Y %I:%M%p"))
except Exception as e:
  print("Couldn't connect to server.")
  quit()
