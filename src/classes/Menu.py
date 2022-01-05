class Menu:
  # array of valid commands
  commands = []

  def __init__(self, header, commands):
    self.header = header
    self.commands = commands
  
  def enter(self):
    print(self.header)
    self.listCommands()

    command = ""

    while True:
      command = input("> ")
      if self.hasCommand(command):
        break
      else:
        print("Please enter a valid command.")
    
    self.runCommand(command)
  
  def listCommands(self):
    print("Actions:")
    for c in self.commands:
      print(" " + c.name)
  
  def hasCommand(self, commandName):
    for c in self.commands:
      if c.name == commandName:
        return True
    return False

  def runCommand(self, commandName):
    for c in self.commands:
      if c.name == commandName:
        c.action()
