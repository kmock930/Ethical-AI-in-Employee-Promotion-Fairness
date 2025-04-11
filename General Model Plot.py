import matplotlib.pyplot as plt

# General
# Metrics and their values
metrics = ['ACC', 'FPR', 'FNR']
male_values = [0.9190, 0.0300, 0.6115]
female_values = [0.9200, 0.0319, 0.6016]

# Create positions for each group of bars
x_positions = range(len(metrics))
bar_width = 0.4

# Plot side-by-side bars for each metric
male_bars = plt.bar([p - bar_width/2 for p in x_positions], male_values, width=bar_width, label='Male')
female_bars = plt.bar([p + bar_width/2 for p in x_positions], female_values, width=bar_width, label='Female')

# Add numbers on each bar
for bar in male_bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.4f}', ha='center', va='bottom')
for bar in female_bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.4f}', ha='center', va='bottom')

# Set up axis labels and legend
plt.xticks(x_positions, metrics)
plt.ylabel('Value')
plt.title('Comparison of Male vs. Female Performance Metrics')
plt.legend()

# Show the chart
plt.savefig('Model Comparison - General.png')