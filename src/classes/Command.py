class Command:
  def __init__(self, name, shortcuts, description, action, quit=False):
    self.name = name
    self.shortcuts = shortcuts
    self.description = description
    self.action = action
    self.quit = quit
  
  # determines whether a command written by a user matches this command
  def matches(self, commandStr):
    if Command._matches(commandStr, self.name):
      return True
    for s in self.shortcuts:
      if Command._matches(commandStr, s):
        return True
    return False

  @staticmethod
  def _matches(userCommand, strToMatch):
    a = userCommand.split(" ")
    b = strToMatch.split(" ")
    if len(a) != len(b): return False
    for i in range(len(b)):
      if not(Command._isVar(b[i]) or a[i] == b[i]):
        return False
    return True
  
  @staticmethod
  def _isVar(str):
    return str.startswith("<") and str.endswith(">")
