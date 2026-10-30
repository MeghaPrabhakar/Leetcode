# Recordings

## Q1 : 🟩 Longest Common Prefix — (Topic 1) #14

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

## Q2 : 🟩 Valid Palindrome — (Topic 3) #125

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

## Q3 : 🟩 Valid Anagram — (Topic 4) #242

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

## Q4 : 🟩 First Unique Character in a String — (Topic 2) #387

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
from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        counts = Counter(s)
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

## Q5 : 🟩 Is Subsequence — (Topic 5) #392

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def isSubsequence(self, s, t):
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(len(t))
Space Complexity: O(1)

</details>

---

## Q6 : 🟩 Reverse String — (Topic 1) #344

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

## Q7 : 🟩 Reverse Words in a String III — (Topic 1) #557

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def reverseWords(self, s):
        words = s.split()
        return ' '.join(word[::-1] for word in words)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Q8 : 🟨 Group Anagrams — (Topic 4) #49

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
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)
        return list(groups.values())
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * k log k)
Space Complexity: O(n * k)

</details>

---

## Q9 : 🟨 String Compression — (Topic 7) #443

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6

Example 2:
Input: chars = ["a"]
Output: 1

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def compress(self, chars):
        write = 0
        i = 0
        while i < len(chars):
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                i += 1
                count += 1
            chars[write] = chars[i]
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            i += 1
        return write
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Q10 : 🟨 Longest Palindromic Substring — (Topic 3) #5

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
        start = 0
        max_len = 1

        def expand(l, r):
            nonlocal start, max_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[start:start + max_len]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n^2)
Space Complexity: O(1)

</details>

---

## Q11 : 🟨 Longest Substring Without Repeating Characters — (Topic 5) #3

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

## Q12 : 🟨 Longest Repeating Character Replacement — (Topic 5) #424

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "ABAB", k = 2
Output: 4

Example 2:
Input: s = "AABABBA", k = 1
Output: 4

</details>

<details>
<summary>Code</summary>

```python
from collections import defaultdict

class Solution:
    def characterReplacement(self, s, k):
        counts = defaultdict(int)
        left = 0
        max_count = 0
        longest = 0

        for right, ch in enumerate(s):
            counts[ch] += 1
            max_count = max(max_count, counts[ch])

            while right - left + 1 - max_count > k:
                counts[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

---

## Q13 : 🟨 Find All Anagrams in a String — (Topic 4) #438

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]

</details>

<details>
<summary>Code</summary>

```python
from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        need = Counter(p)
        window = Counter()
        left = 0
        result = []

        for right, ch in enumerate(s):
            window[ch] += 1
            while window - need < Counter():
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if window == need:
                result.append(left)

        return result
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(k)

</details>

---

## Q14 : 🟨 Decode String — (Topic 6) #394

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def decodeString(self, s):
        stack = []
        current_num = 0
        current_string = ""

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif ch == ']':
                prev_string, repeat = stack.pop()
                current_string = prev_string + current_string * repeat
            else:
                current_string += ch

        return current_string
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

---

## Q15 : 🟨 String to Integer (atoi) — (Topic 6) #8

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
            sign = -1 if s[0] == '-' else 1
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

## Q16 : 🟨 Encode and Decode Strings — (Topic 6) #271

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: words = ["lint","code","love","you"]
Output: "4#lint4#code4#love3#you"

Example 2:
Input: words = ["we","say",":","yes"]
Output: "2#we3#say1#:3#yes"

</details>

<details>
<summary>Code</summary>

```python
class Codec:
    def encode(self, strs):
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length
        return res
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(total characters)
Space Complexity: O(total characters)

</details>

---

## Q17 : 🟨 Palindromic Substrings — (Topic 3) #647

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "abc"
Output: 3

Example 2:
Input: s = "aaa"
Output: 6

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def countSubstrings(self, s):
        count = 0

        def expand(l, r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return count
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n^2)
Space Complexity: O(1)

</details>

---

## Q18 : 🟧 Minimum Window Substring — (Topic 5) #76

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

## Q19 : 🟧 Regular Expression Matching — (Topic 8) #10

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "aa", p = "a"
Output: false

Example 2:
Input: s = "aa", p = "a*"
Output: true

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))

        return dp[len(s)][len(p)]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * m)
Space Complexity: O(n * m)

</details>

---

## Q20 : 🟧 Edit Distance — (Topic 8) #72

<details>
<summary>recording_problem_name</summary>

[Problem recording placeholder](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(m * n)
Space Complexity: O(m * n)

</details>
