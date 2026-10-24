# 🐍 LeetCode Python Practice (121–125)

## 📌 About This Repository

This repository contains five beginner-friendly Python programming exercises designed to improve logical thinking, problem-solving skills, and understanding of core Python concepts.

Each program focuses on a different programming problem, including finding the longest word, checking prime numbers, counting words, calculating powers, and finding common elements between lists.

## 🎯 Objectives

* Practice Python programming fundamentals.
* Improve logical thinking and problem-solving.
* Understand strings, lists, loops, and built-in functions.
* Learn to handle user input and display results.
* Build consistent coding practice for technical interviews.

## 📚 Problems Included

| No. | Problem Name                        | Concepts Used                    |
| --- | ----------------------------------- | -------------------------------- |
| 121 | Find the Longest Word in a Sentence | Strings, Lists, `max()`          |
| 122 | Prime Number Checker                | Loops, Conditions, Mathematics   |
| 123 | Count Words in a Sentence           | Strings, `split()`               |
| 124 | Calculate Power of a Number         | Arithmetic Operators, User Input |
| 125 | Find Common Elements in Two Lists   | Lists, Sets, Sorting             |

---

## 1️⃣ Problem 121 – Find the Longest Word

### Description

Write a Python program to find the longest word in a sentence.

### Code

```python
sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
else:
    print("Please enter a sentence.")
```

### Example

**Input:**

```text
Python programming is interesting
```

**Output:**

```text
Longest word: programming
```

### Concepts Learned

* String manipulation
* Lists
* The `split()` method
* The `max()` function
* The `len()` function

---

## 2️⃣ Problem 122 – Prime Number Checker

### Description

Write a Python program to check whether a number is prime.

A prime number is a number greater than 1 that has exactly two positive factors: 1 and itself.

### Code

```python
import math

number = int(input("Enter a number: "))

if number < 2:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
```

### Example

**Input:**

```text
Enter a number: 17
```

**Output:**

```text
Prime number
```

### Concepts Learned

* Conditional statements
* `for` loops
* The modulo operator `%`
* The `math.isqrt()` function
* Prime number logic

---

## 3️⃣ Problem 123 – Count Words in a Sentence

### Description

Write a Python program to count the number of words in a sentence.

### Code

```python
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))
```

### Example

**Input:**

```text
Python is easy to learn
```

**Output:**

```text
Number of words: 5
```

### Concepts Learned

* String handling
* The `split()` method
* The `len()` function
* User input

---

## 4️⃣ Problem 124 – Calculate Power of a Number

### Description

Write a Python program to calculate a number raised to a given exponent.

### Code

```python
try:
    base = float(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))

    if base == 0 and exponent < 0:
        print("Zero cannot have a negative exponent.")
    else:
        result = base ** exponent
        print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers only.")
```

### Example

**Input:**

```text
Enter the base: 2
Enter the exponent: 5
```

**Output:**

```text
Result: 32.0
```

### Concepts Learned

* Arithmetic operators
* The exponentiation operator `**`
* User input
* Type conversion
* Exception handling with `try` and `except`

---

## 5️⃣ Problem 125 – Find Common Elements in Two Lists

### Description

Write a Python program to find the elements that appear in both lists.

### Code

```python
list1 = list(map(int, input("Enter the first list numbers: ").split()))
list2 = list(map(int, input("Enter the second list numbers: ").split()))

common = sorted(set(list1) & set(list2))

print("Common elements:", common)
```

### Example

**Input:**

```text
Enter the first list numbers: 1 2 3 4 5
Enter the second list numbers: 3 4 5 6 7
```

**Output:**

```text
Common elements: [3, 4, 5]
```

### Concepts Learned

* Lists
* Sets
* Set intersection using `&`
* Sorting
* Type conversion with `map()`

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Code Editor:** Visual Studio Code
* **Version Control:** Git
* **Code Hosting:** GitHub

## ▶️ How to Run the Programs

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Open the Terminal

Select **Terminal → New Terminal**.

### Step 4: Run a Program

If the files are stored inside a folder named `python`, use the corresponding command:

```bash
python python/121.py
```

For the other programs, replace `121.py` with `122.py`, `123.py`, `124.py`, or `125.py`.

Make sure the file paths match your actual project structure.

## 📈 Learning Outcomes

After completing these five exercises, you will have practiced:

* Working with strings and lists.
* Using loops and conditional statements.
* Solving mathematical problems.
* Using Python built-in functions.
* Finding common elements with sets.
* Handling invalid input.
* Running Python programs in Visual Studio Code.

## 👩‍💻 Author

**Aishwarya**

## 🔗 GitHub Repositories

* [LeetCode Python 121](https://github.com/aishuaishu45793-gif/leetcode-python-121.py)
* [LeetCode Python 122](https://github.com/aishuaishu45793-gif/leetcode-python-122.py)
* [LeetCode Python 123](https://github.com/aishuaishu45793-gif/leetcode-python-123.py)
* [LeetCode Python 124](https://github.com/aishuaishu45793-gif/leetcode-python-124.py)
* [LeetCode Python 125](https://github.com/aishuaishu45793-gif/leetcode-python-125.py)

---

⭐ **Thank you for visiting my Python practice repository!**

This project is part of my ongoing journey to improve my Python programming and problem-solving skills through regular coding practice.
