import unittest
from functions import *

class TestEvaluateExpressions(unittest.TestCase):

    def test_evaluatePrefix(self):
        self.assertEqual(evaluatePrefix("+ 1 2"), 3)
        self.assertEqual(evaluatePrefix("- 5 3"), 2)
        self.assertEqual(evaluatePrefix("* 4 2"), 8)
        self.assertEqual(evaluatePrefix("/ 8 2"), 4)
        self.assertEqual(evaluatePrefix("+ * 2 3 4"), 10)
        self.assertEqual(evaluatePrefix("1 2 3"), "1 2 3")

    def test_evaluatePostfix(self):
        self.assertEqual(evaluatePostfix("1 2 +"), 3)
        self.assertEqual(evaluatePostfix("5 3 -"), 2)
        self.assertEqual(evaluatePostfix("4 2 *"), 8)
        self.assertEqual(evaluatePostfix("8 2 /"), 4)
        self.assertEqual(evaluatePostfix("2 3 * 4 +"), 10)
        self.assertEqual(evaluatePostfix("1 2 3"), "1 2 3") 

if __name__ == '__main__':
    unittest.main()
