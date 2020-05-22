import unittest
import calculator

class TestStringMethods(unittest.TestCase):

    def test_emptyString(self):
        self.assertEqual(calculator.Add(""), 0)

    def test_lengthOneString(self):
        self.assertEqual(calculator.Add("3"), 3)
    
    def test_lengthTwoString(self):
        self.assertEqual(calculator.Add("1,4"), 5)

    def test_lengthFiveString(self):
        self.assertEqual(calculator.Add("1,1,3,4,6"), 15)
    
    def test_stringWithNewLines(self):
        self.assertEqual(calculator.Add("5\n2,3,2\n1"), 13)
    
    def test_customDelimeter(self):
        self.assertEqual(calculator.Add("//;\n5;2;3;2;1"), 13)

    @unittest.expectedFailure
    def test_negativeNumbers(self):
        calculator.Add("//;\n5;-2;0")

if __name__ == '__main__':
    unittest.main()