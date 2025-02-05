from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ("bank", "kanb", True), 2: ("attack", "defend", False), 
                            3: ("kelb", "kelb", True), 4: ("abcd", "dcba", False), 
                            5: ("abcd", "abcd", True), 6: ("abc", "bca", True),
                            7: ("abc", "cab", False), 8: ("abc", "abc", True),
                            9: ("sex", "xes", True), 10: ("fax", "fax", True)}
        self.__sol = Solution()
        return super().setUp()
    
    @timeout(1)
    def test_solution(self):
        for key in self.__testcases:
            self.assertEqual(self.__sol.areAlmostEqual(self.__testcases[key][0], self.__testcases[key][1]), self.__testcases[key][2])

if __name__ == "__main__":
    unittest.main()