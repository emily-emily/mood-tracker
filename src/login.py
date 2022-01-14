from getpass import getpass
import src.server
import getpass
import src.mainMenu as main
import src.auth

def login():
  print("Login")

  response = None

  while response == None:
    email = input("email: ")
    pw = getpass.getpass("password: ")

    response = src.server.login(email, pw)

  src.auth.name = response["name"]
  src.auth.token = response["token"]

  main.mainMenu.enter()
