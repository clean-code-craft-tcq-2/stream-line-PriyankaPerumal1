import unittest
import receiver

class receiver_test(unittest.TestCase):

    def test_GetDataFromConsoleSenderOutput(self):
        SampleSizeForSMA = 5
        receiver.GetDataFromConsoleSenderOutput(SampleSizeForSMA)

if __name__ == '__main__':
  unittest.main()
