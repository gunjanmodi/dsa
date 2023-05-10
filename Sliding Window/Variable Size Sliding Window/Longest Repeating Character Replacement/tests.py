import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "ABAB"
        k = 2
        self.assertEqual(4, Solution().characterReplacement(s, k))

    def test_case_2(self):
        s = "AABABBA"
        k = 1
        self.assertEqual(4, Solution().characterReplacement(s, k))

    def test_case_3(self):
        s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
        k = 4
        self.assertEqual(7, Solution().characterReplacement(s, k))


if __name__ == '__main__':
    unittest.main()
