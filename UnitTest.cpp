#include <iostream>
#include <vector>
#include "Solution.hpp"

class UnitTest {
private:
    vector<pair<pair<string, string>, bool>> testcases;
    Solution sol;
public:
    UnitTest() {
        testcases = {{{"ab", "ba"}, true},
                     {{"ab", "ab"}, true},
                     {{"aa", "aa"}, true},
                     {{"aaaaaaabc", "aaaaaaacb"}, true},
                     {{"", ""}, true},
                     {{"a", "a"}, true},
                     {{"a", "b"}, false},
                     {{"ab", "cd"}, false},
                     {{"ab", "ac"}, false},
                     {{"ab", "bc"}, false}};
    }

    void test() {
        for(auto &testcase : testcases) {
            auto input = testcase.first;
            auto expected = testcase.second;
            auto actual = sol.areAlmostEqual(input.first, input.second);
            if (actual != expected) {
                std::cout << "Test failed!" << std::endl;
                std::cout << "Input: " << input.first << ", " << input.second << std::endl;
                std::cout << "Expected: " << (expected ? "true":"false") << std::endl;
                std::cout << "Actual: " << (actual ? "true":"false") << std::endl;
                return;
            }
        }
        std::cout << "All tests passed!" << std::endl;

    }
};

int main() {
    UnitTest test;
    test.test();
    return 0;
}