import json
import requests

config = json.load(open('config.json', 'r'))

def printError(res):
  print("Error: " + str(res.status_code) + " " + res.reason)
  print(res.content)

def getStatuses():
  res = requests.get(url=config["server_url"] + "/status/item", json={"body": {}})
  if not res.ok:
    printError(res)
  else:
    return res.json()

def getActivities():
  res = requests.get(url=config["server_url"] + "/activity", json={"body": {}})
  if not res.ok:
    printError(res)
  else:
    return res.json()

def saveEntry(entry):
  res = requests.get(url=config["server_url"] + "/activity", json={"body": entry})
  if not res.ok:
    printError(res)
  else:
    print("Entry successfully created.")

getStatuses()
