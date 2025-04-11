import matplotlib.pyplot as plt

# K-Means Clustering
# Metrics and their values
metrics = ['ACC', 'FPR', 'FNR']
male_values = [0.9264, 0.0214, 0.6166]
female_values = [0.9250, 0.0224, 0.6454]

# Create positions for each group of bars
x_positions = range(len(metrics))
bar_width = 0.4

# Plot side-by-side bars for each metric
male_bars = plt.bar([p - bar_width/2 for p in x_positions], male_values, width=bar_width, label='Male')
female_bars = plt.bar([p + bar_width/2 for p in x_positions], female_values, width=bar_width, label='Female')

# Add numbers to each bar
for bar in male_bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.4f}', ha='center', va='bottom', fontsize=8)

for bar in female_bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.4f}', ha='center', va='bottom', fontsize=8)

# Set up axis labels and legend
plt.xticks(x_positions, metrics)
plt.ylabel('Value')
plt.title('K-Means Clustering: Male vs. Female Performance Metrics')
plt.legend()

# Show the chart
plt.savefig('Model Comparison - KMeans Clustering.png')