import unittest
def reverse_string(str):
    return str[::-1]

class TestReverse(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("ravikumar"),"ramukivar")
        self.assertEqual(reverse_string("sitadevi"),"ivedatis")

if __name__ == "__main__":
    unittest.main()

'''
Execution:

F:\Python Class>python -m unittest test_reversestring -v
test_reverse_string (test_reversestring.TestReverse) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''
