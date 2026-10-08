# 🧵 String Manipulation --- DSA & LeetCode

A practical guide to the most important String Manipulation concepts,
patterns, and techniques used in DSA and LeetCode.

------------------------------------------------------------------------

## 📚 Table of Contents

1.  Basic String Operations
2.  Character Frequency
3.  HashMap + String
4.  HashSet + String
5.  Two Pointers
6.  Palindromes
7.  Anagrams
8.  Substring vs Subsequence
9.  Sliding Window
10. String → Array
11. String Building
12. Sorting Strings
13. ASCII / Character Conversion
14. String Parsing
15. Stack + String
16. Parentheses
17. String Compression
18. Prefix / Suffix
19. String Search
20. KMP
21. Rabin-Karp
22. Pattern Recognition Cheat Sheet
23. LeetCode Roadmap
24. Top Problems to Master

------------------------------------------------------------------------

# 1. Basic String Operations

## Access Character

``` python
s = "hello"

print(s[0])      # h
print(s[-1])     # o
```

## Length

``` python
len(s)
```

## Slicing

``` python
s = "hello"

s[1:4]     # "ell"
s[:3]      # "hel"
s[2:]      # "llo"
s[::-1]    # "olleh"
```

## Iterate Through String

``` python
for ch in s:
    print(ch)
```

Or using indexes:

``` python
for i in range(len(s)):
    print(s[i])
```

## Reverse

``` python
reversed_s = s[::-1]
```

------------------------------------------------------------------------

# 2. Character Frequency

One of the most common string patterns in LeetCode.

## Using Counter

``` python
from collections import Counter

freq = Counter(s)
```

Example:

``` python
s = "leetcode"

freq = Counter(s)

print(freq)
```

Conceptually:

``` text
l → 1
e → 3
t → 1
c → 1
o → 1
d → 1
```

## Using HashMap

``` python
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
```

## Complexity

``` text
Time:  O(n)
Space: O(k)

k = number of unique characters
```

## Common Problems

-   Valid Anagram
-   Ransom Note
-   First Unique Character
-   Group Anagrams
-   Find All Anagrams

------------------------------------------------------------------------

# 3. HashMap + String

HashMaps are frequently used to store:

-   Character frequency
-   Character positions
-   Previous occurrences
-   Relationships between characters

Example:

``` python
freq = {}

for ch in s:
    if ch not in freq:
        freq[ch] = 0

    freq[ch] += 1
```

## First Unique Character

``` python
from collections import Counter

freq = Counter(s)

for ch in s:
    if freq[ch] == 1:
        return ch
```

------------------------------------------------------------------------

# 4. HashSet + String

Use a Set when you only care about whether something exists.

Example:

``` python
seen = set()

for ch in s:
    if ch in seen:
        return True

    seen.add(ch)

return False
```

Useful for:

-   Detecting duplicates
-   Unique characters
-   Longest substring without repeating characters
-   Tracking visited characters

------------------------------------------------------------------------

# 5. Two Pointers

Two pointers are extremely important for string problems.

Typical structure:

``` text
L → → → → → ← ← ← ← R
```

Example:

``` python
left = 0
right = len(s) - 1

while left < right:

    if s[left] != s[right]:
        return False

    left += 1
    right -= 1

return True
```

## Common Uses

-   Palindrome
-   Reverse String
-   Comparing characters
-   Removing characters
-   Valid Palindrome

## Complexity

``` text
Time:  O(n)
Space: O(1)
```

------------------------------------------------------------------------

# 6. Palindromes

A palindrome reads the same forward and backward.

Examples:

``` text
madam
racecar
level
```

## Simple Approach

``` python
return s == s[::-1]
```

## DSA Approach

``` python
left = 0
right = len(s) - 1

while left < right:

    if s[left] != s[right]:
        return False

    left += 1
    right -= 1

return True
```

## Common Problems

-   Valid Palindrome
-   Longest Palindromic Substring
-   Palindromic Substrings
-   Palindrome Partitioning

------------------------------------------------------------------------

# 7. Anagrams

Two strings are anagrams if they contain the same characters with the
same frequencies.

Example:

``` text
listen
silent
```

## Counter Approach

``` python
from collections import Counter

return Counter(s) == Counter(t)
```

## Sorting Approach

``` python
return sorted(s) == sorted(t)
```

## Complexity

Counter:

``` text
Time:  O(n)
Space: O(k)
```

Sorting:

``` text
Time: O(n log n)
```

## Important LeetCode Problems

-   Valid Anagram
-   Group Anagrams
-   Find All Anagrams in a String
-   Permutation in String

