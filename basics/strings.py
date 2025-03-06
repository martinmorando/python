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
print("1st letter to last one:", alphabet[2:]) 



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