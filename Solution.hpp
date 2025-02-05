#include <string>
using namespace std;

class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        // Array to store the frequency count of characters in s1 and s2
        // freq[i][0] stores frequency of character 'i' in s1, freq[i][1] in s2
        int freq[26][2] = {0};
        
        // Loop through each character in the strings and count their occurrences
        for(int i = 0; i < s1.size(); ++i) {
            // Increment the frequency for s1 and s2 at the respective character positions
            freq[s1[i] - 'a'][0]++; // For s1
            freq[s2[i] - 'a'][1]++; // For s2
        }

        // Check if both strings have the same frequency for each character
        for(int i = 0; i < 26; ++i) {
            if(freq[i][0] != freq[i][1]) {
                // If any character frequency mismatch is found, return false
                return false;
            }
        }

        // Variable to count how many characters are different between the two strings
        int mismatchCount = 0;

        // Loop to find the positions where the characters are different
        for(int i = 0; i < s1.size(); ++i) {
            if(s1[i] != s2[i]) {
                // Count mismatches
                mismatchCount++;
            }
        }

        // If there are two or fewer mismatched characters, they can be swapped to make the strings equal
        return mismatchCount <= 2;
    }
};