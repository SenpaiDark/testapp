"""
Management command to seed all 5 Python lessons, their quizzes, and questions.

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
            {
                "text": "Which function is used to display output in Python?",
                "option_a": "show()",
                "option_b": "print()",
                "option_c": "display()",
                "option_d": "output()",
                "correct_option": "B",
            },
            {
                "text": "Which symbol is used to write a comment in Python?",
                "option_a": "//",
                "option_b": "/* */",
                "option_c": "--",
                "option_d": "#",
                "correct_option": "D",
            },
            {
                "text": "Python is best described as a _____ programming language.",
                "option_a": "Machine-level",
                "option_b": "Assembly",
                "option_c": "High-level",
                "option_d": "Binary",
                "correct_option": "C",
            },
            {
                "text": "What is the correct file extension for a Python source file?",
                "option_a": ".pt",
                "option_b": ".pyt",
                "option_c": ".py",
                "option_d": ".python",
                "correct_option": "C",
            },
            {
                "text": "What is the result of print(2 ** 3) in Python?",
                "option_a": "6",
                "option_b": "5",
                "option_c": "9",
                "option_d": "8",
                "correct_option": "D",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Lesson 2
    # ─────────────────────────────────────────────────────────────────
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
<pre><code>print(type(42))        # &lt;class 'int'&gt;
print(type(3.14))      # &lt;class 'float'&gt;
print(type("hello"))   # &lt;class 'str'&gt;
print(type(True))      # &lt;class 'bool'&gt;</code></pre>

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
            {
                "text": "What data type is the value 3.14 in Python?",
                "option_a": "int",
                "option_b": "str",
                "option_c": "bool",
                "option_d": "float",
                "correct_option": "D",
            },
            {
                "text": "What does the type() function do?",
                "option_a": "Converts a value to a different type",
                "option_b": "Returns the data type of a value",
                "option_c": "Prints the value to the screen",
                "option_d": "Deletes the variable",
                "correct_option": "B",
            },
            {
                "text": "Which of the following is a valid Python variable name?",
                "option_a": "2fast",
                "option_b": "my-name",
                "option_c": "my name",
                "option_d": "my_name",
                "correct_option": "D",
            },
            {
                "text": "What is the value of bool(0) in Python?",
                "option_a": "True",
                "option_b": "1",
                "option_c": "False",
                "option_d": "None",
                "correct_option": "C",
            },
            {
                "text": "What function converts the string \"42\" into an integer?",
                "option_a": "str(\"42\")",
                "option_b": "float(\"42\")",
                "option_c": "int(\"42\")",
                "option_d": "convert(\"42\")",
                "correct_option": "C",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Lesson 3
    # ─────────────────────────────────────────────────────────────────
    {
        "order": 3,
        "title": "Conditional Statements",
        "summary": "Make decisions in your code using if, elif, and else.",
        "content": """
<p>Programs often need to make decisions. <strong>Conditional statements</strong> let your code do different things depending on whether a condition is <code>True</code> or <code>False</code>.</p>

<h3>The if Statement</h3>
<p>The simplest form checks a single condition:</p>
<pre><code>age = 18

if age >= 18:
    print("You are an adult.")</code></pre>
<p>Notice the <strong>colon</strong> (<code>:</code>) after the condition and the <strong>indentation</strong> (4 spaces or a tab) before the code inside the block. Python uses indentation to group code — this is mandatory.</p>

<h3>if / else</h3>
<p>Use <code>else</code> to handle the case when the condition is <code>False</code>:</p>
<pre><code>score = 45

if score >= 50:
    print("You passed!")
else:
    print("You need to try again.")</code></pre>

<h3>if / elif / else</h3>
<p>Use <code>elif</code> (short for "else if") to check multiple conditions in sequence:</p>
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
  <li><code>&gt;</code> greater than</li>
  <li><code>&lt;</code> less than</li>
  <li><code>&gt;=</code> greater than or equal to</li>
  <li><code>&lt;=</code> less than or equal to</li>
</ul>

