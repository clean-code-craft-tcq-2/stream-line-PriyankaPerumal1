import sys
from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html) 

BMSparameters = ["current", "temperature"]

def readDataFromConsole():
    signal(SIGPIPE,SIG_DFL)
    lines = sys.stdin.readlines()
    return lines

def formulateReadingsToProperFormat(stream):
  ArrayOfReadings = []
  for Reading in stream:
      Reading = Reading.strip('\n')
      readingList = list(map(float,Reading.split(',')))
      ArrayOfReadings.append(readingList)
  return ArrayOfReadings

def getParamindex(parameter):
    for index, parameterName in enumerate(BMSparameters):
        if parameterName == parameter:
            return index
        
def extractParameterReading(ArrayOfReadings, param):
    ParamIndex = getParamindex(param)
    return [readings[ParamIndex] for readings in ArrayOfReadings]

def createWindow(readings, windowSize):
    windows = [readings[index : index + windowSize] for index, value in enumerate(readings) if index < len(readings) - windowSize + 1]
    return windows

def roundOffAverage(value, digits):
    return round(value, digits)

def calculateAverage(array):
    return calculateSum(array) / len(array)

def calculateSum(array):
    return sum(array)

def calculateMovingAverage(readings, windowSize):
    windows = createWindow(readings, windowSize)
    movingAverages = [roundOffAverage(calculateAverage(window), 2) for window in windows]
    return movingAverages

def calculateMinMaxReading(readings):
    minReading = calculateMinReading(readings)
    maxReading = calculateMaxReading(readings)
    return {'min': minReading, 'max': maxReading}

def calculateMinReading(readings):
    return min(readings,default="EMPTY")

def calculateMaxReading(readings):
    return max(readings,default="EMPTY")

def convertOperationResultsToCSVFormat(parameter,minMaxReading,movingAverage):
  return f'{parameter}:{minMaxReading},{movingAverage}'

def printOnConsole(string):
    print(string)
    return True

def GetDataFromConsoleSenderOutput():
  datastream = readDataFromConsole()
  ArrayOfReadings = formulateReadingsToProperFormat(datastream)
  for param in BMSparameters:
    readings = extractParameterReading(ArrayOfReadings, param)
    minMaxReading = calculateMinMaxReading(readings)
    movingAverage = calculateMovingAverage(readings, 5)
    formattedOutputString = convertOperationResultsToCSVFormat(param,minMaxReading,movingAverage)
    printOnConsole(formattedOutputString)
