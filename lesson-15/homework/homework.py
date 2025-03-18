import matplotlib.pyplot as plt
import numpy as np



#task1
x= np.linspace(-10, 10, 100)
y = x**2-4*x+4
plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 4$", color="blue")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of $f(x) = x^2 - 4x + 4$")
plt.show()
#task2
x_pi = np.linspace(0, 2*np.pi, 400)
y_sin = np.sin(x_pi)
y_cos = np.cos(x_pi)
plt.plot(x_pi, y_sin, linestyle="--", marker="o", color="blue", label=r"$\sin(x)$")
plt.plot(x_pi, y_cos, linestyle="-.", marker="s", color="red", label=r"$\cos(x)$")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of $\sin(x)$ and $\cos(x)$")
plt.show()

#task3

# Define x values
x1 = np.linspace(-2, 2, 400)  # For x^3
x2 = np.linspace(0, 2*np.pi, 400)  # For sin(x)
x3 = np.linspace(-2, 2, 400)  # For e^x
x4 = np.linspace(0, 5, 400)  # For log(x+1)

y1 = x1**3
y2 = np.sin(x2)
y3 = np.exp(x3)
y4 = np.log(x4 + 1)

# Create subplots using plt.subplot()
plt.figure(figsize=(10, 8))

# Top-left: f(x) = x³
plt.subplot(2, 2, 1)
plt.plot(x1, y1, color="blue")
plt.title(r"$f(x) = x^3$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Top-right: f(x) = sin(x)
plt.subplot(2, 2, 2)
plt.plot(x2, y2, color="red", linestyle="--")
plt.title(r"$f(x) = \sin(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Bottom-left: f(x) = e^x
plt.subplot(2, 2, 3)
plt.plot(x3, y3, color="green", linestyle="-.")
plt.title(r"$f(x) = e^x$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Bottom-right: f(x) = log(x+1)
plt.subplot(2, 2, 4)
plt.plot(x4, y4, color="purple", linestyle=":")
plt.title(r"$f(x) = \log(x+1)$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.tight_layout()

# Show the plots
plt.show()

#task4


np.random.seed(42) 
x_random = np.random.uniform(0, 10, 100)
y_random = np.random.uniform(0, 10, 100)

# Define a set of different markers
marker_styles = ['o', 's', 'D', 'v', '^']  # Circle, square, diamond, triangle-down, triangle-up

# Assign markers in a repeating pattern
num_markers = len(marker_styles)
markers = [marker_styles[i % num_markers] for i in range(100)]

# Create the scatter plot
plt.figure(figsize=(8, 6))

for i in range(100):
    plt.scatter(x_random[i], y_random[i], color=plt.cm.viridis(i / 100), marker=markers[i], s=80)  # Fixed different markers

# Add title and labels
plt.title("Scatter Plot of 100 Random Points", fontsize=14)
plt.xlabel("X values", fontsize=12)
plt.ylabel("Y values", fontsize=12)

# Add a grid
plt.grid(True, linestyle="--", alpha=0.6)

# Show the plot
plt.show()


# task5


np.random.seed(42)  # For reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)

# Plot histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='blue', edgecolor='black')  # Adjust transparency with alpha

# Add title and axis labels
plt.title("Histogram of Normally Distributed Data (Mean=0, Std=1)", fontsize=14)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# Show the plot
plt.show()

#task6

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)

xx, yy = np.meshgrid(x, y)

zz = np.cos(xx**2 + yy**2)

ax.plot_surface(xx, yy, zz, cmap='viridis')
plt.show()

#task7

# Product names and sales data
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

# Custom colors for bars
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Create bar chart
plt.figure(figsize=(8, 5))  # Set figure size
plt.bar(products, sales, color=colors)

# Add title and labels
plt.title('Sales Data for Different Products', fontsize=14)
plt.xlabel('Products', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)

# Display grid lines on y-axis for better readability
plt.grid(axis='y', linestyle='--')

# Show the plot
plt.show()

#task8

# Time periods
time_periods = ['T1', 'T2', 'T3', 'T4']

# Sample data for each category
category_A = [5, 7, 6, 8]
category_B = [3, 4, 5, 6]
category_C = [2, 3, 4, 3]

# Bar width
bar_width = 0.6

# Create stacked bars
plt.figure(figsize=(8, 6))  # Set figure size
plt.bar(time_periods, category_A, color='blue', label='Category A')
plt.bar(time_periods, category_B, color='green', label='Category B', bottom=np.array(category_A))
plt.bar(time_periods, category_C, color='red', label='Category C', bottom=np.array(category_A) + np.array(category_B))

# Add title and labels
plt.title('Stacked Bar Chart of Category Contributions Over Time', fontsize=14)
plt.xlabel('Time Periods', fontsize=12)
plt.ylabel('Values', fontsize=12)

# Add a legend
plt.legend()

# Show the plot
plt.show()
