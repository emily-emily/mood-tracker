import src.login
import sys

try:
  src.login.login()
except KeyboardInterrupt:
  print("Program exited.")
  sys.exit(0)