------------------------------------------------------------------------

# 8. Substring vs Subsequence

This distinction is extremely important.

## Substring

Characters must be continuous.

``` text
s = "abcde"

"bcd" → Substring ✅
"ace" → Substring ❌
```

## Subsequence

Characters do NOT need to be continuous.

Order must remain the same.

``` text
s = "abcde"

"ace" → Subsequence ✅
"bd"  → Subsequence ✅
"ec"  → Subsequence ❌
```

## Check Subsequence

``` python
i = 0

for ch in s:

    if i < len(t) and ch == t[i]:
        i += 1

return i == len(t)
```

## Complexity

``` text
Time:  O(n)
Space: O(1)
```

------------------------------------------------------------------------

# 9. Sliding Window

One of the MOST important string patterns.

Sliding Window is used when dealing with:

-   Substrings
-   Consecutive characters
-   Longest/shortest range
-   Character frequency inside a range

## Fixed Window

Example:

``` text
s = "abcdef"
k = 3

Windows:

abc
bcd
cde
def
```

Basic structure:

``` python
left = 0

for right in range(len(s)):

    # Add s[right]

    if right - left + 1 > k:
        # Remove s[left]
        left += 1
```

## Variable Window

Example:

> Longest substring without repeating characters

``` python
left = 0
seen = set()

for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    # window = s[left:right + 1]
```

## Sliding Window Pattern

``` text
Expand → → → →

      [ window ]

      ← ← Shrink when invalid
```

## Common Problems

-   Longest Substring Without Repeating Characters
-   Minimum Window Substring
-   Longest Repeating Character Replacement
-   Find All Anagrams
-   Permutation in String

------------------------------------------------------------------------

# 10. String → Array

Strings are immutable in Python.

Convert to a list when you need to modify characters.

``` python
s = "hello"

chars = list(s)

chars[0] = "H"

s = "".join(chars)
```

Result:

``` text
Hello
```

------------------------------------------------------------------------

# 11. String Building

Avoid repeatedly concatenating strings in large loops.

## Less Efficient

``` python
result = ""

for ch in s:
    result += ch
```

## Better

``` python
result = []

for ch in s:
    result.append(ch)

answer = "".join(result)
```

Useful for:

-   String transformation
-   String compression
-   Removing characters
-   Building answers

------------------------------------------------------------------------

# 12. Sorting Strings

Python:

``` python
sorted(s)
```

Example:

``` python
s = "cab"

print(sorted(s))
```

Output:

``` text
['a', 'b', 'c']
```

Convert back:

``` python
sorted_s = "".join(sorted(s))
```

Useful for:

-   Anagrams
-   Group Anagrams
-   Character ordering
-   Comparing strings

## Complexity

``` text
Time: O(n log n)
Space: O(n)
```

------------------------------------------------------------------------

# 13. ASCII / Character Conversion

Very useful in DSA.

## Character → ASCII

``` python
ord('a')    # 97
ord('z')    # 122
```

## ASCII → Character

``` python
chr(97)     # 'a'
```

## Convert a-z to 0-25

``` python
index = ord(ch) - ord('a')
```

Example:

``` text
a → 0
b → 1
c → 2
...
z → 25
```

## Frequency Array

Instead of a HashMap:

``` python
freq = [0] * 26

for ch in s:
    freq[ord(ch) - ord('a')] += 1
```

This is very common in LeetCode.

------------------------------------------------------------------------

# 14. String Parsing

Useful Python methods:

``` python
ch.isdigit()
ch.isalpha()
ch.isalnum()
ch.isspace()
ch.islower()
ch.isupper()
```

Example:

``` python
for ch in s:

    if ch.isdigit():
        print("Number")

    elif ch.isalpha():
        print("Letter")
```

Useful for:

-   String to Integer
-   Valid Number
-   Basic Calculator
-   Decode String
-   Parsing expressions

------------------------------------------------------------------------

# 15. Stack + String

Strings often use a Stack.

Example:

``` text
s = "ab#c#"
```

Suppose `#` means delete previous character.

``` python
stack = []

for ch in s:

    if ch == '#':

        if stack:
            stack.pop()

    else:
        stack.append(ch)

return "".join(stack)
```

## Common Problems

-   Backspace String Compare
-   Remove Adjacent Duplicates
-   Decode String
-   Parentheses Problems

------------------------------------------------------------------------

# 16. Parentheses

Classic Stack problem.

Example:

``` text
"({[]})"
```

Use:

