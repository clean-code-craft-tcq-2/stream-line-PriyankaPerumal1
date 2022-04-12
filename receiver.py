import sys
from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html) 


def readFromConsole():
    signal(SIGPIPE,SIG_DFL)
    lines = sys.stdin.readlines()
    return lines

def formulateReadings(stream):
  mergedReadings = []
  for csvReading in stream:
      csvReading = csvReading.strip('\n')
      reading = list(map(float,csvReading.split(',')))
      mergedReadings.append(reading)
  return mergedReadings
  
def GetDataFromConsoleSenderOutput():
  stream = readFromConsole()
  mergedreadings = formulateReadings(stream)
  print("helloo1")
  print(mergedreadings)
  print("helloo again")
