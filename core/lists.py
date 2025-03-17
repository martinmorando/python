'''
    Lists
'''

# [Create lists]
empty = []
strings = ["A", "B", "C"]
numbers = [1, 2, 3]
mixed = ["A", 1, 0.99, True]



# - Create a list with integers from 0 up to 99 included
# (list() is necessary because range() returns a range object)
list(range(100))            # [0, 1, 2, 3,..., 98, 99]

# - Create a list with integers from 20 up to 99, incrementing by 5
list(range(20, 100, 5))     # [20, 25, 30, 35,..., 90, 95]



# [Count items inside list]
len(mixed)                  # 4



# [Access]: the 1st item of "strings" list
strings[0]



# [Add]: an item to "strings" list
strings.append("D")         # ["A", "B", "C", "D"]



# [Remove]
# - Remove a specific item (first match only)
strings.remove("B")         # ["A", "C", "D"]

# - Remove the last item
strings.pop()               # ["A", "C"]



# [Modify]: the 1st item from "strings" list
strings[0] = "AA"           # ["AA", "C"]



# [Add lists]
# - Add 2 lists
mixed_2 = strings + numbers # ["AA", "C", 1, 2, 3]

# - Add a list that contains one item
mixed_3 = strings + [4]     # ["AA", "C", 4]
# This is wrong: mixed_4 = strings + 4



# [Zip]: combine 2 lists into a list of tuples, where each tuple
# contains one element from each list at the same index
list(zip(numbers, strings))  # [(1, 'AA'), (2, 'C')]



# [Slice]
example_list = list(range(3, 11))   # [3, 4, 5..., 9, 10]

# - Slice the list to get elements from index 3 to 4 (index 5 is excluded)
example_list[3:5]                   # [6, 7]



# [Sort]
# - Sort ascending order
another_list = [3, 7, 1, 5, 8]
another_list.sort()                 # None (no return value, sorts directly)
print(another_list)                 # [1, 3, 5, 7, 8]

# - Sort descending order
another_list.sort(reverse=True)     # None (no return value, sorts directly)
print(another_list)                 # [8, 7, 5, 3, 1]