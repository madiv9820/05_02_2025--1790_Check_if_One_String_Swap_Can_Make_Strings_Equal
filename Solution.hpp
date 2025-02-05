#include <string>
using namespace std;

class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        // If the strings are already equal, no need for any swaps
        if(s1 == s2) 
            return true;
        
        // Initialize two pointers, one starting from the beginning (left) and one from the end (right)
        int left = 0, right = s1.size() - 1;

        // Move the left pointer to the right until we find the 
        // first character that is different in both strings
        while(s1[left] == s2[left]) ++left;
        
        // Move the right pointer to the left until we find the 
        // first character that is different in both strings
        while(s1[right] == s2[right]) --right;
        
        // Swap the characters at the left and right pointers
        swap(s1[left], s1[right]);

        // After the potential swap, check if the strings are now equal
        return s1 == s2;
    }  
};