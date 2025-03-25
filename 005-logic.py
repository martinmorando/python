'''
    Logic
'''

a = 2
b = 3

# Boolean operators: and, or, not
print((a == 2) and (b == 3))        # Output: True
print((a == 2) or (b == 4))         # Output: True
print(not a == 1)                   # Output: True


# Conditional
if (a > b):
    print("a > b")
elif (a < b):
    print("a < b")
else:
    print("a = b")


# Match statements, only valid since Python 3.10
match a:
    case 0:
        print("Case", 0)
    case 1:
        print("Case", 1)
    case 2:
        print("Case", 2)
    case default:
        print("?")