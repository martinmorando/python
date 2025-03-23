'''
    Strings
'''

# Multi-line strings (""" or ''')
multiLine = """
A purely peer-to-peer version of electronic cash would allow online
payments to be sent directly from one party to another without going through a
financial institution. Digital signatures provide part of the solution, but the main
benefits are lost if a trusted third party is still required to prevent double-spending.
We propose a solution to the double-spending problem using a peer-to-peer network.
The network timestamps transactions by hashing them into an ongoing chain of
hash-based proof-of-work, forming a record that cannot be changed without redoing
the proof-of-work.
"""


# Concatenation
a = "Hello"
b = "Goodbye"
c = 2
print(a + " " + b + ". See you in " + str(c) + " halvings.")


# Formatting
# Alternative A
print("{} {}. See you in {} halvings.".format(a, b, c))
# Alternative B
print("{x} {y}. See you in {z} halvings.".format(x=a, y=b, z=c))


# Length
alphabet = "abcdefghijklmnopqrstuvwxyz"
print( len(alphabet) )


# Select letters, slice strings
print("1st letter:", alphabet[0])
print("Last letter:", alphabet[-1])
print("3rd letter to last one:", alphabet[2:]) 


# Replace
message = "The authoritarian could not tolerate individuals using bitcoin to carry out voluntary transactions outside of his control."
new_message = message.replace("bitcoin", "#bitcoin")
print(new_message)


# Check and locate a substring
# Is this string inside the other string?
target = "authoritarian"
if target in message:
	print("Yes")
	
# Where is it?
# If found, returns the index of the starting letter
# If not found, returns -1
index = message.find("asd")