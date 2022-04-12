import sys, errno
try:
    ### IO operation ###
except IOError as e:
    if e.errno == errno.EPIPE:
        ###Handle the error ###


def GetDataFromConsoleSenderOutput():
  print("i am here")
  for line in sys.stdin:
     line=line.split(',')
     print(line)
