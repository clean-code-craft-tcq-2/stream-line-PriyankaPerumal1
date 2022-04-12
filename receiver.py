import sys
from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
signal(SIGPIPE,SIG_DFL) 


def segregateTemperatureandChargerate(line,temperature,charge_rate):
  index=0
  if "temperature" in line[index]:
    while(not("charge_rate" in line[index])):
      temperature.append(line[index])
      index = index+1
    for i in range(index,len(line)):
      charge_rate.append(line[i])
  return temperature,charge_rate

def GetDataFromConsoleSenderOutput():
  for line in sys.stdin:
    temperature = []
    charge_rate = []
    
    line=line.split(',')
    temperature,charge_rate = segregateTemperatureandChargerate(line,temperature,charge_rate)
    print(temperature,charge_rate)
