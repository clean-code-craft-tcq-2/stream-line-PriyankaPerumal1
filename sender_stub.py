from random import randint

from signal import signal, SIGPIPE, SIG_DFL  
signal(SIGPIPE,SIG_DFL) 

def generate_randomReadings(minLimit,maxLimit):
    return randint(minLimit, maxLimit)

def get_currentReadings():
    return generate_randomReadings(0, 4094)

def get_temperatureReadings():
    return generate_randomReadings(0,45)
