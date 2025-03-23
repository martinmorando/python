'''
    Topics: add markers, change linestyle, and change line color
'''

import matplotlib.pyplot as plt

X = range(15)
Y = list(map(lambda x: x**2, X))

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Squaring function")

plt.grid()

'''
  Plot the graph
    - Markers available: "o"(circle), "s" (square), "*" (star)
    - Linestyles available: "solid", "dotted", "dashed", "dashdot"
    - Colors: also accepts hex colors (#FFAA88)
'''
plt.plot(X, Y, marker="o", linestyle="solid", color="green")

plt.show()