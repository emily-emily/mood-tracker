import json
import requests
from dateutil import parser
import src.auth

config = json.load(open('config.json', 'r'))

def printError(res):
  print("Error: " + str(res.status_code) + " " + res.reason)
  print("Message:", res.json()["message"])
  # print(res.content)

def login(email, pw):
  res = requests.get(url=config["server_url"] + "/user/login", json={ "email": email, "password": pw })
  if not res.ok:
    printError(res)
    return None
  else:
    return res.json()

def getStatuses():
  res = requests.get(url=config["server_url"] + "/status", headers={ "authorization": src.auth.token })
  if not res.ok:
    printError(res)
  else:
    return res.json()

def getActivities():
  res = requests.get(url=config["server_url"] + "/activity", headers={ "authorization": src.auth.token })
  if not res.ok:
    printError(res)
  else:
    return res.json()

def saveEntry(entry):
  res = requests.post(url=config["server_url"] + "/entry", headers={ "authorization": src.auth.token }, json=[entry])
  if not res.ok:
    printError(res)
  else:
    print("Entry successfully created.")

def getLastEntryDate():
  res = requests.get(url=config["server_url"] + "/stats/lastEntryDate", headers={ "authorization": src.auth.token })
  if not res.ok:
    printError(res)
  else:
    return parser.parse(res.json())

def getLastActivityOccurrrence(activity):
  res = requests.get(url=config["server_url"] + "/stats/lastActivityOccurrence", headers={ "authorization": src.auth.token }, json={ "activity": activity })
  if not res.ok:
    printError(res)
  else:
    return parser.parse(res.json())

# try:
#   print("Last entry:", getLastEntryDate().strftime("%A %B %d, %Y %I:%M%p"))
# except Exception as e:
#   print("Couldn't connect to server.")
#   quit()
