# Recordings

[14. Longest Common Substring](https://raw.githubusercontent.com/MeghaPrabhakar/Leetcode/main/2_Strings/Recordings/14.%20Longest%20Common%20Substring.mp3)<br/>
Sample <br/>
Example 1:<br/>

Input: strs = ["flower","flow","flight"]<br/>
Output: "fl"<br/>
Example 2:<br/>

Input: strs = ["dog","racecar","car"]<br/>
Output: ""<br/>
Explanation: There is no common prefix among the input strings.<br/>

code<br/>
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

        
