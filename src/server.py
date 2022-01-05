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

def getLastEntry():
  res = requests.get(url=config["server_url"] + "/stats/lastEntry")
  if not res.ok:
    printError(res)
  else:
    return parser.parse(res.json()).strftime("%A %B %d, %Y %I:%M%p")

print("last entry:", getLastEntry())
