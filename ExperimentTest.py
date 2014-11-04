import unittest
import Experiment

class MyTestCase(unittest.TestCase):
  def test_t6(self):
    r1 = Experiment.largest([-3,-2,-3,-1,-4]) 
    self.assertEqual(r1, -1)

  def test_t7(self):
    self.assertRaises(ValueError, Experiment.largest, [])

if __name__ == '__main__':
  unittest.main()
