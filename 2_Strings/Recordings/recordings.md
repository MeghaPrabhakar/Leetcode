# Recordings

## Problem : 14. Longest Common Substring

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

## Problem : 1. Two Sum

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

## Problem : 3. Longest Substring Without Repeating Characters

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

## Problem : 5. Longest Palindromic Substring

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

## Problem : 6. Zigzag Conversion

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

## Problem : 8. String to Integer (atoi)

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

## Problem : 9. Palindrome Number

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

## Problem : 12. Integer to Roman

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

## Problem : 13. Roman to Integer

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

## Problem : 14. Longest Common Prefix

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

## Problem : 17. Letter Combinations of a Phone Number

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

## Problem : 20. Valid Parentheses

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

## Problem : 21. Merge Two Sorted Lists

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

## Problem : 28. Find the Index of the First Occurrence in a String

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

## Problem : 38. Count and Say

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

## Problem : 49. Group Anagrams

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

## Problem : 76. Minimum Window Substring

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

## Problem : 125. Valid Palindrome

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

## Problem : 242. Valid Anagram

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

## Problem : 344. Reverse String

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

---

## Problem : 387. First Unique Character in a String

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def firstUniqChar(self, s):
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

---

## Problem : 409. Longest Palindrome

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "abccccdd"
Output: 7

Example 2:
Input: s = "a"
Output: 1

</details>

<details>
<summary>Code</summary>

```python
from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        counts = Counter(s)
        length = 0
        odd_found = False

        for count in counts.values():
            length += count // 2 * 2
            if count % 2 == 1:
                odd_found = True

        return length + 1 if odd_found else length
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Problem : 451. Sort Characters By Frequency

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "tree"
Output: "eert"

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"

</details>

<details>
<summary>Code</summary>

```python
from collections import Counter

class Solution:
    def frequencySort(self, s):
        counts = Counter(s)
        sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return ''.join(ch * count for ch, count in sorted_chars)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n log n)
Space Complexity: O(n)

</details>

---

## Problem : 657. Robot Return to Origin

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: moves = "UD"
Output: true

Example 2:
Input: moves = "LL"
Output: false

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return x == 0 and y == 0
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Problem : 819. Most Common Word

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

</details>

<details>
<summary>Code</summary>

```python
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = [word.lower() for word in re.findall(r"[a-z']+", paragraph)]
        counts = Counter(word for word in words if word not in banned)
        return counts.most_common(1)[0][0]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Problem : 929. Unique Email Addresses

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            seen.add((local, domain))
        return len(seen)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Problem : 1002. Find Common Characters

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

</details>

<details>
<summary>Code</summary>

```python
from collections import Counter

class Solution:
    def commonChars(self, words):
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)

        result = []
        for ch, count in common.items():
            result.extend([ch] * count)
        return result
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * m)
Space Complexity: O(m)

</details>

---

## Problem : 1047. Remove All Adjacent Duplicates In String

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "abbaca"
Output: "ca"

Example 2:
Input: s = "azxxzy"
Output: "ay"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def removeDuplicates(self, s):
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Problem : 1239. Maximum Length of a Concatenated String with Unique Characters

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def maxLength(self, arr):
        dp = [set()]
        for s in arr:
            if len(set(s)) < len(s):
                continue
            s_set = set(s)
            for prev in dp[:]:
                if s_set & prev:
                    continue
                dp.append(prev | s_set)
        return max(len(s) for s in dp)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(2^n)
Space Complexity: O(2^n)

</details>

---

## Problem : 1392. Longest Happy Prefix

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "level"
Output: "l"

Example 2:
Input: s = "ababab"
Output: "abab"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def longestPrefix(self, s):
        prefix = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = prefix[j - 1]
            if s[i] == s[j]:
                j += 1
            prefix[i] = j
        return s[:prefix[-1]]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Problem : 1512. Number of Good Pairs

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4

Example 2:
Input: nums = [1,1,1,1]
Output: 6

</details>

<details>
<summary>Code</summary>

```python
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums):
        counts = Counter(nums)
        total = 0
        for count in counts.values():
            total += count * (count - 1) // 2
        return total
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Problem : 1662. Check If Two String Arrays are Equivalent

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Problem : 1678. Goal Parser Interpretation

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: command = "G()(al)"
Output: "Goal"

Example 2:
Input: command = "(al)G(al)()"
Output: "alGal"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def interpret(self, command):
        result = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                result.append('G')
                i += 1
            elif command[i:i+2] == '()':
                result.append('o')
                i += 2
            else:
                result.append('al')
                i += 4
        return ''.join(result)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Problem : 2114. Maximum Number of Words Found in Sentences

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6

Example 2:
Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def mostWordsFound(self, sentences):
        return max(len(sentence.split()) for sentence in sentences)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Problem : 2224. Minimum Number of Operations to Convert Time

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: current = "09:41", correct = "10:00"
Output: 2

Example 2:
Input: current = "00:00", correct = "00:00"
Output: 0

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def convertTime(self, current, correct):
        start = int(current[:2]) * 60 + int(current[3:])
        end = int(correct[:2]) * 60 + int(correct[3:])
        diff = end - start
        ops = [60, 15, 5, 1]
        count = 0

        for op in ops:
            count += diff // op
            diff %= op
        return count
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(1)
Space Complexity: O(1)

</details>

---

## Problem : 2351. First Letter to Appear Twice

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "abccbaacz"
Output: "c"

Example 2:
Input: s = "abcdd"
Output: "d"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def repeatedCharacter(self, s):
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Problem : 2710. Remove Trailing Zeros From a String

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "51230100"
Output: "512301"

Example 2:
Input: s = "123"
Output: "123"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def removeTrailingZeros(self, num):
        while num and num[-1] == '0':
            num = num[:-1]
        return num
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Problem : 2744. Find Maximum Number of String Pairs

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: words = ["ab","ba","abc","cba"]
Output: 2

Example 2:
Input: words = ["ll","lb","bb","lb"]
Output: 1

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def maximumNumberOfStringPairs(self, words):
        seen = set()
        pairs = 0
        for word in words:
            rev = word[::-1]
            if rev in seen:
                pairs += 1
            seen.add(word)
        return pairs
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Problem : 2942. Find Words Containing Character

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: words = ["leet","code"], x = "e"
Output: [0,1]

Example 2:
Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def findWordsContaining(self, words, x):
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * m)
Space Complexity: O(k)

</details>

---

## Problem : 3079. Find the Sum of Encrypted Integers

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [10,21,12]
Output: 18

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def sumOfEncryptedInt(self, nums):
        result = 0
        for num in nums:
            digits = sorted(str(num))
            max_digit = digits[-1]
            encrypted = int(max_digit * len(digits))
            result += encrypted
        return result
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * d)
Space Complexity: O(d)

</details>
