import unittest
import sender
import sender_stub

class sender_test(unittest.TestCase):

    def test_A2D_convertor(self):
        self.assertTrue(sender.A2D_convertor(10) == 0)
        self.assertTrue(sender.A2D_convertor(1000) == 2)
        self.assertTrue(sender.A2D_convertor(4092) == 10)
        
    def test_celcius_to_Farenheit_convertor(self):
        self.assertTrue(sender.celcius_to_Farenheit_convertor(20) == 68.0)
        self.assertTrue(sender.celcius_to_Farenheit_convertor(40) == 104.0)
    
    def test_pre_process(self):
        self.assertTrue(sender.pre_process(0,0) == (0,32.0))
        self.assertTrue(sender.pre_process(10,20) == (0,68.0))
    
    def test_sender_data(self):
        self.assertTrue(len(sender.sender_data(50)) == 50)
    
    def test_generate_randomReadings(self):
        self.assertTrue(sender_stub.generate_randomReadings(0,10) in range(0,10))

    def test_get_currentReadings(self):
        self.assertTrue(sender_stub.get_currentReadings() in range(0, 4094))

    def test_get_temperatureReadings(self):
        self.assertTrue(sender_stub.get_temperatureReadings() in range(0,45))

if __name__ == '__main__':
  unittest.main()