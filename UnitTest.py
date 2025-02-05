from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ("bank", "kanb", True), 2: ("attack", "defend", False), 
                            3: ("kelb", "kelb", True), 4: ("abcd", "dcba", False), 
                            5: ("abcd", "abcd", True), 6: ("abc", "bca", False),
                            7: ("abc", "cab", False), 8: ("abc", "abc", True),
                            9: ("sex", "xes", True), 10: ("fax", "fax", True)}
        self.__sol = Solution()
        return super().setUp()
    
    @timeout(1)
    def test_case_1(self):
        s1,s2,output = self.__testcases[1]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)

    @timeout(1)
    def test_case_2(self):
        s1,s2,output = self.__testcases[2]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)
    
    @timeout(1)
    def test_case_3(self):
        s1,s2,output = self.__testcases[3]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)

    @timeout(1)
    def test_case_4(self):
        s1,s2,output = self.__testcases[4]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)
    
    @timeout(1)
    def test_case_5(self):
        s1,s2,output = self.__testcases[5]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)
    
    @timeout(1)
    def test_case_6(self):
        s1,s2,output = self.__testcases[6]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)

    @timeout(1)
    def test_case_7(self):
        s1,s2,output = self.__testcases[7]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)
    
    @timeout(1)
    def test_case_8(self):
        s1,s2,output = self.__testcases[8]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)
    
    @timeout(1)
    def test_case_9(self):
        s1,s2,output = self.__testcases[9]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)

    @timeout(1)
    def test_case_10(self):
        s1,s2,output = self.__testcases[10]
        self.assertEqual(self.__sol.areAlmostEqual(s1,s2), output)
        

if __name__ == "__main__":
    unittest.main()