<h3>Logical Operators</h3>
<p>Combine multiple conditions with <code>and</code>, <code>or</code>, and <code>not</code>:</p>
<pre><code>age = 20
has_id = True

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
            {
                "text": "What keyword starts a conditional block in Python?",
                "option_a": "when",
                "option_b": "case",
                "option_c": "if",
                "option_d": "check",
                "correct_option": "C",
            },
            {
                "text": "What is the output of this code?\n\nx = 10\nif x > 5:\n    print('big')\nelse:\n    print('small')",
                "option_a": "small",
                "option_b": "big",
                "option_c": "10",
                "option_d": "Error",
                "correct_option": "B",
            },
            {
                "text": "Which keyword handles additional conditions after an initial if?",
                "option_a": "else if",
                "option_b": "elseif",
                "option_c": "elif",
                "option_d": "otherwise",
                "correct_option": "C",
            },
            {
                "text": "What is the result of the expression: 5 != 5",
                "option_a": "True",
                "option_b": "None",
                "option_c": "Error",
                "option_d": "False",
                "correct_option": "D",
            },
            {
                "text": "Which logical operator returns True only when BOTH conditions are True?",
                "option_a": "or",
                "option_b": "not",
                "option_c": "and",
                "option_d": "xor",
                "correct_option": "C",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Lesson 4
    # ─────────────────────────────────────────────────────────────────
    {
        "order": 4,
        "title": "Loops",
        "summary": "Repeat actions efficiently using for loops and while loops.",
        "content": """
<p>A <strong>loop</strong> lets you run the same block of code multiple times without writing it out repeatedly. Python has two main types: <code>for</code> loops and <code>while</code> loops.</p>

<h3>The for Loop</h3>
<p>A <code>for</code> loop iterates over a sequence (like a list or range of numbers):</p>
<pre><code>for i in range(5):
    print(i)
# Output: 0 1 2 3 4</code></pre>

<h3>The range() Function</h3>
<p><code>range()</code> generates a sequence of numbers. It has three forms:</p>
<pre><code>range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8  (step = 2)</code></pre>

<h3>Looping Over a List</h3>
<pre><code>fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# Output: apple  banana  cherry</code></pre>

<h3>The while Loop</h3>
<p>A <code>while</code> loop keeps running as long as its condition remains <code>True</code>:</p>
<pre><code>count = 0

while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4</code></pre>
<p><strong>Warning:</strong> always make sure the condition eventually becomes <code>False</code>, or the loop will run forever (infinite loop).</p>

<h3>break and continue</h3>
<p><code>break</code> exits the loop immediately. <code>continue</code> skips the rest of the current iteration and jumps to the next one.</p>
<pre><code># break example
for i in range(10):
    if i == 5:
        break       # stop the loop when i equals 5
    print(i)
# Output: 0 1 2 3 4

# continue example
for i in range(6):
    if i == 3:
        continue    # skip 3
    print(i)
# Output: 0 1 2 4 5</code></pre>
""".strip(),
        "quiz_title": "Loops Quiz",
        "pass_mark": 60,
        "questions": [
            {
                "text": "What numbers does range(5) produce?",
                "option_a": "1, 2, 3, 4, 5",
                "option_b": "0, 1, 2, 3, 4",
                "option_c": "0, 1, 2, 3, 4, 5",
                "option_d": "1, 2, 3, 4",
                "correct_option": "B",
            },
            {
                "text": "Which keyword immediately exits a loop?",
                "option_a": "exit",
                "option_b": "stop",
                "option_c": "continue",
                "option_d": "break",
                "correct_option": "D",
            },
            {
                "text": "What does the continue keyword do inside a loop?",
                "option_a": "Exits the loop entirely",
                "option_b": "Restarts the program",
                "option_c": "Skips the rest of the current iteration",
                "option_d": "Pauses the loop",
                "correct_option": "C",
            },
            {
                "text": "A while loop keeps running as long as its condition is ___.",
                "option_a": "False",
                "option_b": "Zero",
                "option_c": "None",
                "option_d": "True",
                "correct_option": "D",
            },
            {
                "text": "What is the output of:\n\nfor i in range(3):\n    print(i)",
                "option_a": "1 2 3",
                "option_b": "0 1 2 3",
                "option_c": "0 1 2",
                "option_d": "1 2",
                "correct_option": "C",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Lesson 5
    # ─────────────────────────────────────────────────────────────────
    {
        "order": 5,
        "title": "Functions",
        "summary": "Write reusable blocks of code with parameters, return values, and defaults.",
        "content": """
<p>A <strong>function</strong> is a reusable block of code that performs a specific task. Instead of writing the same logic over and over, you define it once and call it whenever you need it.</p>

<h3>Defining a Function</h3>
<p>Use the <code>def</code> keyword, followed by the function name, parentheses, and a colon. The function body is indented:</p>
<pre><code>def greet():
    print("Hello from the function!")

greet()   # calling the function
# Output: Hello from the function!</code></pre>

<h3>Parameters and Arguments</h3>
<p><strong>Parameters</strong> are variables listed inside the parentheses when defining a function. <strong>Arguments</strong> are the actual values you pass when calling it:</p>
<pre><code>def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!</code></pre>

<h3>The return Statement</h3>
<p>Use <code>return</code> to send a value back from the function to wherever it was called:</p>
<pre><code>def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8</code></pre>

<h3>Default Parameters</h3>
<p>You can give a parameter a default value. If the caller does not provide that argument, the default is used:</p>
<pre><code>def power(base, exponent=2):
    return base ** exponent

print(power(4))      # 16  (uses default exponent = 2)
print(power(2, 10))  # 1024 (overrides default)</code></pre>

<h3>Why Use Functions?</h3>
<ul>
  <li><strong>Reusability</strong> — write once, use anywhere</li>
  <li><strong>Readability</strong> — give meaningful names to blocks of logic</li>
  <li><strong>Maintainability</strong> — fix a bug in one place instead of many</li>
</ul>

<pre><code># A complete example
def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

print(calculate_grade(85))  # A
print(calculate_grade(55))  # C
print(calculate_grade(40))  # F</code></pre>
""".strip(),
        "quiz_title": "Functions Quiz",
        "pass_mark": 60,
        "questions": [
            {
                "text": "What keyword is used to define a function in Python?",
                "option_a": "function",
                "option_b": "func",
                "option_c": "define",
                "option_d": "def",
                "correct_option": "D",
            },
            {
                "text": "What keyword sends a value back from a function?",
                "option_a": "send",
                "option_b": "output",
                "option_c": "return",
                "option_d": "give",
                "correct_option": "C",
            },
            {
                "text": "What is the output of:\n\ndef greet():\n    return \"Hi\"\nprint(greet())",
                "option_a": "greet",
                "option_b": "None",
                "option_c": "Error",
                "option_d": "Hi",
                "correct_option": "D",
            },
            {
                "text": "In def power(base, exponent=2): what is exponent=2 called?",
                "option_a": "Required parameter",
                "option_b": "Global variable",
                "option_c": "Default parameter",
                "option_d": "Return value",
                "correct_option": "C",
            },
            {
                "text": "How do you correctly call a function named calculate?",
                "option_a": "run calculate()",
                "option_b": "call calculate()",
                "option_c": "calculate()",
                "option_d": "execute calculate()",
                "correct_option": "C",
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed the database with 5 Python lessons, quizzes, and questions."

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
