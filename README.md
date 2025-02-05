# [1790. Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal)

**Type:** Easy <br>
**Topics:** Hash Table, String, Counting
<hr>

You are given two strings `s1` and `s2` of equal length. A **string swap** is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return `true` *if it is possible to make both strings equal by performing **at most one string swap** on **exactly one** of the strings*. Otherwise, return `false`.
<hr>

- ### Examples:
    - **Example 1:**
        ```
        Input: s1 = "bank", s2 = "kanb"
        Output: true
        Explanation: For example, swap the first character with the last character of s2 to make "bank".
        ```
    - **Example 2:**
        ```
        Input: s1 = "attack", s2 = "defend"
        Output: false
        Explanation: It is impossible to make them equal with one string swap.
        ```
    - **Example 3:**
        ```
        Input: s1 = "kelb", s2 = "kelb"
        Output: true
        Explanation: The two strings are already equal, so no string swap operation is required.
        ```
<hr>

- ### Constraints:
    - `1 <= s1.length, s2.length <= 100`
    - `s1.length == s2.length`
    - `s1` and `s2` consist of only lowercase English letters.
<hr>

- ### Hints:
    - The answer is false if the number of nonequal positions in the strings is not equal to 0 or 2.
    - Check that these positions have the same set of characters.
<hr>