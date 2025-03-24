'''
    Lists
'''

# [CREATE LISTS]
empty = []
strings = ["A", "B", "C"]
numbers = [1, 2, 3]
mixed = ["A", 1, 0.99, True]
repetitive_list = ["C", "A", "C", "B", "A"]

# - Create a consecutive list with integers from 0 up to 99 included
# (list() is necessary because range() returns a range object)
list(range(100))            # [0, 1, 2, 3,..., 98, 99]

# - Create a list with integers from 20 up to 99, incrementing by 5
list(range(20, 100, 5))     # [20, 25, 30, 35,..., 90, 95]



# [LENGTH]: get the number of elements inside a list
len(mixed)                  # 4


# [COUNT]: count specific element inside a list
repetitive_list.count("C")  # 2



# [ACCESS ITEM]: the 1st item of "strings" list
strings[0]



# [MODIFY ITEM]: the 1st item from "strings" list
strings[0] = "AA"           # 'AA'



# [ADD ITEMS]
# - Add an item to the end of "strings" list
strings.append("D")         # strings: ['A', 'B', 'C', 'D']

# - Insert by index (can use negative indexes)
strings.insert(1, "A2")     # strings: ['A', 'A2', 'B', 'C', 'D']



# [REMOVE ITEMS]
# - Remove a specific item (first match only)
strings.remove("B")         # strings: ['A', 'A2' 'C', 'D']

# - Remove the last item
strings.pop()               # strings: ['A', 'A2', 'C']



# [ADD LISTS]
# - Add 2 lists
mixed_2 = strings + numbers # ['AA', 'A2', 'C', 1, 2, 3]

# - Add a list that contains one item
mixed_3 = strings + [4]     # ['AA', 'A2', 'C', 4]
# This is wrong: mixed_4 = strings + 4



# [SLICE]: extract a portion of a list
example_list = list(range(3, 11))   # [3, 4, 5, 6, 7, 8, 9, 10]

# - Slice the list to get elements from index 3 to 4 (index 5 is excluded)
example_list[3:5]                   # [6, 7]

# - Slice the list to get elements from index 0 to index 3 included
example_list[:4]                    # [3, 4, 5, 6]

# - Slice the list to get all elements except last 2
example_list[:-2]                   # [3, 4, 5, 6, 7, 8]

# - Slice the list to get all elements from index 5 to the end
example_list[5:]                    # [8, 9, 10]



# [SORT]
another_list = [3, 7, 1, 5, 8]
disordered_letters = ["d", "a", "c", "g"]

# - Sort ascending order
another_list.sort()                 # None (no return value, sorts directly)
print(another_list)                 # [1, 3, 5, 7, 8]

disordered_letters.sort()
print(disordered_letters)           # ['a', 'c', 'd', 'g']


# - Sort descending order
another_list.sort(reverse=True)     # None (no return value, sorts directly)
print(another_list)                 # [8, 7, 5, 3, 1]



# [SORTED]: similar to sort but creates a new list
disordered_letters_2 = ["d", "a", "c", "g"]
ordered_letters = sorted(disordered_letters_2)
print(ordered_letters)              # ['a', 'c', 'd', 'g']



# [ZIP]: combine 2 lists into a list of tuples, where each tuple
# contains one element from each list at the same index
list(zip(numbers, strings))         # [(1, 'AA'), (2, 'A2'), (3, 'C')]