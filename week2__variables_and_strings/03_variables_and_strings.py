# 03_variables_and_strings.py
# 1. String Indexing & Slicing

# len() counts characters in a *string*
print(len("Hello"))          # 5
print(len("1000"))           # 4

# An int has no length – uncommenting the next line raises
# TypeError: object of type 'int' has no len()
# len(4)

# Indexing is 0‑based
print("Hello"[0])            # 'H'
print("Hello"[1])            # 'e'
print("Hello"[-1])           # 'o'  # negative indices count from the end

# Slicing: start is inclusive, stop is exclusive
print("Hello"[0:3])          # 'Hel'

sentence = "I say Hello."
print(len(sentence))          # 12 (includes space & period)
print(sentence[:])            # full string
print(sentence[:-1])          # without last char
print(sentence[1:4])          # ' sa'

# 2. Variables

name = "Haley"

# Variable‑naming rules (Python/PEP 8):
# starts with a letter or underscore
# cannot start with a digit
# no spaces; use _ for multi‑word names
# case‑sensitive
# cannot be a Python keyword (if, else, def…)

print("My name is " + name)
print(type(name))    # <class 'str'>

# VS Code shortcut: Ctrl+/ toggles comments on selected lines.

# 3. String Formatting

job = "programmer"
age = 15

# 3‑1 Concatenation (requires str() for non‑string pieces)
print("Hello. My name is " + name +
      ". My job is " + job +
      ". My age is " + str(age) + ".")

# 3‑2 Old %-formatting
print("Hello. My name is %s. My job is %s. My age is %s." %
      (name, job, age))

# 3‑3 str.format()
print("Hello. My name is {0}. My job is {1}. My age is {2}.".format(name, job, age))

# 3‑4 f‑string (Python 3.6+)
print(f"Hello. My name is {name}. My job is {job}. My age is {age}.")


# 4. Repetition example

# Instead of copy‑pasting the same line many times:
for _ in range(7):
    print("My name is " + name)

# or repeat with * operator
print(("My name is " + name + "\n") * 7)

# 5. VS Code Quick Reference

# Alt+J   → soft‑wrap (visual only, doesn’t add newline)
# Ctrl+/  → toggle comment
