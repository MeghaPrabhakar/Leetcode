# Recordings

[14. Longest Common Substring](https://raw.githubusercontent.com/MeghaPrabhakar/Leetcode/main/2_Strings/Recordings/14.%20Longest%20Common%20Substring.mp3)

Sample:

<details>
<summary>Python</summary>

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
```

```python
strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
# Output: "fl"
```

```python
strs = ["dog", "racecar", "car"]
print(Solution().longestCommonPrefix(strs))
# Output: ""
```

</details>

Explanation: There is no common prefix among the input strings.
