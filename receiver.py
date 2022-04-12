import sys


def GetDataFromConsoleSenderOutput():
  for line in sys.stdin:
     line=line.split(',')
     print(line)
