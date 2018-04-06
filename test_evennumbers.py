import unittest
def even_numbers(l):
    Flag = True
    for i in l:
        if i%2 == 0:
            Flag = True
        else:
            Flag = False
            break
    return Flag

class TestEvenNumbers(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(even_numbers([2,4,6,8,10]),True)
        self.assertEqual(even_numbers([1,3,5,7,9]),False)

if __name__ == "__main__":
    unittest.main()

'''
Execution:
F:\Python Class>python -m unittest test_evennumbers
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

F:\Python Class>python -m unittest test_evennumbers -v
test_even_numbers (test_evennumbers.TestEvenNumbers) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''
