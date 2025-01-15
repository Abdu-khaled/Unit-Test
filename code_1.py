import unittest

from fun1 import CarSpeed

class CarSpeedTest(unittest.TestCase):
    def test_speed(self):
        self.assertEqual(CarSpeed(-1), "Invalid")
        self.assertEqual(CarSpeed(0), "Low")
        self.assertEqual(CarSpeed(39), "Low")
        self.assertEqual(CarSpeed(40), "Normal")
        self.assertEqual(CarSpeed(119), "Normal")
        self.assertEqual(CarSpeed(120), "High")
        self.assertEqual(CarSpeed(199), "High")
        self.assertEqual(CarSpeed(200), "V.High")
        self.assertEqual(CarSpeed(219), "V.High")
        self.assertEqual(CarSpeed(220),"V.High")
        

if __name__ == "__main__":
    unittest.main()