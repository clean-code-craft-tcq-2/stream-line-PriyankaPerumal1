from random import randint

def generate_randomReadings(minLimit,maxLimit):
    return randint(minLimit, maxLimit)

def get_currentReadings():
    return generate_randomReadings(0, 4094)

def get_temperatureReadings():
    return generate_randomReadings(0,45)