'''
    Topics: add labels, title, grid, plot, and save as PNG
'''

# Import matplotlib
import matplotlib.pyplot as plt

# Straight line: y = mx + b
# X values (input), m (slope), b (y-intercept), Y values (output)
X = range(30)
m = 2
b = 25
Y = [m*x + b for x in X]

# Add labels
plt.xlabel("X")
plt.ylabel("Y")

# Add a title
plt.title("A straight line")

# Add a grid
plt.grid()

# Plot the graph
plt.plot(X, Y)

'''
  Optional: save the graph as a .png.
    - Seems it needs to go after .plot() but before .show()
    If not, only saves a white image
plt.savefig("fileName.png")
'''

# Display the graph
plt.show()