import pandas as pd
import matplotlib.pyplot as plt

#Read marks from CSV
try:
    df = pd.read_csv('student_marks.csv')
except FileNotFoundError:
    print("Error: 'student_marks.csv' not found. Please create the file first.")
    exit()

#Calculate average, max, min per subject
subjects = ['Math', 'Science', 'English', 'History']
subject_stats = pd.DataFrame({
    'Average': df[subjects].mean(),
    'Max': df[subjects].max(),
    'Min': df[subjects].min()
})

print("--- Subject-wise Statistics ---")
print(subject_stats.round(2))
print("\n")

# Calculate Total marks for each student
df['Total'] = df[subjects].sum(axis=1)

# Bar Chart: Compare Students
# Sorting students by total marks for a cleaner ranking view
df_sorted = df.sort_values(by='Total', ascending=True)

plt.figure(figsize=(10, 12))
plt.barh(df_sorted['Name'], df_sorted['Total'], color='skyblue', edgecolor='navy')
plt.title('Student Comparison: Total Marks (Out of 400)', fontsize=14)
plt.xlabel('Total Score', fontsize=12)
plt.ylabel('Student Name', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('student_comparison_bar.png') # Saves the bar chart
plt.show()

# Histogram: Distribution of Scores
plt.figure(figsize=(10, 6))
plt.hist(df['Total'], bins=8, color='orange', edgecolor='black', alpha=0.7)
plt.title('Class Score Distribution (Histogram)', fontsize=14)
plt.xlabel('Total Marks Range', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('score_distribution_hist.png') # Saves the histogram
plt.show()