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