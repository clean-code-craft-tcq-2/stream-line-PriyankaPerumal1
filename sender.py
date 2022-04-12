import sender_stub

from signal import signal, SIGPIPE, SIG_DFL  
signal(SIGPIPE,SIG_DFL) 

def celcius_to_Farenheit_convertor(temperature):
    return round(((temperature * 1.8) + 32),2)

def A2D_convertor(current):
    return abs(round(current*10/4094))
    
def pre_process(current,temperature):
    return A2D_convertor(current),celcius_to_Farenheit_convertor(temperature)

def sender_data(no_of_readings):
    readings = []
    for i in range(no_of_readings):
        current = sender_stub.get_currentReadings()
        temperature = sender_stub.get_temperatureReadings()
        current,temperature = pre_process(current,temperature)
        readings.append([current,temperature])
        print("{}, {}".format(current,temperature))
    return readings

if __name__ == "__main__":
    sender_data(50)
