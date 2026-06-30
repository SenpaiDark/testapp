"""
Management command to seed all 12 Python lessons, their quizzes, and questions.

Usage:
    python manage.py seed_lessons
    python manage.py seed_lessons --clear   # delete existing data first
"""
from django.core.management.base import BaseCommand
from courses.models import Lesson
from quizzes.models import Quiz, Question


LESSONS = [
    # ─────────────────────────────────────────────────────────────────
    # Lesson 1
    # ─────────────────────────────────────────────────────────────────
    {
        "order": 1,
        "title": "Introduction to Python",
        "summary": "What Python is, why it matters, and your first lines of code.",
        "content": """
<p>Python is a high-level, interpreted programming language created by <strong>Guido van Rossum</strong> and first released in 1991. It is known for its clean, readable syntax that resembles plain English — making it one of the best first languages for beginners.</p>

<h3>Why Learn Python?</h3>
<ul>
  <li>Easy to read and write — looks almost like English</li>
  <li>Used in web development, data science, AI, automation, and more</li>
  <li>Massive community with tons of free resources</li>
  <li>Runs on Windows, macOS, and Linux</li>
</ul>

<h3>Your First Python Program</h3>
<p>The simplest thing you can do in Python is print a message to the screen. We use the built-in <code>print()</code> function for this:</p>
<pre><code>print("Hello, World!")</code></pre>
<p>Running the code above will display:</p>
<pre><code>Hello, World!</code></pre>

<h3>Comments</h3>
<p>A <strong>comment</strong> is a note in your code that Python completely ignores. Use the <code>#</code> symbol to start one. Comments help you and other programmers understand what the code does.</p>
<pre><code># This is a comment — Python ignores this line
print("Comments make code easier to understand")  # inline comment</code></pre>

<h3>Python as a Calculator</h3>
<p>Python can perform arithmetic operations directly:</p>
<pre><code>print(5 + 3)    # 8  — addition
print(10 - 4)   # 6  — subtraction
print(3 * 4)    # 12 — multiplication
print(15 / 3)   # 5.0 — division (always returns a float)
print(17 // 3)  # 5  — floor division (drops the decimal)
print(17 % 3)   # 2  — modulo (remainder)
print(2 ** 8)   # 256 — exponentiation</code></pre>

<h3>Summary</h3>
<ul>
  <li>Use <code>print()</code> to display output</li>
  <li>Use <code>#</code> to write comments</li>
  <li>Python supports all basic arithmetic operators</li>
</ul>
""".strip(),
        "quiz_title": "Introduction to Python Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "Which function is used to display output in Python?", "option_a": "show()", "option_b": "print()", "option_c": "display()", "option_d": "output()", "correct_option": "B"},
            {"text": "Which symbol is used to write a comment in Python?", "option_a": "//", "option_b": "/* */", "option_c": "--", "option_d": "#", "correct_option": "D"},
            {"text": "Python is best described as a _____ programming language.", "option_a": "Machine-level", "option_b": "Assembly", "option_c": "High-level", "option_d": "Binary", "correct_option": "C"},
            {"text": "What is the correct file extension for a Python source file?", "option_a": ".pt", "option_b": ".pyt", "option_c": ".py", "option_d": ".python", "correct_option": "C"},
            {"text": "What is the result of print(2 ** 3) in Python?", "option_a": "6", "option_b": "5", "option_c": "9", "option_d": "8", "correct_option": "D"},
        ],
    },

    # ── Lesson 2 ──────────────────────────────────────────────────────────────
    {
        "order": 2,
        "title": "Variables and Data Types",
        "summary": "Store and work with numbers, text, and booleans using variables.",
        "content": """
<p>A <strong>variable</strong> is a named container that stores a value. In Python, you create a variable simply by assigning a value to a name — no need to declare a type first.</p>

<h3>Creating Variables</h3>
<pre><code>name = "Alice"        # a string (text)
age = 20              # an integer (whole number)
gpa = 3.75            # a float (decimal number)
is_student = True     # a boolean (True or False)</code></pre>

<h3>Python's Core Data Types</h3>
<ul>
  <li><code>int</code> — whole numbers, e.g. <code>42</code>, <code>-7</code></li>
  <li><code>float</code> — decimal numbers, e.g. <code>3.14</code>, <code>-0.5</code></li>
  <li><code>str</code> — text enclosed in quotes, e.g. <code>"hello"</code></li>
  <li><code>bool</code> — either <code>True</code> or <code>False</code></li>
</ul>

<h3>Checking a Variable's Type</h3>
<p>Use the built-in <code>type()</code> function to find out what type a value is:</p>
<pre><code>print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'></code></pre>

<h3>Naming Rules for Variables</h3>
<ul>
  <li>Can contain letters, digits, and underscores (<code>_</code>)</li>
  <li>Must start with a letter or underscore — <strong>not</strong> a digit</li>
  <li>Case-sensitive: <code>name</code> and <code>Name</code> are different variables</li>
  <li>Cannot be a Python keyword (like <code>if</code>, <code>for</code>, <code>True</code>)</li>
</ul>
<pre><code>my_name = "Bob"    # valid
_count = 0         # valid
2fast = "no"       # INVALID — starts with a digit</code></pre>

<h3>Type Conversion</h3>
<p>You can convert between types using built-in functions:</p>
<pre><code>x = int("42")      # string -> integer: 42
y = float(7)       # integer -> float: 7.0
z = str(100)       # integer -> string: "100"
b = bool(0)        # integer -> bool: False
</code></pre>

<h3>String Concatenation</h3>
<p>Join strings together with the <code>+</code> operator, or use an f-string for easy formatting:</p>
<pre><code>first = "Python"
second = "Rocks"
print(first + " " + second)   # Python Rocks

# f-string (modern and recommended)
language = "Python"
print(f"I am learning {language}!")  # I am learning Python!</code></pre>
""".strip(),
        "quiz_title": "Variables and Data Types Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "What data type is the value 3.14 in Python?", "option_a": "int", "option_b": "str", "option_c": "bool", "option_d": "float", "correct_option": "D"},
            {"text": "What does the type() function do?", "option_a": "Converts a value to a different type", "option_b": "Returns the data type of a value", "option_c": "Prints the value to the screen", "option_d": "Deletes the variable", "correct_option": "B"},
            {"text": "Which of the following is a valid Python variable name?", "option_a": "2fast", "option_b": "my-name", "option_c": "my name", "option_d": "my_name", "correct_option": "D"},
            {"text": "What is the value of bool(0) in Python?", "option_a": "True", "option_b": "1", "option_c": "False", "option_d": "None", "correct_option": "C"},
            {"text": 'What function converts the string "42" into an integer?', "option_a": 'str("42")', "option_b": 'float("42")', "option_c": 'int("42")', "option_d": 'convert("42")', "correct_option": "C"},
        ],
    },

    # ── Lesson 3 ──────────────────────────────────────────────────────────────
    {
        "order": 3,
        "title": "Conditional Statements",
        "summary": "Make decisions in your code using if, elif, and else.",
        "content": """
<p>Programs often need to make decisions. <strong>Conditional statements</strong> let your code do different things depending on whether a condition is <code>True</code> or <code>False</code>.</p>

<h3>The if Statement</h3>
<pre><code>age = 18

if age >= 18:
    print("You are an adult.")</code></pre>
<p>Notice the <strong>colon</strong> (<code>:</code>) after the condition and the <strong>indentation</strong> (4 spaces or a tab) before the code inside the block.</p>

<h3>if / else</h3>
<pre><code>score = 45

if score >= 50:
    print("You passed!")
else:
    print("You need to try again.")</code></pre>

<h3>if / elif / else</h3>
<pre><code>score = 72

if score >= 70:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")</code></pre>

<h3>Comparison Operators</h3>
<ul>
  <li><code>==</code> equal to</li>
  <li><code>!=</code> not equal to</li>
  <li><code>></code> greater than</li>
  <li><code><</code> less than</li>
  <li><code>>=</code> greater than or equal to</li>
  <li><code><=</code> less than or equal to</li>
</ul>

<h3>Logical Operators</h3>
<pre><code>age = 20; has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
x = 5
if x < 0 or x > 100:
    print("Out of range")
if not has_id:
    print("No ID provided")</code></pre>
""".strip(),
        "quiz_title": "Conditional Statements Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "What keyword starts a conditional block in Python?", "option_a": "when", "option_b": "case", "option_c": "if", "option_d": "check", "correct_option": "C"},
            {"text": "What is the output of: x = 10\\nif x > 5: print('big')\\nelse: print('small')", "option_a": "small", "option_b": "big", "option_c": "10", "option_d": "Error", "correct_option": "B"},
            {"text": "Which keyword handles additional conditions after an initial if?", "option_a": "else if", "option_b": "elseif", "option_c": "elif", "option_d": "otherwise", "correct_option": "C"},
            {"text": "What is the result of the expression: 5 != 5", "option_a": "True", "option_b": "None", "option_c": "Error", "option_d": "False", "correct_option": "D"},
            {"text": "Which logical operator returns True only when BOTH conditions are True?", "option_a": "or", "option_b": "not", "option_c": "and", "option_d": "xor", "correct_option": "C"},
        ],
    },

    # ── Lesson 4 ──────────────────────────────────────────────────────────────
    {
        "order": 4,
        "title": "Loops",
        "summary": "Repeat actions efficiently using for loops and while loops.",
        "content": """
<p>A <strong>loop</strong> lets you run the same block of code multiple times. Python has two main types: <code>for</code> loops and <code>while</code> loops.</p>

<h3>The for Loop</h3>
<pre><code>for i in range(5):
    print(i)
# Output: 0 1 2 3 4</code></pre>

<h3>The range() Function</h3>
<pre><code>range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8  (step = 2)</code></pre>

<h3>Looping Over a List</h3>
<pre><code>fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple  banana  cherry</code></pre>

<h3>The while Loop</h3>
<pre><code>count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4</code></pre>
<p><strong>Warning:</strong> always make sure the condition eventually becomes <code>False</code>, or the loop will run forever.</p>

<h3>break and continue</h3>
<pre><code>for i in range(10):
    if i == 5: break
    print(i)
# Output: 0 1 2 3 4

for i in range(6):
    if i == 3: continue
    print(i)
# Output: 0 1 2 4 5</code></pre>
""".strip(),
        "quiz_title": "Loops Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "What numbers does range(5) produce?", "option_a": "1, 2, 3, 4, 5", "option_b": "0, 1, 2, 3, 4", "option_c": "0, 1, 2, 3, 4, 5", "option_d": "1, 2, 3, 4", "correct_option": "B"},
            {"text": "Which keyword immediately exits a loop?", "option_a": "exit", "option_b": "stop", "option_c": "continue", "option_d": "break", "correct_option": "D"},
            {"text": "What does the continue keyword do inside a loop?", "option_a": "Exits the loop entirely", "option_b": "Restarts the program", "option_c": "Skips the rest of the current iteration", "option_d": "Pauses the loop", "correct_option": "C"},
            {"text": "A while loop keeps running as long as its condition is ___.", "option_a": "False", "option_b": "Zero", "option_c": "None", "option_d": "True", "correct_option": "D"},
            {"text": "What is the output of: for i in range(3): print(i)", "option_a": "1 2 3", "option_b": "0 1 2 3", "option_c": "0 1 2", "option_d": "1 2", "correct_option": "C"},
        ],
    },

    # ── Lesson 5 ──────────────────────────────────────────────────────────────
    {
        "order": 5,
        "title": "Functions",
        "summary": "Write reusable blocks of code with parameters, return values, and defaults.",
        "content": """
<p>A <strong>function</strong> is a reusable block of code that performs a specific task. Instead of writing the same logic over and over, you define it once and call it whenever you need it.</p>

<h3>Defining a Function</h3>
<pre><code>def greet():
    print("Hello from the function!")
greet()   # Output: Hello from the function!</code></pre>

<h3>Parameters and Arguments</h3>
<pre><code>def greet(name):
    print(f"Hello, {name}!")
greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!</code></pre>

<h3>The return Statement</h3>
<pre><code>def add(a, b):
    return a + b
result = add(3, 5)
print(result)   # 8</code></pre>

<h3>Default Parameters</h3>
<pre><code>def power(base, exponent=2):
    return base ** exponent
print(power(4))      # 16
print(power(2, 10))  # 1024</code></pre>

<h3>Why Use Functions?</h3>
<ul>
  <li><strong>Reusability</strong> — write once, use anywhere</li>
  <li><strong>Readability</strong> — give meaningful names to blocks of logic</li>
  <li><strong>Maintainability</strong> — fix a bug in one place instead of many</li>
</ul>
<p>A complete example:</p>
<pre><code>def calculate_grade(score):
    if score >= 70: return "A"
    elif score >= 60: return "B"
    elif score >= 50: return "C"
    else: return "F"
print(calculate_grade(85))  # A
print(calculate_grade(55))  # C
print(calculate_grade(40))  # F</code></pre>
""".strip(),
        "quiz_title": "Functions Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "What keyword is used to define a function in Python?", "option_a": "function", "option_b": "func", "option_c": "define", "option_d": "def", "correct_option": "D"},
            {"text": "What keyword sends a value back from a function?", "option_a": "send", "option_b": "output", "option_c": "return", "option_d": "give", "correct_option": "C"},
            {"text": 'What is the output of: def greet(): return "Hi" print(greet())', "option_a": "greet", "option_b": "None", "option_c": "Error", "option_d": "Hi", "correct_option": "D"},
            {"text": "In def power(base, exponent=2): what is exponent=2 called?", "option_a": "Required parameter", "option_b": "Global variable", "option_c": "Default parameter", "option_d": "Return value", "correct_option": "C"},
            {"text": "How do you correctly call a function named calculate?", "option_a": "run calculate()", "option_b": "call calculate()", "option_c": "calculate()", "option_d": "execute calculate()", "correct_option": "C"},
        ],
    },

    # ── Lesson 6: Lists ───────────────────────────────────────────────────────
    {
        "order": 6,
        "title": "Lists",
        "summary": "Store and manipulate ordered collections of items using lists.",
        "content": """
<p>A <strong>list</strong> is an ordered, mutable collection of items. You can store any data type in a list — strings, numbers, booleans, even other lists.</p>

<h3>Creating a List</h3>
<pre><code>fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]
empty = []</code></pre>

<h3>Accessing Items by Index</h3>
<pre><code>fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (negative index = from end)</code></pre>

<h3>Slicing</h3>
<pre><code>nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])   # [1, 2, 3]
print(nums[:3])    # [0, 1, 2]
print(nums[3:])    # [3, 4, 5]
print(nums[::2])   # [0, 2, 4]  (step = 2)</code></pre>

<h3>Modifying Lists</h3>
<pre><code>fruits = ["apple", "banana"]
fruits.append("cherry")       # add to the end
fruits.insert(1, "blueberry") # insert at position 1
fruits[0] = "avocado"         # replace an item
fruits.remove("banana")       # remove by value
last = fruits.pop()           # remove and return the last item
print(fruits)                 # ['avocado', 'blueberry']</code></pre>

<h3>Useful List Methods</h3>
<pre><code>nums = [3, 1, 4, 1, 5]
nums.sort()                   # sort in place -> [1, 1, 3, 4, 5]
nums.reverse()                # reverse -> [5, 4, 3, 1, 1]
print(len(nums))              # 5 — number of items
print(nums.count(1))          # 2 — count occurrences
print(3 in nums)              # True — check membership</code></pre>

<h3>Iterating Over a List</h3>
<pre><code>fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())</code></pre>

<h3>Summary</h3>
<ul>
  <li>Lists are ordered, mutable collections. Use <code>[]</code> to create.</li>
  <li>Index with <code>[n]</code>, slice with <code>[start:end:step]</code></li>
  <li><code>append()</code>, <code>insert()</code>, <code>remove()</code>, <code>pop()</code> modify lists</li>
  <li>Iterate with <code>for item in list:</code></li>
</ul>
""".strip(),
        "quiz_title": "Lists Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "Which of the following creates a new list?", "option_a": "list = (1, 2, 3)", "option_b": "list = {1, 2, 3}", "option_c": "list = [1, 2, 3]", "option_d": "list = <1, 2, 3>", "correct_option": "C"},
            {"text": "What is the index of the first element in a Python list?", "option_a": "1", "option_b": "-1", "option_c": "0", "option_d": "First", "correct_option": "C"},
            {"text": "Which method adds an item to the end of a list?", "option_a": "insert()", "option_b": "add()", "option_c": "push()", "option_d": "append()", "correct_option": "D"},
            {"text": "What does nums[::-1] do?", "option_a": "Returns the first item", "option_b": "Returns a reversed copy of the list", "option_c": "Removes the last item", "option_d": "Sorts the list in reverse", "correct_option": "B"},
            {"text": "What is the result of len([10, 20, 30])?", "option_a": "2", "option_b": "30", "option_c": "10", "option_d": "3", "correct_option": "D"},
        ],
    },

    # ── Lesson 7: Dictionaries ────────────────────────────────────────────────
    {
        "order": 7,
        "title": "Dictionaries",
        "summary": "Store key-value pairs and look up data by descriptive keys.",
        "content": """
<p>A <strong>dictionary</strong> stores data as <strong>key-value pairs</strong>. Each key is unique and used to look up its associated value.</p>

<h3>Creating a Dictionary</h3>
<pre><code>student = {"name": "Alice", "age": 20, "grade": "A"}
empty_dict = {}</code></pre>

<h3>Accessing Values</h3>
<pre><code>student = {"name": "Alice", "age": 20}
print(student["name"])              # Alice
print(student.get("age"))           # 20
print(student.get("gpa", "N/A"))    # N/A (safe access with default)</code></pre>

<h3>Adding and Modifying</h3>
<pre><code>student["age"] = 21         # modify existing key
student["major"] = "CS"     # add a new key-value pair
# Result: {'name': 'Alice', 'age': 21, 'major': 'CS'}</code></pre>

<h3>Removing Items</h3>
<pre><code>del student["major"]          # delete a key
age = student.pop("age")      # remove and return the value
print(student)                # {'name': 'Alice'}</code></pre>

<h3>Iterating Over a Dictionary</h3>
<pre><code>student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student: print(key)                  # keys
for value in student.values(): print(value)     # values
for k, v in student.items(): print(f"{k}: {v}") # both</code></pre>

<h3>Checking Key Existence</h3>
<pre><code>if "name" in student: print("Name exists!")
if "gpa" not in student: print("GPA not set.")</code></pre>

<h3>Summary</h3>
<ul>
  <li>Dictionaries store <code>key: value</code> pairs</li>
  <li>Access with <code>dict[key]</code> or <code>dict.get(key, default)</code></li>
  <li>Iterate with <code>.keys()</code>, <code>.values()</code>, <code>.items()</code></li>
  <li>Keys must be unique and immutable (strings, numbers, tuples)</li>
</ul>
""".strip(),
        "quiz_title": "Dictionaries Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "Which of the following creates a dictionary?", "option_a": "d = [1, 2, 3]", "option_b": "d = {1, 2, 3}", "option_c": "d = {'a': 1, 'b': 2}", "option_d": "d = ('a': 1, 'b': 2)", "correct_option": "C"},
            {"text": "How do you safely access a dictionary key that might not exist?", "option_a": "dict[key]", "option_b": "dict.get(key)", "option_c": "dict.find(key)", "option_d": "dict[key] or None", "correct_option": "B"},
            {"text": "Which method returns all key-value pairs as tuples?", "option_a": ".keys()", "option_b": ".values()", "option_c": ".pairs()", "option_d": ".items()", "correct_option": "D"},
            {"text": "What does 'Alice' in {'name': 'Alice', 'age': 20} return?", "option_a": "True", "option_b": "Alice", "option_c": "False", "option_d": "20", "correct_option": "A"},
            {"text": "Which is NOT a valid dictionary key?", "option_a": '"color"', "option_b": "42", "option_c": "[1, 2, 3]", "option_d": "True", "correct_option": "C"},
        ],
    },

    # ── Lesson 8: Strings in Depth ────────────────────────────────────────────
    {
        "order": 8,
        "title": "Strings in Depth",
        "summary": "Master string manipulation with slicing, methods, and formatting.",
        "content": """
<p>Strings have a rich set of methods and Python treats them as <strong>sequences of characters</strong> — you can index, slice, and iterate over them just like lists.</p>

<h3>String Indexing and Slicing</h3>
<pre><code>msg = "Hello, Python!"
print(msg[0])      # H
print(msg[-1])     # !
print(msg[7:13])   # Python
print(msg[::-1])   # !nohtyP ,olleH (reversed)</code></pre>

<h3>Common String Methods</h3>
<pre><code>text = "  Python Programming  "
print(text.upper())              #   PYTHON PROGRAMMING
print(text.lower())              #   python programming
print(text.strip())              # "Python Programming"
print(text.find("Python"))       # 2
print("gram" in text)            # True
csv = "apple,banana,cherry"
items = csv.split(",")           # ['apple', 'banana', 'cherry']
joined = " | ".join(items)       # "apple | banana | cherry"
print(text.replace("Python", "Java"))</code></pre>

<h3>String Formatting</h3>
<pre><code>name = "Alice"; age = 20
print(f"My name is {name} and I am {age}.")
price = 49.95
print(f"Price: ${price:.2f}")    # Price: $49.95</code></pre>

<h3>Checking String Properties</h3>
<pre><code>print("hello".isalpha())          # True
print("123".isdigit())            # True
print("Hello".startswith("H"))    # True
print("world".endswith("d"))      # True</code></pre>

<h3>Summary</h3>
<ul>
  <li>Strings support indexing, slicing, and iteration like lists</li>
  <li>Key methods: <code>.upper()</code>, <code>.lower()</code>, <code>.strip()</code>, <code>.split()</code>, <code>.join()</code>, <code>.replace()</code></li>
  <li>Use f-strings for modern formatting</li>
</ul>
""".strip(),
        "quiz_title": "Strings in Depth Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "What does 'Python'[::-1] return?", "option_a": "nohtyP", "option_b": "Python", "option_c": "P", "option_d": "nohty", "correct_option": "A"},
            {"text": "Which method removes whitespace from both ends of a string?", "option_a": ".trim()", "option_b": ".strip()", "option_c": ".clean()", "option_d": ".remove()", "correct_option": "B"},
            {"text": "What does 'a,b,c'.split(',') return?", "option_a": "'a b c'", "option_b": "['a', 'b', 'c']", "option_c": "'a,b,c'", "option_d": "('a', 'b', 'c')", "correct_option": "B"},
            {"text": "Which method checks if a string contains only digits?", "option_a": ".isnum()", "option_b": ".isnumeric()", "option_c": ".isdigit()", "option_d": ".isinteger()", "correct_option": "C"},
            {"text": "What is the result of 'Hello'.find('lo')?", "option_a": "-1", "option_b": "3", "option_c": "2", "option_d": "0", "correct_option": "B"},
        ],
    },

    # ── Lesson 9: Tuples and Sets ─────────────────────────────────────────────
    {
        "order": 9,
        "title": "Tuples and Sets",
        "summary": "Immutable sequences with tuples and unordered unique elements with sets.",
        "content": """
<p>Two more useful collection types: <strong>tuples</strong> (immutable) and <strong>sets</strong> (unique elements).</p>

<h3>Tuples</h3>
<p>A <strong>tuple</strong> is an ordered, immutable collection. Use parentheses <code>()</code>:</p>
<pre><code>point = (3, 7)
colors = ("red", "green", "blue")
single = (42,)         # trailing comma required for single-element
print(point[0])        # 3
print(len(colors))     # 3</code></pre>

<h3>Why Use Tuples?</h3>
<pre><code>x, y = (10, 20)        # tuple unpacking
print(x, y)            # 10 20

a, b = b, a            # swap variables elegantly

def min_max(nums):
    return min(nums), max(nums)
result = min_max([3, 1, 4, 1, 5])
print(result)          # (1, 5)</code></pre>

<h3>Sets</h3>
<p>A <strong>set</strong> is an unordered collection of <strong>unique</strong> elements. Use curly braces:</p>
<pre><code>fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)          # {'cherry', 'banana', 'apple'} — duplicates removed
unique = set([1, 2, 2, 3, 3, 4])
print(unique)          # {1, 2, 3, 4}</code></pre>

<h3>Set Operations</h3>
<pre><code>a = {1, 2, 3, 4}; b = {3, 4, 5, 6}
print(a | b)    # Union: {1, 2, 3, 4, 5, 6}
print(a & b)    # Intersection: {3, 4}
print(a - b)    # Difference: {1, 2}
print(a ^ b)    # Symmetric diff: {1, 2, 5, 6}
a.add(7)        # Add element
a.discard(99)   # Safe remove (no error if missing)</code></pre>

<h3>Summary</h3>
<ul>
  <li>Tuples are immutable — use for fixed data</li>
  <li>Sets store unique elements with fast membership tests</li>
  <li>Sets support union, intersection, difference</li>
  <li>Use <code>set(list)</code> to remove duplicates</li>
</ul>
""".strip(),
        "quiz_title": "Tuples and Sets Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "Which of the following creates a tuple?", "option_a": "t = [1, 2, 3]", "option_b": "t = {1, 2, 3}", "option_c": "t = (1, 2, 3)", "option_d": "t = <1, 2, 3>", "correct_option": "C"},
            {"text": "What happens if you try to modify a tuple after creation?", "option_a": "The change succeeds", "option_b": "Python silently ignores it", "option_c": "Python raises an error", "option_d": "The tuple becomes a list", "correct_option": "C"},
            {"text": "What does set([1, 2, 2, 3, 3]) return?", "option_a": "[1, 2, 2, 3, 3]", "option_b": "{1, 2, 3}", "option_c": "[1, 2, 3]", "option_d": "{1, 2, 2, 3, 3}", "correct_option": "B"},
            {"text": "What does {1, 2, 3} & {2, 3, 4} return?", "option_a": "{1, 2, 3, 4}", "option_b": "{2, 3}", "option_c": "{1, 4}", "option_d": "{1, 2, 3, 2, 3, 4}", "correct_option": "B"},
            {"text": "Which set method safely removes an element without raising an error?", "option_a": ".remove()", "option_b": ".delete()", "option_c": ".pop()", "option_d": ".discard()", "correct_option": "D"},
        ],
    },

    # ── Lesson 10: List Comprehensions ────────────────────────────────────────
    {
        "order": 10,
        "title": "List Comprehensions",
        "summary": "Create lists concisely using Python's powerful comprehension syntax.",
        "content": """
<p>A <strong>list comprehension</strong> lets you create a new list by applying an expression to each item in an existing sequence — all in a single, readable line.</p>

<h3>Basic Syntax</h3>
<pre><code>new_list = [expression for item in iterable]</code></pre>

<h3>Simple Example</h3>
<pre><code># Traditional approach
squares = []
for i in range(10):
    squares.append(i ** 2)
# List comprehension (same result, one line)
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]</code></pre>

<h3>With a Condition</h3>
<pre><code># Even numbers only
evens = [x for x in range(20) if x % 2 == 0]
# Uppercase long names
names = ["alice", "bob", "charlie", "dave"]
long_names = [name.upper() for name in names if len(name) > 3]
print(long_names)  # ['ALICE', 'CHARLIE']</code></pre>

<h3>Transforming Data</h3>
<pre><code># Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
# Extract values from dictionaries
students = [{"name": "Alice", "grade": 85}, {"name": "Bob", "grade": 72}]
grades = [s["grade"] for s in students]</code></pre>

<h3>Nested Comprehensions</h3>
<pre><code># Flatten a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]</code></pre>

<h3>Summary</h3>
<ul>
  <li>Basic: <code>[expr for item in iterable]</code></li>
  <li>With filter: <code>[expr for item in iterable if condition]</code></li>
  <li>Use cautiously — don't nest more than 2 levels</li>
</ul>
""".strip(),
        "quiz_title": "List Comprehensions Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "What does [x * 2 for x in range(5)] return?", "option_a": "[2, 4, 6, 8, 10]", "option_b": "[0, 2, 4, 6, 8]", "option_c": "[0, 1, 2, 3, 4]", "option_d": "[1, 2, 3, 4, 5]", "correct_option": "B"},
            {"text": "What does [n for n in range(10) if n > 5] return?", "option_a": "[5, 6, 7, 8, 9]", "option_b": "[6, 7, 8, 9]", "option_c": "[0, 1, 2, 3, 4, 5]", "option_d": "[]", "correct_option": "B"},
            {"text": "How would you uppercase all names in a list?", "option_a": "[n.upper() for n in names]", "option_b": "[upper(n) for n in names]", "option_c": "[n for n in names].upper()", "option_d": "names.upper()", "correct_option": "A"},
            {"text": "Which line flattens a list of lists?", "option_a": "[row for row in matrix]", "option_b": "[num for num in row for row in matrix]", "option_c": "[num for row in matrix for num in row]", "option_d": "[num for num in matrix]", "correct_option": "C"},
            {"text": "What is the main advantage of list comprehensions?", "option_a": "Faster runtime", "option_b": "Use less memory", "option_c": "More concise and readable", "option_d": "Support while loops", "correct_option": "C"},
        ],
    },

    # ── Lesson 11: File I/O ───────────────────────────────────────────────────
    {
        "order": 11,
        "title": "File I/O",
        "summary": "Read from and write to files using Python's built-in file handling.",
        "content": """
<p>Python makes it easy to work with files. Use the built-in <code>open()</code> function with a <strong>context manager</strong> (<code>with</code> statement) — it automatically closes the file when you're done.</p>

<h3>File Modes</h3>
<ul>
  <li><code>"r"</code> — read (default)</li>
  <li><code>"w"</code> — write (overwrites existing content)</li>
  <li><code>"a"</code> — append (adds to existing content)</li>
  <li><code>"x"</code> — exclusive creation (fails if file exists)</li>
  <li><code>"r+"</code> — read and write</li>
</ul>

<h3>Reading Files</h3>
<pre><code># Read entire file
with open("data.txt", "r") as f:
    content = f.read()

# Read line by line (memory efficient)
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into a list
with open("data.txt", "r") as f:
    lines = f.readlines()</code></pre>

<h3>Writing Files</h3>
<pre><code># Write (overwrites)
with open("output.txt", "w") as f:
    f.write("Hello, file!\n")

# Append
with open("output.txt", "a") as f:
    f.write("This line is appended.\n")</code></pre>

<h3>Error Handling with Files</h3>
<pre><code>try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")</code></pre>

<h3>Summary</h3>
<ul>
  <li>Always use <code>with open()</code> for automatic file closing</li>
  <li>Use <code>for line in file</code> for memory-efficient reading</li>
  <li>Handle <code>FileNotFoundError</code> when reading</li>
</ul>
""".strip(),
        "quiz_title": "File I/O Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "Which statement is the safest way to open and work with a file?", "option_a": "file = open('data.txt')", "option_b": "with open('data.txt') as file:", "option_c": "open('data.txt').read()", "option_d": "file.open('data.txt')", "correct_option": "B"},
            {"text": "What file mode should you use to append to an existing file?", "option_a": '"w"', "option_b": '"r"', "option_c": '"x"', "option_d": '"a"', "correct_option": "D"},
            {"text": "What happens if you open a file in mode 'w' and it already exists?", "option_a": "Python raises an error", "option_b": "The file is overwritten", "option_c": "Data is appended", "option_d": "Nothing — file stays unchanged", "correct_option": "B"},
            {"text": "Which method reads a file into a list of lines?", "option_a": ".read()", "option_b": ".readline()", "option_c": ".readlines()", "option_d": ".splitlines()", "correct_option": "C"},
            {"text": "What exception is raised when opening a file that doesn't exist?", "option_a": "FileError", "option_b": "IOError", "option_c": "FileNotFoundError", "option_d": "MissingFileError", "correct_option": "C"},
        ],
    },

    # ── Lesson 12: Error Handling ─────────────────────────────────────────────
    {
        "order": 12,
        "title": "Error Handling",
        "summary": "Handle errors gracefully using try, except, else, and finally.",
        "content": """
<p>Errors happen — files go missing, users enter invalid input. <strong>Error handling</strong> lets your program respond gracefully instead of crashing.</p>

<h3>Try and Except</h3>
<pre><code>try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")</code></pre>

<h3>Multiple Exception Types</h3>
<pre><code>try:
    data = open("missing.txt").read()
    result = 10 / len(data)
except (FileNotFoundError, ZeroDivisionError) as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Something went wrong: {e}")</code></pre>

<h3>Else and Finally</h3>
<pre><code>try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print(f"Read {len(content)} characters.")
finally:
    print("Cleanup complete.")  # Always runs</code></pre>

<h3>Raising Exceptions</h3>
<pre><code>def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")
try:
    set_age(-5)
except ValueError as e:
    print(e)</code></pre>

<h3>Common Built-in Exceptions</h3>
<ul>
  <li><code>ValueError</code> — wrong value type</li>
  <li><code>TypeError</code> — wrong operation</li>
  <li><code>IndexError</code> — list index out of range</li>
  <li><code>KeyError</code> — dictionary key not found</li>
  <li><code>FileNotFoundError</code> — file doesn't exist</li>
  <li><code>ZeroDivisionError</code> — division by zero</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Use <code>try</code>/<code>except</code> to handle errors gracefully</li>
  <li><code>else</code> runs when no error occurs; <code>finally</code> always runs</li>
  <li>Raise custom errors with <code>raise</code></li>
  <li>Be specific about what you catch — don't catch everything blindly</li>
</ul>
""".strip(),
        "quiz_title": "Error Handling Quiz",
        "pass_mark": 60,
        "questions": [
            {"text": "Which keyword starts the error-handling block in Python?", "option_a": "catch", "option_b": "try", "option_c": "handle", "option_d": "error", "correct_option": "B"},
            {"text": "When does the else block run in try/except/else?", "option_a": "Before the try block", "option_b": "Only if an exception is raised", "option_c": "Only if NO exception is raised", "option_d": "Always", "correct_option": "C"},
            {"text": "What does the finally block do?", "option_a": "Runs only if no error occurs", "option_b": "Runs only if an error occurs", "option_c": "Always runs, even if an exception is raised", "option_d": "Stops the program", "correct_option": "C"},
            {"text": "How do you raise a custom exception?", "option_a": "error ValueError", "option_b": "raise ValueError('message')", "option_c": "throw ValueError('message')", "option_d": "new ValueError('message')", "correct_option": "B"},
            {"text": "What exception is raised when accessing list[10] on a list with 3 items?", "option_a": "ValueError", "option_b": "KeyError", "option_c": "OutOfBoundsError", "option_d": "IndexError", "correct_option": "D"},
        ],
    },
]


