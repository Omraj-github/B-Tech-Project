import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Create a plot
plt.plot(x, y1, label='Line 1')  # Add a label for the first line
plt.plot(x, y2, label='Line 2')  # Add a label for the second line

# Add a legend
plt.legend()

# Customize the legend
# plt.legend(loc='upper right')  # You can specify the location of the legend

# Set labels for the x and y axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set the title of the plot
plt.title('Sample Plot with Legends')

# Display the plot
plt.show()
