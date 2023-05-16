import unittest
from geezify import Geezify
from test_data import TESTDATA

class TestGeezify(unittest.TestCase):
    def test_geezify_for_all_test_cases(self):
        for x in TESTDATA:
            print(f"{x[0]} => {x[1]}")
            print(f"{x[1]} == {Geezify.geezify(x[0])}")
            self.assertEqual(x[1], Geezify.geezify(x[0]))

if __name__ == '__main__':
    unittest.main()