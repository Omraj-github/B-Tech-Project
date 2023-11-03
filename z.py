import matplotlib.pyplot as plt

# Set global configuration options
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'serif'

# Create a plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.title('Customized Plot')

# Show the plot
plt.show()
