'''
    Loops
'''

numbers = list(range(1,11))

# Iterate over items in "numbers" list
for n in numbers:
    print(n)


# Iterate over items until condition is met
for n in numbers:        
    if (n == 5):
        print("I'M BREAKING FREE")
        break
    print(n)


# Iterate over items and skip on certain condition
for n in numbers:    
    if (n == 5):
        continue    # 5 won't get printed
    print(n)