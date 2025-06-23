# Type checking
# In the Python terminal (REPL), we confirmed that:
# type("Hello") → <class 'str'>
# type("1")     → <class 'str'>
# type(" ")     → <class 'str'>
# type("")      → <class 'str'>

# Simple print statements
print("Hello")
print("""
      Hello
      World
      """)

# Newline and tab characters
print("Hello\nWorld\nHi")     # \n = new line
print("Hello\tWorld\tHi")     # \t = tab space

# Quotation marks inside strings
print("I said \"Hello\" to you.")      # Use \" to include double quotes inside double-quoted strings
print('I said "Hello" to you.')        # Mixing quotes
print("I said \'Hello\' to you.")      # Use \' to include single quotes

# Backslash
print("\\")                            # \\ prints a single backslash

# String operations
print(type("Hello"))                   # <class 'str'>
print("hi" + "friends")                # Concatenation
print("hi" + " " + "friends")          # Concatenation with space
print("*" * 20)                        # Repetition: prints ********************

# 1. Mismatched quotation marks cause SyntaxError
# "hi" + "friends'  ← unmatched quotes
# 2. Using invalid operators like - with strings causes TypeError
# "Hi" - "Hello"    ← unsupported operand for string