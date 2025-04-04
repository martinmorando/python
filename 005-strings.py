'''
    Strings
    - Both valid: single quotes ('') and double quotes ("").
    - Think of a list of characters (see 007-lists.py).
    - Inmutable: can't be changed.
'''

goal = "freedom"

# Access the first character
print(goal[0])              # Output: f

# Slice [first_index:last_index]
print(goal[1:3])            # Output: re
print(goal[:2])             # Output: fr
print(goal[2:])             # Output: eedom

# Length
print(len(goal))            # Output: 7

# String methods
print(goal.lower())         # Output: freedom
print(goal.upper())         # Output: FREEDOM