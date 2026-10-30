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

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of lowercase English letters

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
        max_len_psbl = len(min(strs, key=len))
        i=0
        possibilities=[]
        while i < len(strs):
            possibilities.append((strs[i][0:max_len_psbl]))
            i+=1
        print(possibilities)
        for i in range(len(possibilities)-1):
            while(possibilities[i][0:max_len_psbl]!=possibilities[i+1][0:max_len_psbl]):
                print(possibilities[i],possibilities[i+1])
                max_len_psbl-=1
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

A phrase is a palindrome if, after converting all uppercase letters into lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string s, return true if it is a palindrome, otherwise false.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters

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

Given two strings s and t, return true if t is an anagram of s and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of another using all the original letters exactly once.

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

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

Given a string s, find the first non-repeating character and return its index.
If no such character exists, return -1.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters

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

</details>

<details>
<summary><strong>✅ Q5 : Is Subsequence</strong></summary>

<details>
<summary>Details</summary>

#392,Easy,Topic5<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+392+Is+Subsequence+solution), [LeetCode #392](https://leetcode.com/problems/is-subsequence/)

</details>

<details>
<summary>recording</summary>

[#392_Is Subsequence](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters

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

</details>

<details>
<summary><strong>✅ Q6 : Reverse String</strong></summary>

<details>
<summary>Details</summary>

#344,Easy,Topic1<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+344+Reverse+String+solution), [LeetCode #344](https://leetcode.com/problems/reverse-string/)

</details>

<details>
<summary>recording</summary>

[#344_Reverse String](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Write a function that reverses a string in-place. The input string is given as a character array s.
You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is a printable ASCII character

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

</details>

<details>
<summary><strong>✅ Q7 : Reverse Words in a String III</strong></summary>

<details>
<summary>Details</summary>

#557,Easy,Topic1<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+557+Reverse+Words+in+a+String+III+solution), [LeetCode #557](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

</details>

<details>
<summary>recording</summary>

[#557_Reverse Words in a String III](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and word order.

Constraints:
- 1 <= s.length <= 10^5
- s contains printable ASCII characters
- s does not contain leading or trailing spaces

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

</details>

<details>
<summary><strong>✅ Q8 : Group Anagrams</strong></summary>

<details>
<summary>Details</summary>

#49,Med.,Topic4<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+49+Group+Anagrams+solution), [LeetCode #49](https://leetcode.com/problems/group-anagrams/)

</details>

<details>
<summary>recording</summary>

[#49_Group Anagrams](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given an array of strings strs, group the anagrams together. Two strings are anagrams if they have the same characters with the same frequency, but different order.

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters

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

</details>

<details>
<summary><strong>✅ Q9 : String Compression</strong></summary>

<details>
<summary>Details</summary>

#443,Med.,Topic7<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+443+String+Compression+solution), [LeetCode #443](https://leetcode.com/problems/string-compression/)

</details>

<details>
<summary>recording</summary>

[#443_String Compression](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Compress a run-length encoded string in-place. Each group of consecutive identical characters should be replaced with the character followed by the count if the count is greater than 1.

Constraints:
- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase letter, digit, or symbol

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

</details>

<details>
<summary><strong>✅ Q10 : Longest Palindromic Substring</strong></summary>

<details>
<summary>Details</summary>

#5,Med.,Topic3<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+5+Longest+Palindromic+Substring+solution), [LeetCode #5](https://leetcode.com/problems/longest-palindromic-substring/)

</details>

<details>
<summary>recording</summary>

[#5_Longest Palindromic Substring](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given a string s, return the longest palindromic substring in s.

Constraints:
- 1 <= s.length <= 1000
- s consists of digits and English letters

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

</details>

<details>
<summary><strong>✅ Q11 : Longest Substring Without Repeating Characters</strong></summary>

<details>
<summary>Details</summary>

#3,Med.,Topic5<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+3+Longest+Substring+Without+Repeating+Characters+solution), [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

</details>

<details>
<summary>recording</summary>

[#3_Longest Substring Without Repeating Characters](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given a string s, find the length of the longest substring without repeating characters.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols, and spaces

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

</details>

<details>
<summary><strong>✅ Q12 : Longest Repeating Character Replacement</strong></summary>

<details>
<summary>Details</summary>

#424,Med.,Topic5<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+424+Longest+Repeating+Character+Replacement+solution), [LeetCode #424](https://leetcode.com/problems/longest-repeating-character-replacement/)

</details>

<details>
<summary>recording</summary>

[#424_Longest Repeating Character Replacement](#)

</details>

<details>
<summary>Sample Input & Output</summary>

You are given a string s and an integer k. You can choose any character and replace it with any other uppercase English character. Find the length of the longest substring containing the same character after at most k replacements.

Constraints:
- 1 <= s.length <= 10^5
- s consists of uppercase English letters
- 0 <= k <= s.length

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

</details>

<details>
<summary><strong>✅ Q13 : Find All Anagrams in a String</strong></summary>

<details>
<summary>Details</summary>

#438,Med.,Topic4<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+438+Find+All+Anagrams+in+a+String+solution), [LeetCode #438](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

</details>

<details>
<summary>recording</summary>

[#438_Find All Anagrams in a String](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given two strings s and p, return an array of all the starting indices of p's anagrams in s. The output should be in increasing order.

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters

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

</details>

<details>
<summary><strong>✅ Q14 : Decode String</strong></summary>

<details>
<summary>Details</summary>

#394,Med.,Topic6<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+394+Decode+String+solution), [LeetCode #394](https://leetcode.com/problems/decode-string/)

</details>

<details>
<summary>recording</summary>

[#394_Decode String](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given an encoded string s, return its decoded string. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.

Constraints:
- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and brackets
- The input is guaranteed to be valid

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

</details>

<details>
<summary><strong>✅ Q15 : String to Integer (atoi)</strong></summary>

<details>
<summary>Details</summary>

#8,Med.,Topic6<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+8+String+to+Integer+atoi+solution), [LeetCode #8](https://leetcode.com/problems/string-to-integer-atoi/)

</details>

<details>
<summary>recording</summary>

[#8_String to Integer (atoi)](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer according to the following rules: ignore leading whitespace, read an optional sign, read digits until a non-digit appears, and clamp the result to the int32 range.

Constraints:
- 0 <= s.length <= 200
- s consists of English letters, digits, spaces, '+' and '-'

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

</details>

<details>
<summary><strong>✅ Q16 : Encode and Decode Strings</strong></summary>

<details>
<summary>Details</summary>

#271,Med.,Topic6<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+271+Encode+and+Decode+Strings+solution), [LeetCode #271](https://leetcode.com/problems/encode-and-decode-strings/)

</details>

<details>
<summary>recording</summary>

[#271_Encode and Decode Strings](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Design an algorithm to encode a list of strings into a single string and decode it back to the original list.

Constraints:
- 1 <= words.length <= 200
- 0 <= words[i].length <= 20
- words[i] consists of lowercase English letters

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

</details>

<details>
<summary><strong>✅ Q17 : Palindromic Substrings</strong></summary>

<details>
<summary>Details</summary>

#647,Med.,Topic3<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+647+Palindromic+Substrings+solution), [LeetCode #647](https://leetcode.com/problems/palindromic-substrings/)

</details>

<details>
<summary>recording</summary>

[#647_Palindromic Substrings](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given a string s, count how many palindromic substrings are in it.

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters

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
<summary><strong>✅ Q18 : Minimum Window Substring</strong></summary>

<details>
<summary>Details</summary>

#76,Hard,Topic5<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+76+Minimum+Window+Substring+solution), [LeetCode #76](https://leetcode.com/problems/minimum-window-substring/)

</details>

<details>
<summary>recording</summary>

[#76_Minimum Window Substring](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window, return an empty string.

Constraints:
- 1 <= s.length, t.length <= 10^5
- s and t consist of uppercase and lowercase English letters

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

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
<summary><strong>✅ Q19 : Regular Expression Matching</strong></summary>

<details>
<summary>Details</summary>

#10,Hard,Topic8<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+10+Regular+Expression+Matching+solution), [LeetCode #10](https://leetcode.com/problems/regular-expression-matching/)

</details>

<details>
<summary>recording</summary>

[#10_Regular Expression Matching](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'.

Constraints:
- 0 <= s.length <= 20
- 0 <= p.length <= 30
- s and p consist of lowercase English letters

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
<summary><strong>✅ Q20 : Edit Distance</strong></summary>

<details>
<summary>Details</summary>

#72,Hard,Topic8<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+72+Edit+Distance+solution), [LeetCode #72](https://leetcode.com/problems/edit-distance/)

</details>

<details>
<summary>recording</summary>

[#72_Edit Distance](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Given two strings word1 and word2, find the minimum number of operations required to convert word1 into word2. You can perform insert, delete, and replace operations.

Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters

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

</details>
