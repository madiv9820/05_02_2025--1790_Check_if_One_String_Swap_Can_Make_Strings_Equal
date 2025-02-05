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