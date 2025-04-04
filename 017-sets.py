'''
    Sets
    - Group of unordered elements and no duplicates.
    - Can contain any combination of data types.
'''

# [CREATE]
# - Alternative A: using {}
lettersA = {"A", "B", "C", "D", "D"}
print(lettersA)              # Output: {'B', 'C', 'A', 'D'}

# - Alternative B: using set()
lettersB = set(["A", "B", "C", "D", "D"])
print(lettersB)              # Output: {'A', 'C', 'B', 'D'}

# - Create a frozen set (inmutable)
frozenB = frozenset(lettersB)
print(frozenB)               # Output: frozenset({'C', 'D', 'A', 'B'})



# [ADD]
# - Add 1 element to a set
lettersA.add("E")
print(lettersA)              # Output: {'D', 'B', 'A', 'E', 'C'} 

# - Add several elements to a set
lettersA.update(["F", 1.23])
print(lettersA)              # Output: {1.23, 'B', 'C', 'E', 'A', 'D', 'F'}