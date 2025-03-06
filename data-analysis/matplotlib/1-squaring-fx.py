'''
Graph with Matplotlib.

In this case, also using tkinter to display the graph in a window.
'''

# Import matplotlib
import matplotlib.pyplot as plt
import matplotlib

# Set the backend to TkAgg
matplotlib.use("TkAgg") 

# X and Y values
x = range(15)
y = list(map(lambda x: x**2, x))

# Add labels
plt.xlabel("X")
plt.ylabel("Y")

# Add a title
plt.title("Squaring function")

# Add a grid
plt.grid()

# Plot the graph
plt.plot(x, y)

# Optional: save the graph as a .png.
# Seems it needs to go after .plot() but before .show()
# If not, only saves a white image
plt.savefig("plot.png")

# Show the graph
plt.show()