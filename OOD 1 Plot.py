import matplotlib.pyplot as plt

# OOD 1
# Metrics and their values
metrics = ['ACC', 'FPR', 'FNR']
male_values = [0.9108, 0.0388, 0.6149]
female_values = [0.9351, 0.0026, 0.7410]

# Create positions for each group of bars
x_positions = range(len(metrics))
bar_width = 0.4

# Plot side-by-side bars for each metric
male_bars = plt.bar([p - bar_width/2 for p in x_positions], male_values, width=bar_width, label='Male')
female_bars = plt.bar([p + bar_width/2 for p in x_positions], female_values, width=bar_width, label='Female')

# Add numbers to each bar
for bar in male_bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.4f}', ha='center', va='bottom')
for bar in female_bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.4f}', ha='center', va='bottom')

# Set up axis labels and legend
plt.xticks(x_positions, metrics)
plt.ylabel('Value')
plt.title('Out-of-Distribution: Male vs. Female Performance Metrics')
plt.legend()

# Show the chart
plt.savefig('Model Comparison - OOD 1.png')