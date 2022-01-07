from src.classes.Command import Command

class Menu:
  # array of valid commands
  commands = []

  def __init__(self, header, commands):
    self.header = header
    self.commands = commands
    self.commands.append(Command("quit", ["q"], "", lambda x: None, True))
  
  def enter(self, prevCommand=None):
    print()
    print(self.header)
    self.listCommands()

    commandStr = ""

    while True:
      commandStr = input("> ")
      command = self.getCommand(commandStr)
      if command != None:
        break
      else:
        print("Please enter a valid command.")
    
    command.action(commandStr)
    if not command.quit:
      self.enter()
  
  def listCommands(self):
    print("Actions:")
    for c in self.commands:
      if c.shortcuts:
        print("  " + c.name, c.shortcuts)
      else:
        print("  " + c.name)
      
      if c.description != "":
        print("    " + c.description)
  
  def getCommand(self, commandName):
    for c in self.commands:
      if c.matches(commandName):
        return c
