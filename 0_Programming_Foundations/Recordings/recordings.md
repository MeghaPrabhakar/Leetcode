# Recordings

<details>
<summary><strong>✅ Topic 1 : Python Basics</strong></summary>

<details>
<summary>Details</summary>

Python Basics<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=Python+basics+tutorial+for+beginners)

</details>

<details>
<summary>Key Points</summary>

- Variables and assignment
- Input and output
- Comments and indentation
- Basic operators
- Data flow in a Python script

</details>

<details>
<summary>Examples</summary>

```python
name = "Alice"
print(f"Hello, {name}!")
```

</details>

</details>


<details>
<summary><strong>✅ Topic 2 : Data Types & Loops</strong></summary>

<details>
<summary>Details</summary>

Data Types & Loops<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=Python+data+types+and+loops+tutorial)

</details>

<details>
<summary>Key Points</summary>

- int, float, str, bool, list, tuple, dict, set
- for loops and while loops
- break, continue, pass
- iteration over collections

</details>

<details>
<summary>Examples</summary>

```python
nums = [1, 2, 3]
for n in nums:
    print(n * 2)
```

</details>

</details>


<details>
<summary><strong>✅ Topic 3 : Functions & OOP Basics</strong></summary>

<details>
<summary>Details</summary>

Functions & OOP Basics<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=Python+functions+and+OOP+for+beginners)

</details>

<details>
<summary>Key Points</summary>

- Function definition and parameters
- Return values
- Scope and global variables
- Classes, objects, methods
- __init__ and object state

</details>

<details>
<summary>Examples</summary>

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} barks!"
```

</details>

</details>


<details>
<summary><strong>✅ Topic 4 : Recursion Basics</strong></summary>

<details>
<summary>Details</summary>

Recursion Basics<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=Python+recursion+tutorial+for+beginners)

</details>

<details>
<summary>Key Points</summary>

- Base case and recursive case
- Call stack behavior
- Factorial and Fibonacci examples
- When to avoid recursion

</details>

<details>
<summary>Examples</summary>

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

</details>

</details>


<details>
<summary><strong>✅ Topic 5 : Time & Space Complexity</strong></summary>

<details>
<summary>Details</summary>

Time & Space Complexity<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=Python+time+and+space+complexity+tutorial)

</details>

<details>
<summary>Key Points</summary>

- O(1), O(log n), O(n), O(n log n), O(n^2)
- Counting operations
- Best, average, worst case
- Memory usage analysis

</details>

<details>
<summary>Examples</summary>

```python
# O(n)
for x in range(10):
    print(x)
```

</details>

</details>


<details>
<summary><strong>✅ Topic 6 : Big-O Analysis</strong></summary>

<details>
<summary>Details</summary>

Big-O Analysis<br/>Useful links: [YouTube](https://www.youtube.com/results?search_query=Big+O+notation+tutorial+Python)

</details>

<details>
<summary>Key Points</summary>

- Compare algorithm growth rates
- Ignore constants and lower-order terms
- Use Big-O to reason about scalability
- Pair with practical testing

</details>

<details>
<summary>Examples</summary>

```python
# O(n)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

</details>

</details>