``` python
stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for ch in s:

    if ch in "([{":
        stack.append(ch)

    else:

        if not stack:
            return False

        if stack.pop() != pairs[ch]:
            return False

return not stack
```

## Complexity

``` text
Time:  O(n)
Space: O(n)
```

------------------------------------------------------------------------

# 17. String Compression

Example:

``` text
Input:
aaabbcccc

Output:
a3b2c4
```

Basic pattern:

``` python
count = 1

for i in range(1, len(s)):

    if s[i] == s[i - 1]:
        count += 1

    else:
        # Process previous character
        count = 1
```

## Important Concept

You are detecting groups of consecutive characters:

``` text
AAAA BBB CC
│    │   │
4    3   2
```

Used in:

-   String Compression
-   Count and Say
-   Consecutive Characters

------------------------------------------------------------------------

# 18. Prefix / Suffix

## Prefix

Characters from the beginning.

``` text
flower

""
"f"
"fl"
"flo"
"flow"
"flowe"
"flower"
```

## Suffix

Characters from the end.

``` text
flower

"r"
"er"
"wer"
"ower"
"lower"
"flower"
```

## Longest Common Prefix

Example:

``` text
flower
flow
flight
```

Answer:

``` text
fl
```

Simple approach:

``` python
prefix = strs[0]

for s in strs[1:]:

    while not s.startswith(prefix):
        prefix = prefix[:-1]

return prefix
```

------------------------------------------------------------------------

# 19. String Search

Basic string search:

``` python
s.find("abc")
```

Or:

``` python
"abc" in s
```

For DSA, understand the algorithms behind string matching:

``` text
Naive Search
      ↓
KMP
      ↓
Rabin-Karp
      ↓
Z Algorithm
```

------------------------------------------------------------------------

# 20. KMP

KMP = Knuth-Morris-Pratt.

Used for efficient pattern matching.

Example:

``` text
Text:
ABABDABACDABABCABAB

Pattern:
ABABCABAB
```

Instead of restarting from the beginning after every mismatch, KMP uses
previously matched information.

## Core Concept

Build:

``` text
LPS Array
```

LPS means:

``` text
Longest Proper Prefix
which is also
Suffix
```

Example:

``` text
Pattern:
AAACAAAA

LPS:
0 1 2 0 1 2 3 1
```

## Complexity

``` text
Time:  O(n + m)
Space: O(m)
```

Where:

``` text
n = text length
m = pattern length
```

------------------------------------------------------------------------

# 21. Rabin-Karp

Rabin-Karp uses hashing for pattern matching.

Basic idea:

``` text
String
  ↓
Hash
  ↓
Compare hash
  ↓
Verify characters
```

Useful for:

-   Pattern matching
-   Multiple pattern searches
-   Rolling hash problems

## Rolling Hash

Instead of recalculating the entire hash for every window:

``` text
Window 1 → Hash
Window 2 → Update Hash
Window 3 → Update Hash
```

This allows efficient substring comparison.

------------------------------------------------------------------------

# 22. Pattern Recognition Cheat Sheet

  Problem Clue                           Likely Pattern
  -------------------------------------- ---------------------------------
  Are these two strings anagrams?        HashMap / Counter
  Find duplicate characters              HashSet / HashMap
  Is this a palindrome?                  Two Pointers
  Longest substring...                   Sliding Window
  Minimum substring containing...        Sliding Window + HashMap
  Characters must remain in order        Two Pointers / Subsequence
  Remove previous character              Stack
  Valid parentheses                      Stack
  Count consecutive characters           Run Length / Compression
  Common beginning of strings            Prefix
  Find pattern inside text efficiently   KMP / Rabin-Karp
  Fixed-size substring                   Fixed Sliding Window
  Variable-size substring                Variable Sliding Window
  Character a-z                          ord(ch) - ord('a')
  Modify string                          Convert to list → modify → join
  Build large string                     List + "".join()

------------------------------------------------------------------------

# 23. LeetCode Roadmap

## 🟢 Beginner

Learn these first:

1.  Basic String Operations
2.  Character Frequency
3.  HashMap
4.  HashSet
5.  Reverse String
6.  Palindrome
7.  Anagram
8.  Sorting
9.  ASCII / ord / chr

Recommended problems:

-   Valid Anagram
-   Valid Palindrome
-   Ransom Note
-   First Unique Character in a String
-   Reverse String
-   Longest Common Prefix
-   Is Subsequence

------------------------------------------------------------------------

## 🟡 Intermediate

Then learn:

1.  Two Pointers
2.  Sliding Window
3.  String Parsing
4.  Stack + String
5.  Prefix / Suffix
6.  String Compression

