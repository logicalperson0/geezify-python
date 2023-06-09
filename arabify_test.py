import unittest
from arabify import Arabify
from test_data import TESTDATA

class TestArabify(unittest.TestCase):
    def test_arabify_for_all_test_cases(self):
        for x in TESTDATA:
            print(f"{x[1]} => {x[0]}")
            print(f"{x[0]} == {Arabify.arabify(x[1])}")
            self.assertEqual(x[0], Arabify.arabify(x[1]))

if __name__ == '__main__':
    unittest.main()
