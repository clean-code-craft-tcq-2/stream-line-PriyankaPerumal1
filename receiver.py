import sys
from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
signal(SIGPIPE,SIG_DFL) 


def GetDataFromConsoleSenderOutput():
  print("i am here")
  for line in sys.stdin:
     line=line.split(',')
     print(line)
