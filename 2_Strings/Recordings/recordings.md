# Recordings

<details>
<summary>Q1 : 🟩 Longest Common Prefix — (Topic 1) #14</summary>

<details>
<summary>Details</summary>

#14, Easy, Topic 1<br/>
Useful links: [YouTube](#), [LeetCode #14](#)

</details>

<details>
<summary>Recording</summary>

[#14_Longest Common Prefix](#)

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
    def longestCommonPrefix(self, strs: list[str]) -> str:
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

</details>

<details>
<summary>Q2 : 🟩 Valid Palindrome — (Topic 3) #125</summary>

<details>
<summary>Details</summary>

#125, Easy, Topic 3<br/>
Useful links: [YouTube](#), [LeetCode #125](#)

</details>

<details>
<summary>Recording</summary>

[#125_Valid Palindrome](#)

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
<summary>Q3 : 🟩 Valid Anagram — (Topic 4) #242</summary>

<details>
<summary>Details</summary>

#242, Easy, Topic 4<br/>
Useful links: [YouTube](#), [LeetCode #242](#)

</details>

<details>
<summary>Recording</summary>

[#242_Valid Anagram](#)

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
<summary>Q4 : 🟩 First Unique Character in a String — (Topic 2) #387</summary>

<details>
<summary>Details</summary>

#387, Easy, Topic 2<br/>
Useful links: [YouTube](#), [LeetCode #387](#)

</details>

<details>
<summary>Recording</summary>

[#387_First Unique Character in a String](#)

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

<details>
<summary>Q5 : 🟩 Is Subsequence — (Topic 5) #392</summary>

<details>
<summary>Details</summary>

#392, Easy, Topic 5<br/>
Useful links: [YouTube](#), [LeetCode #392](#)

</details>

<details>
<summary>Recording</summary>

[#392_Is Subsequence](#)

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
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

</details>

<details>
<summary>Q6 : 🟩 Reverse String — (Topic 1) #344</summary>

<details>
<summary>Details</summary>

#344, Easy, Topic 1<br/>
Useful links: [YouTube](#), [LeetCode #344](#)

</details>

<details>
<summary>Recording</summary>

[#344_Reverse String](#)

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
    def reverseString(self, s: list[str]) -> None:
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

</details>

<details>
<summary>Q7 : 🟩 Reverse Words in a String III — (Topic 1) #557</summary>

<details>
<summary>Details</summary>

#557, Easy, Topic 1<br/>
Useful links: [YouTube](#), [LeetCode #557](#)

</details>

<details>
<summary>Recording</summary>

[#557_Reverse Words in a String III](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return ' '.join(word[::-1] for word in words)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

</details>

<details>
<summary>Q8 : 🟨 Group Anagrams — (Topic 4) #49</summary>

<details>
<summary>Details</summary>

#49, Medium, Topic 4<br/>
Useful links: [YouTube](#), [LeetCode #49](#)

</details>

<details>
<summary>Recording</summary>

[#49_Group Anagrams](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

</details>

<details>
<summary>Code</summary>

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            groups[tuple(sorted(word))].append(word)
        return list(groups.values())
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n * k log k)
Space Complexity: O(n * k)

</details>

</details>

<details>
<summary>Q9 : 🟨 String Compression — (Topic 7) #443</summary>

<details>
<summary>Details</summary>

#443, Medium, Topic 7<br/>
Useful links: [YouTube](#), [LeetCode #443](#)

</details>

<details>
<summary>Recording</summary>

[#443_String Compression](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: 7

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        ans = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            chars[ans] = chars[i]
            ans += 1
            if j - i > 1:
                for digit in str(j - i):
                    chars[ans] = digit
                    ans += 1
            i = j
        return ans
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

</details>

<details>
<summary>Q10 : 🟨 Longest Palindromic Substring — (Topic 3) #5</summary>

<details>
<summary>Details</summary>

#5, Medium, Topic 3<br/>
Useful links: [YouTube](#), [LeetCode #5](#)

</details>

<details>
<summary>Recording</summary>

[#5_Longest Palindromic Substring](#)

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
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        best = s[0]
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(best):
                    best = s[l:r+1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(best):
                    best = s[l:r+1]
                l -= 1
                r += 1
        return best
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n^2)
Space Complexity: O(1)

</details>

</details>

<details>
<summary>Q11 : 🟨 Longest Substring Without Repeating Characters — (Topic 5) #3</summary>

<details>
<summary>Details</summary>

#3, Medium, Topic 5<br/>
Useful links: [YouTube](#), [LeetCode #3](#)

</details>

<details>
<summary>Recording</summary>

[#3_Longest Substring Without Repeating Characters](#)

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
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        best = 0
        for right, ch in enumerate(s):
            if ch in seen:
                left = max(left, seen[ch] + 1)
            seen[ch] = right
            best = max(best, right - left + 1)
        return best
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(min(n, k))

</details>

</details>

<details>
<summary>Q12 : 🟨 Longest Repeating Character Replacement — (Topic 5) #424</summary>

<details>
<summary>Details</summary>

#424, Medium, Topic 5<br/>
Useful links: [YouTube](#), [LeetCode #424](#)

</details>

<details>
<summary>Recording</summary>

[#424_Longest Repeating Character Replacement](#)

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
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

</details>

<details>
<summary>Q13 : 🟨 Find All Anagrams in a String — (Topic 4) #438</summary>

<details>
<summary>Details</summary>

#438, Medium, Topic 4<br/>
Useful links: [YouTube](#), [LeetCode #438](#)

</details>

<details>
<summary>Recording</summary>

[#438_Find All Anagrams in a String](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]

</details>

<details>
<summary>Code</summary>

```python
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        need = Counter(p)
        window = Counter()
        left = 0
        ans = []
        for right, ch in enumerate(s):
            window[ch] += 1
            while right - left + 1 > len(p):
                left_ch = s[left]
                window[left_ch] -= 1
                if window[left_ch] == 0:
                    del window[left_ch]
                left += 1
            if window == need:
                ans.append(left)
        return ans
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(k)

</details>

</details>

<details>
<summary>Q14 : 🟨 Decode String — (Topic 6) #394</summary>

<details>
<summary>Details</summary>

#394, Medium, Topic 6<br/>
Useful links: [YouTube](#), [LeetCode #394](#)

</details>

<details>
<summary>Recording</summary>

[#394_Decode String](#)

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
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                sub = ''
                while stack and stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * sub)
        return ''.join(str(x) for x in stack)
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

</details>

<details>
<summary>Q15 : 🟨 String to Integer (atoi) — (Topic 6) #8</summary>

<details>
<summary>Details</summary>

#8, Medium, Topic 6<br/>
Useful links: [YouTube](#), [LeetCode #8](#)

</details>

<details>
<summary>Recording</summary>

[#8_String to Integer (atoi)](#)

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
    def myAtoi(self, s: str) -> int:
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
            num = num * 10 + int(ch)
        return max(-2**31, min(sign * num, 2**31 - 1))
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

</details>

<details>
<summary>Q16 : 🟨 Encode and Decode Strings — (Topic 6) #271</summary>

<details>
<summary>Details</summary>

#271, Medium, Topic 6<br/>
Useful links: [YouTube](#), [LeetCode #271](#)

</details>

<details>
<summary>Recording</summary>

[#271_Encode and Decode Strings](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: words = ["lint","code","love","you"]
Output: "4#lint4#code4#love3#you"

</details>

<details>
<summary>Code</summary>

```python
class Codec:
    def encode(self, strs: list[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

</details>

<details>
<summary>Q17 : 🟨 Palindromic Substrings — (Topic 3) #647</summary>

<details>
<summary>Details</summary>

#647, Medium, Topic 3<br/>
Useful links: [YouTube](#), [LeetCode #647](#)

</details>

<details>
<summary>Recording</summary>

[#647_Palindromic Substrings](#)

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
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n^2)
Space Complexity: O(1)

</details>

</details>

<details>
<summary>Q18 : 🟧 Minimum Window Substring — (Topic 5) #76</summary>

<details>
<summary>Details</summary>

#76, Hard, Topic 5<br/>
Useful links: [YouTube](#), [LeetCode #76](#)

</details>

<details>
<summary>Recording</summary>

[#76_Minimum Window Substring](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

</details>

<details>
<summary>Code</summary>

```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        best = (float('inf'), None, None)
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        if best[1] is None:
            return ""
        return s[best[1]:best[2] + 1]
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(k)

</details>

</details>

<details>
<summary>Q19 : 🟧 Regular Expression Matching — (Topic 8) #10</summary>

<details>
<summary>Details</summary>

#10, Hard, Topic 8<br/>
Useful links: [YouTube](#), [LeetCode #10](#)

</details>

<details>
<summary>Recording</summary>

[#10_Regular Expression Matching](#)

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
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2, len(p) + 1):
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

</details>

<details>
<summary>Q20 : 🟧 Edit Distance — (Topic 8) #72</summary>

<details>
<summary>Details</summary>

#72, Hard, Topic 8<br/>
Useful links: [YouTube](#), [LeetCode #72](#)

</details>

<details>
<summary>Recording</summary>

[#72_Edit Distance](#)

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
    def minDistance(self, word1: str, word2: str) -> int:
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

</details>
