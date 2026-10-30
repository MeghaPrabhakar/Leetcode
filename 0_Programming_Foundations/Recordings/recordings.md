# Recordings

<details>
<summary><strong>✅ Q1 : Fizz Buzz</strong></summary>

<details>
<summary>Details</summary>

#412,Topic1<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+412+Fizz+Buzz+solution)

</details>

<details>
<summary>recording</summary>

[#412_Fizz Buzz](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def fizzBuzz(self, n: int):
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1) extra space

</details>

</details>

<details>
<summary><strong>✅ Q2 : Running Sum of 1d Array</strong></summary>

<details>
<summary>Details</summary>

#1480,Topic2<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+1480+Running+Sum+of+1D+Array+solution)

</details>

<details>
<summary>recording</summary>

[#1480_Running Sum of 1d Array](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Example 2:
Input: nums = [1,1,1]
Output: [1,2,3]

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def runningSum(self, nums):
        running = 0
        result = []
        for num in nums:
            running += num
            result.append(running)
        return result
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(n)

</details>

</details>

<details>
<summary><strong>✅ Q3 : Richest Customer Wealth</strong></summary>

<details>
<summary>Details</summary>

#1672,Topic2<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+1672+Richest+Customer+Wealth+solution)

</details>

<details>
<summary>recording</summary>

[#1672_Richest Customer Wealth](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

Example 2:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        for customer in accounts:
            max_wealth = max(max_wealth, sum(customer))
        return max_wealth
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(m * n)
Space Complexity: O(1)

</details>

</details>

<details>
<summary><strong>✅ Q4 : Find Numbers with Even Number of Digits</strong></summary>

<details>
<summary>Details</summary>

#1295,Topic2<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+1295+Find+Numbers+with+Even+Number+of+Digits+solution)

</details>

<details>
<summary>recording</summary>

[#1295_Find Numbers with Even Number of Digits](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2

Example 2:
Input: nums = [555,901,482,1771]
Output: 1

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            digits = len(str(abs(num)))
            if digits % 2 == 0:
                count += 1
        return count
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

</details>

<details>
<summary><strong>✅ Q5 : Find Pivot Index</strong></summary>

<details>
<summary>Details</summary>

#724,Topic3<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+724+Find+Pivot+Index+solution)

</details>

<details>
<summary>recording</summary>

[#724_Find Pivot Index](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3

Example 2:
Input: nums = [1,2,3]
Output: -1

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            left += num
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
<summary><strong>✅ Q6 : Binary Search</strong></summary>

<details>
<summary>Details</summary>

#704,Topic3<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+704+Binary+Search+solution)

</details>

<details>
<summary>recording</summary>

[#704_Binary Search](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(log n)
Space Complexity: O(1)

</details>

</details>

<details>
<summary><strong>✅ Q7 : Fibonacci Number</strong></summary>

<details>
<summary>Details</summary>

#509,Topic4<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+509+Fibonacci+Number+solution)

</details>

<details>
<summary>recording</summary>

[#509_Fibonacci Number](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: n = 2
Output: 1

Example 2:
Input: n = 3
Output: 2

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

</details>

<details>
<summary><strong>✅ Q8 : Climbing Stairs</strong></summary>

<details>
<summary>Details</summary>

#70,Topic4<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=LeetCode+70+Climbing+Stairs+solution)

</details>

<details>
<summary>recording</summary>

[#70_Climbing Stairs](#)

</details>

<details>
<summary>Sample Input & Output</summary>

Example 1:
Input: n = 2
Output: 2

Example 2:
Input: n = 3
Output: 3

</details>

<details>
<summary>Code</summary>

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
```

</details>

<details>
<summary>Space & Time Complexity</summary>

Time Complexity: O(n)
Space Complexity: O(1)

</details>

</details>
