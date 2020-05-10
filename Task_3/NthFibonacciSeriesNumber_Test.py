#Command to run:
#python NthFibonacciSeriesNumber_Test.py -v

import unittest
import doctest
from NthFibonacciSeriesNumber import NthNumberOfFibonacciSeries

class NthFibonacciSeriesNumber_Test(unittest.TestCase):

    def test_wrongInput(self):
        result = NthNumberOfFibonacciSeries(-100)
        self.assertEqual(result, -1)

    def test_firstElement(self):
        result = NthNumberOfFibonacciSeries(1)
        self.assertEqual(result, 0)

    def test_secondElement(self):
        result = NthNumberOfFibonacciSeries(2)
        self.assertEqual(result, 1)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("./doctest.txt"))
    return tests

if __name__ == '__main__':
    unittest.main()
