import matplotlib.pyplot as plt

# Metrics and values for Section 9.3 New Approach results
metrics = ['ACC', 'FPR', 'FNR']
male_values = [0.9238, 0.0214, 0.6470]
female_values = [0.9294, 0.0173, 0.6494]

# Define positions for the groups
x_positions = range(len(metrics))
bar_width = 0.4

# Plot side-by-side bars
male_bars = plt.bar([p - bar_width/2 for p in x_positions], male_values, width=bar_width, label='Male')
female_bars = plt.bar([p + bar_width/2 for p in x_positions], female_values, width=bar_width, label='Female')

# Add numbers to each bar
for bar in male_bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.4f}', ha='center', va='bottom', fontsize=8)
for bar in female_bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.4f}', ha='center', va='bottom', fontsize=8)

# Customize axes, title, legend
plt.xticks(x_positions, metrics)
plt.ylabel('Value')
plt.title('Cluster-based Out-of-Distribution: Male vs. Female Performance Metrics')
plt.legend()

# Display the chart
plt.savefig('Model Comparison - OOD 2.png')
