# Recordings

## Q1 : (LC14)Longest Common Substring

<details>
<summary>recording_problem_name</summary>

[14. Longest Common Substring](https://raw.githubusercontent.com/MeghaPrabhakar/Leetcode/main/2_Strings/Recordings/14.%20Longest%20Common%20Substring.mp3)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * m)
Space Complexity: O(1)

</details>

---

## Q2 : (LC1)Two Sum

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], i]
            seen[num] = i
        return []
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Q3 : (LC3)Longest Substring Without Repeating Characters

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "abcabcbb"
Output: 3

Example 2:
Input: s = "bbbbb"
Output: 1

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        seen = {}
        longest = 0

        for right, ch in enumerate(s):
            if ch in seen:
                left = max(left, seen[ch] + 1)
            seen[ch] = right
            longest = max(longest, right - left + 1)

        return longest
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(min(n, 256))

</details>

---

## Q4 : (LC5)Longest Palindromic Substring

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "babad"
Output: "bab"

Example 2:
Input: s = "cbbd"
Output: "bb"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""

        start, max_len = 0, 1
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start, max_len = l, r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start, max_len = l, r - l + 1
                l -= 1
                r += 1

        return s[start:start + max_len]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n^2)
Space Complexity: O(1)

</details>

---

## Q5 : (LC6)Zigzag Conversion

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        cur_row = 0
        going_down = False

        for ch in s:
            rows[cur_row] += ch
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return "".join(rows)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Q6 : (LC8)String to Integer (atoi)

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "42"
Output: 42

Example 2:
Input: s = "   -42"
Output: -42

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] in '+-':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        num = 0
        for ch in s:
            if not ch.isdigit():
                break
            num = num * 10 + (ord(ch) - ord('0'))
            if sign == 1 and num > 2**31 - 1:
                return 2**31 - 1
            if sign == -1 and num > 2**31:
                return -(2**31)

        return sign * num
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Q7 : (LC9)Palindrome Number

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        original = x
        reversed_x = 0

        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        return reversed_x == original
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(log n)
Space Complexity: O(1)

</details>

---

## Q8 : (LC12)Integer to Roman

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 58
Output: "LVIII"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""

        for v, n in zip(values, numerals):
            while num >= v:
                result += n
                num -= v

        return result
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(1)
Space Complexity: O(1)

</details>

---

## Q9 : (LC13)Roman to Integer

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "MCMXCIV"
Output: 1994

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def romanToInt(self, s):
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Q10 : (LC14)Longest Common Prefix

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * m)
Space Complexity: O(1)

</details>

---

## Q11 : (LC17)Letter Combinations of a Phone Number

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = [""]

        for digit in digits:
            letters = mapping[digit]
            result = [prefix + letter for prefix in result for letter in letters]

        return result
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(4^n)
Space Complexity: O(4^n)

</details>

---

## Q12 : (LC20)Valid Parentheses

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(]"
Output: false

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                return False

        return not stack
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Q13 : (LC21)Merge Two Sorted Lists

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return dummy.next
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n + m)
Space Complexity: O(1)

</details>

---

## Q14 : (LC28)Find the Index of the First Occurrence in a String

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * m)
Space Complexity: O(1)

</details>

---

## Q15 : (LC38)Count and Say

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: n = 1
Output: "1"

Example 2:
Input: n = 4
Output: "1211"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def countAndSay(self, n):
        s = "1"
        for _ in range(1, n):
            next_s = ""
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                next_s += str(count) + s[i]
                i += 1
            s = next_s
        return s
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * length)
Space Complexity: O(length)

</details>

---

## Q16 : (LC49)Group Anagrams

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            key = tuple(sorted(word))
            groups.setdefault(key, []).append(word)
        return list(groups.values())
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * k log k)
Space Complexity: O(n * k)

</details>

---

## Q17 : (LC76)Minimum Window Substring

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "aa"
Output: ""

</details>

<details>
<summary>Code</summary>

```python
from collections import Counter

class Solution:
    def minWindow(self, s, t):
        need = Counter(t)
        missing = len(t)
        left = 0
        best = (-1, float('inf'))

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if right - left + 1 < best[1]:
                    best = (left, right - left + 1)
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        if best[0] == -1:
            return ""
        return s[best[0]:best[0] + best[1]]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(k)

</details>

---

## Q18 : (LC125)Valid Palindrome

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def isPalindrome(self, s):
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Q19 : (LC242)Valid Anagram

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n log n)
Space Complexity: O(n)

</details>

---

## Q20 : (LC344)Reverse String

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>
