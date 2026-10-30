# Recordings

<details>
<summary><strong>✅ Q1 : Longest Common Prefix</strong></summary>

<details>
<summary>Details</summary>

#14,Easy,Topic1<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+14+Longest+Common+Prefix+solution), [LeetCode #14](https://leetcode.com/problems/longest-common-prefix/)

</details>

<details>
<summary>recording</summary>

[#14_Longest Common Prefix](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Write a function to find the longest common prefix string among an array of strings. If there is no common prefix, return an empty string.

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Example 3:
Input: strs = ["leetcode","leets","leetcode"]
Output: "lee"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        max_len_psbl = len(min(strs, key=len))
        i = 0
        possibilities = []
        while i < len(strs):
            possibilities.append((strs[i][0:max_len_psbl]))
            i += 1
        print(possibilities)
        for i in range(len(possibilities)-1):
            while(possibilities[i][0:max_len_psbl] != possibilities[i+1][0:max_len_psbl]):
                print(possibilities[i], possibilities[i+1])
                max_len_psbl -= 1
                print(max_len_psbl)
        return possibilities[0][0:max_len_psbl]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * m)
Space Complexity: O(1)

</details>

</details>

<details>
<summary><strong>✅ Q2 : Valid Palindrome</strong></summary>

<details>
<summary>Details</summary>

#125,Easy,Topic3<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+125+Valid+Palindrome+solution), [LeetCode #125](https://leetcode.com/problems/valid-palindrome/)

</details>

<details>
<summary>recording</summary>

[#125_Valid Palindrome](#)

</details>

<details>
<summary>Sample Input & Output</summary>

A phrase is a palindrome if, after converting all uppercase letters into lowercase and removing all non-alphanumeric characters, it reads the same forward and backward. Given a string s, return true if it is a palindrome, otherwise false.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false

Example 3:
Input: s = " "
Output: true

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

</details>

<details>
<summary><strong>✅ Q3 : Valid Anagram</strong></summary>

<details>
<summary>Details</summary>

#242,Easy,Topic4<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+242+Valid+Anagram+solution), [LeetCode #242](https://leetcode.com/problems/valid-anagram/)

</details>

<details>
<summary>recording</summary>

[#242_Valid Anagram](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Example 3:
Input: s = "aacc", t = "ccac"
Output: false

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n log n)
Space Complexity: O(n)

</details>

</details>

<details>
<summary><strong>✅ Q4 : First Unique Character in a String</strong></summary>

<details>
<summary>Details</summary>

#387,Easy,Topic2<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+387+First+Unique+Character+in+a+String+solution), [LeetCode #387](https://leetcode.com/problems/first-unique-character-in-a-string/)

</details>

<details>
<summary>recording</summary>

[#387_First Unique Character in a String](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

</details>