class Command(BaseCommand):
    help = "Seed the database with 12 Python lessons, quizzes, and questions."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all existing lessons, quizzes, and questions before seeding.",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            Question.objects.all().delete()
            Quiz.objects.all().delete()
            Lesson.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared existing data."))

        created_lessons = 0
        created_quizzes = 0
        created_questions = 0

        for data in LESSONS:
            lesson, lesson_created = Lesson.objects.get_or_create(
                order=data["order"],
                defaults={
                    "title": data["title"],
                    "summary": data["summary"],
                    "content": data["content"],
                    "is_published": True,
                },
            )
            if lesson_created:
                created_lessons += 1
                self.stdout.write(f"  Created lesson: {lesson}")
            else:
                self.stdout.write(f"  Lesson already exists, skipping: {lesson}")
                continue

            quiz = Quiz.objects.create(
                lesson=lesson,
                title=data["quiz_title"],
                pass_mark=data["pass_mark"],
            )
            created_quizzes += 1

            for q_data in data["questions"]:
                Question.objects.create(
                    quiz=quiz,
                    text=q_data["text"],
                    option_a=q_data["option_a"],
                    option_b=q_data["option_b"],
                    option_c=q_data["option_c"],
                    option_d=q_data["option_d"],
                    correct_option=q_data["correct_option"],
                )
                created_questions += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone! Created {created_lessons} lesson(s), "
                f"{created_quizzes} quiz(zes), "
                f"{created_questions} question(s)."
            )
        )