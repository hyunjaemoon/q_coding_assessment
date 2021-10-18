import unittest
from most_active_cookie import CustomQueue, Solution

"""
@author: Hyun Jae Moon
To run this Python Code, write the following line in the console:

% python testcase.py
"""

class Testing(unittest.TestCase):

    def test_example1(self):
        csvFile = 'cookie_log.csv'
        date = '2018-12-09'
        actual = ['AtY0laUfhglK3lC7']
        s = Solution(csvFile, date)
        expected = s.solve()
        self.assertEqual(actual, expected)

    def test_example2(self):
        csvFile = 'cookie_log.csv'
        date = '2018-12-08'
        actual = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
        s = Solution(csvFile, date)
        expected = s.solve()
        self.assertEqual(actual, expected)

    def test_empty(self):
        csvFile = 'cookie_log.csv'
        date = '2018-12-06'
        actual = []
        s = Solution(csvFile, date)
        expected = s.solve()
        self.assertEqual(actual, expected)

    def test_lastline(self):
        csvFile = 'cookie_log.csv'
        date = '2018-12-07'
        actual = ['4sMM2LxV07bPJzwf']
        s = Solution(csvFile, date)
        expected = s.solve()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
