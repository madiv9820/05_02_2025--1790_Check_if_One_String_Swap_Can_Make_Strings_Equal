# 1790. Check if One String Swap Can Make Strings Equal (All Approaches)
- ## Approach 1:- Frequency Map With Check Difference
    - ### Intuition:
        The goal is to check if two strings can be made equal by performing at most one swap of characters. This means that:
        1. **Character Frequency Check**: Both strings must have the exact same frequency of characters. If this is not the case, they can never be made equal by a swap.
        2. **Mismatch Count**: We need to check how many positions differ between the two strings. If there are exactly 2 mismatches, it’s possible to swap the characters at those positions to make the strings equal. If there are more than 2 mismatches, one swap won't be enough to make the strings equal.

    - ### Approach:
        1. **Frequency Check**: 
            - We loop through both strings and count the occurrences of each character. We store these counts in a 2D list `freq` where:
                    - `freq[i][0]` represents the count of character `i` in string `s1`.
                    - `freq[i][1]` represents the count of character `i` in string `s2`.
            - If the frequency of any character differs between the two strings, we return `False` immediately.
        2. **Mismatch Count**: 
            - After ensuring the frequencies are the same, we compare the strings character by character.
            - For each mismatch, we increment a counter `mismatchCount`.
        3. **Final Decision**: 
            - If the `mismatchCount` is 2 or less, it means that a single swap could potentially make the strings equal. We return `True`.
            - If there are more than 2 mismatches, it is impossible to make the strings equal with just one swap, so we return `False`.

    - ### Code Implementation:
        - **Python Solution:**
            ```python3 []
            class Solution:
                def areAlmostEqual(self, s1: str, s2: str) -> bool:
                    # Create a 2D list to store the frequency count of characters in both strings
                    # freq[i][0] will store the frequency of character 'i' in s1, freq[i][1] in s2
                    freq = [[0] * 2 for _ in range(26)]
                    
                    # Get the length of the strings
                    n = len(s1)

                    # Loop through the strings and count the frequency of each character in both s1 and s2
                    for i in range(n):
                        # Ord value of a character minus 97 gives its position in the alphabet (0 for 'a', 1 for 'b', ..., 25 for 'z')
                        # Increment the frequency for s1 and s2 at the corresponding character index
                        freq[ord(s1[i]) - 97][0] += 1  # Increment frequency for s1
                        freq[ord(s2[i]) - 97][1] += 1  # Increment frequency for s2
                    
                    # Check if both strings have the same frequency for each character
                    for i in range(26):
                        if freq[i][0] != freq[i][1]:
                            # If there's any mismatch in frequencies, return False
                            return False
                    
                    # Variable to count how many characters are different between s1 and s2
                    mismatchCount = 0

                    # Loop to compare the characters at each position in both strings
                    for i in range(n):
                        if s1[i] != s2[i]:
                            # Count mismatches between s1 and s2
                            mismatchCount += 1

                    # If there are two or fewer mismatched positions, we can swap characters to make the strings equal
                    return mismatchCount <= 2
            ```
        - **C++ Solution:**
            ```cpp []
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
            ```

    - ### Time Complexity:
        - **Step 1 (Frequency Check)**: We iterate through the strings once to count character frequencies. This takes **$O(n)$** time where $n$ is the length of the strings.
        - **Step 2 (Mismatch Count)**: We loop through the strings again to count mismatches, which also takes **$O(n)$** time.
        
        Overall, the time complexity is **$O(n)$** because both the frequency check and mismatch counting each take linear time.

    - ### Space Complexity:
        - **Frequency Count**: We use a 2D list `freq` of size 26x2 to store the frequencies of characters. This requires **$O(1)$** space because the size of this list is constant (only 26 possible characters).
        - **Other Variables**: We use a few integer variables (e.g., `mismatchCount`), which also require **$O(1)$** space.
    
        Overall, the space complexity is **$O(1)$** because the space used does not depend on the size of the input strings.
<hr>

- ## Approach 2:- Only Check Difference
    - ### Intuition:
        We need to check if two strings can be made equal by performing **at most one swap**. The process works as follows:
        1. **Check for Immediate Equality**: If the strings are already equal, no swap is needed, and we return `True` right away.
        2. **Find the First Mismatch**: If the strings are not equal, we search for the first position (from the left) where the characters in `s1` and `s2` differ.
        3. **Find the Last Mismatch**: After identifying the first mismatch from the left, we search for the first mismatch from the right.
        4. **Perform One Swap**: If we find these two mismatches, we attempt to swap them in `s1` and check if the resulting `s1` matches `s2`.

        If after swapping the characters the strings match, it means one swap can make the strings equal, so we return `True`. Otherwise, if the strings don't match after the swap, we return `False`.

    - ### Approach:
        1. **Immediate Check**: First, check if the strings are already equal. If so, return `True` immediately.
        2. **Pointer Setup**: Use two pointers:
            - `left` pointer starts at the beginning of the string.
            - `right` pointer starts at the end of the string.
        3. **Find Mismatches**: Move the `left` pointer to the right until a mismatch is found. Similarly, move the `right` pointer to the left until a mismatch is found.
        4. **Swap the Mismatched Characters**: Once mismatched positions are found, swap the characters at `left` and `right` positions in `s1`.
        5. **Final Comparison**: Check if the modified `s1` is equal to `s2`. If they are, return `True`, indicating that one swap made the strings equal. Otherwise, return `False`.

    - ### Code Implementation
        - **Python Solution:**
            ```python3 []
            class Solution:
                def areAlmostEqual(self, s1: str, s2: str) -> bool:
                    # If both strings are already equal, 
                    # no need to swap, just return True
                    if s1 == s2: 
                        return True

                    # Get the length of the strings
                    n = len(s1)

                    # Initialize two pointers: one at the start(left) 
                    # and one at the end(right) of the strings
                    left, right = 0, n - 1

                    # Convert the strings to lists so we can swap characters
                    s1, s2 = list(s1), list(s2)
                    
                    # Move the left pointer to the right until we find the 
                    # first character that is different in both strings
                    while s1[left] == s2[left]: left += 1
                    
                    # Move the right pointer to the left until we find the 
                    # first character that is different in both strings
                    while s1[right] == s2[right]: right -= 1

                    # Swap the characters at the left and right pointers
                    s1[left], s1[right] = s1[right], s1[left]

                    # After the swap (if any), check if the strings are equal
                    return s1 == s2
            ```
        - **C++ Solution**
            ```cpp []
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
            ```

    - ### Time Complexity:
        - **Finding Mismatches**: We use two `while` loops to find the first mismatch from the left and the first mismatch from the right. Each of these loops runs at most **$O(n)$** time where $n$ is the length of the strings.
        - **Swapping**: The swap operation takes **$O(1)$** time.
        - **Final Comparison**: The comparison `s1 == s2` takes **$O(n)$** time.
        
        Therefore, the overall time complexity is **$O(n)$**.

    - ### Space Complexity:
        - **String Conversion**: For python, we convert the strings `s1` and `s2` into lists, which requires **$O(n)$** space where $n$ is the length of the strings.
        - **Other Variables**: The variables `left`, `right`, and `n` are all constant space usage, i.e., **$O(1)$**.
        
        Overall, the space complexity is **$O(n)$** due to the list conversions for Python, and **$O(1)$** for C++.
<hr>