Recommended problems:

-   Longest Substring Without Repeating Characters
-   Permutation in String
-   Find All Anagrams in a String
-   Longest Repeating Character Replacement
-   String Compression
-   Backspace String Compare
-   Remove All Adjacent Duplicates
-   Decode String

------------------------------------------------------------------------

## 🔴 Advanced

Finally:

1.  KMP
2.  Rabin-Karp
3.  Rolling Hash
4.  Z Algorithm
5.  Palindrome Algorithms
6.  Advanced String DP

Recommended problems:

-   Minimum Window Substring
-   Longest Palindromic Substring
-   Palindromic Substrings
-   Implement strStr()
-   Repeated Substring Pattern
-   Word Break
-   Word Search

------------------------------------------------------------------------

# 24. Most Important String Patterns

  Priority     Pattern               Importance
  ------------ --------------------- ------------
  ⭐⭐⭐⭐⭐   HashMap + Frequency   Very High
  ⭐⭐⭐⭐⭐   Sliding Window        Very High
  ⭐⭐⭐⭐⭐   Two Pointers          Very High
  ⭐⭐⭐⭐⭐   HashSet               Very High
  ⭐⭐⭐⭐     Palindrome            High
  ⭐⭐⭐⭐     Anagrams              High
  ⭐⭐⭐⭐     Subsequence           High
  ⭐⭐⭐⭐     Stack + String        High
  ⭐⭐⭐       String Parsing        Medium
  ⭐⭐⭐       Prefix / Suffix       Medium
  ⭐⭐         KMP                   Advanced
  ⭐⭐         Rabin-Karp            Advanced
  ⭐⭐         Z Algorithm           Advanced

------------------------------------------------------------------------

# 🎯 Recommended Learning Order

``` text
                    STRINGS
                       │
                       ▼
             Basic String Operations
                       │
                       ▼
              HashMap + Frequency
                       │
                       ▼
                  HashSet
                       │
                       ▼
                Two Pointers
                       │
                       ▼
                 Palindromes
                       │
                       ▼
                  Anagrams
                       │
                       ▼
              Substring / Subsequence
                       │
                       ▼
               Sliding Window ⭐
                       │
                       ▼
               Stack + Strings
                       │
                       ▼
                String Parsing
                       │
                       ▼
                 Prefix/Suffix
                       │
                       ▼
                String Search
                       │
                       ▼
              KMP / Rabin-Karp
```

------------------------------------------------------------------------

# 🏆 Top 10 String Problems to Master

1.  Valid Anagram
2.  Valid Palindrome
3.  First Unique Character in a String
4.  Longest Common Prefix
5.  Is Subsequence
6.  Longest Substring Without Repeating Characters
7.  Permutation in String
8.  Find All Anagrams in a String
9.  Longest Repeating Character Replacement
10. Minimum Window Substring

------------------------------------------------------------------------

# 🧠 Final Interview Cheat Sheet

``` text
FREQUENCY
    ↓
HashMap / Counter

DUPLICATES
    ↓
HashSet

PALINDROME
    ↓
Two Pointers

ANAGRAM
    ↓
Counter / Frequency Array / Sorting

SUBSEQUENCE
    ↓
Two Pointers

SUBSTRING
    ↓
Sliding Window

LONGEST SUBSTRING
    ↓
Sliding Window + HashMap/Set

MINIMUM WINDOW
    ↓
Sliding Window + Frequency Map

PARENTHESES
    ↓
Stack

REMOVE PREVIOUS CHARACTER
    ↓
Stack

CONSECUTIVE CHARACTERS
    ↓
Run Length Encoding

COMMON START
    ↓
Prefix

PATTERN MATCHING
    ↓
KMP / Rabin-Karp

FIXED SIZE SUBSTRING
    ↓
Fixed Sliding Window

VARIABLE SIZE SUBSTRING
    ↓
Variable Sliding Window

CHARACTER a-z
    ↓
ord(ch) - ord('a')

MODIFY STRING
    ↓
Convert to list → modify → join

BUILD LARGE STRING
    ↓
List + "".join()
```

------------------------------------------------------------------------

# 🚀 Goal

Before moving to advanced DSA topics, be comfortable solving string
problems using:

-   HashMap
-   HashSet
-   Counter
-   Two Pointers
-   Sliding Window
-   Stack
-   Sorting
-   Prefix/Suffix
-   ASCII / Frequency Array
-   Basic String Parsing

These patterns cover a large portion of the string-manipulation problems
encountered in LeetCode interviews.
