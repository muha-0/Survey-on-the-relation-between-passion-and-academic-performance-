import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

# Load the survey data
file_path = 'Survey on the relation between passion and academic performance .csv'
survey_data = pd.read_csv(file_path)

# Calculate the passion score
survey_data['Passion Score'] = survey_data['Did you want to pursue that major?'].map({'Yes': 2, 'No': 0}) + \
                               survey_data['Do you consider pursuing a master\'s degree?'].map({'Yes': 2, 'No': 0}) + \
                               survey_data['Do you believe your chosen major aligns with your interests and career goals?'].map({'Yes': 2, 'No': 0}) + \
                               survey_data['How much do you engage in activities related to your major outside of your coursework?'].map({'Frequently': 2, 'Occasionally': 1, 'Rarely': 0, 'Never': -1})

# Calculate mean
mean_cgpa = survey_data['What is your CGPA?'].mean()
mean_passion_score = survey_data['Passion Score'].mean()

# Calculate median
median_cgpa = survey_data['What is your CGPA?'].median()
median_passion_score = survey_data['Passion Score'].median()

# Calculate mode
try:
    mode_cgpa = statistics.mode(survey_data['What is your CGPA?'])
except statistics.StatisticsError:
    mode_cgpa = None

try:
    mode_passion_score = statistics.mode(survey_data['Passion Score'])
except statistics.StatisticsError:
    mode_passion_score = None

print("Mean CGPA:", mean_cgpa)
print("Median CGPA:", median_cgpa)
print("Mode CGPA:", mode_cgpa)
print("Mean Passion Score:", mean_passion_score)
print("Median Passion Score:", median_passion_score)
print("Mode Passion Score:", mode_passion_score)

# Scatter plot for CGPA and Passion Score
correlation = survey_data['What is your CGPA?'].corr(survey_data['Passion Score'])
plt.figure(figsize=(10, 6))
sns.regplot(x='What is your CGPA?', y='Passion Score', data=survey_data, scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'color': 'red'})
plt.title(f'CGPA vs. Passion Score (correlation:{correlation:.2f})')
plt.xlabel('CGPA')
plt.ylabel('Passion Score')
plt.grid(True)
plt.show()

print(correlation)

# Create a box plot for CGPA and Passion Score to show if there are any outliers
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.boxplot(survey_data['What is your CGPA?'])
plt.title('CGPA Box Plot')

plt.subplot(1, 2, 2)
plt.boxplot(survey_data['Passion Score'])
plt.title('Passion Score Box Plot')

plt.tight_layout()
plt.show()

# Create a box plot comparing CGPA between different levels of engagement
plt.figure(figsize=(10, 6))
sns.boxplot(x='How much do you engage in activities related to your major outside of your coursework?', y='What is your CGPA?', data=survey_data)
plt.title('CGPA vs. Engagement in Activities Related to Major')
plt.xlabel('Engagement Level')
plt.ylabel('CGPA')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Never', 'Rarely', 'Occasionally', 'Frequently'])
plt.grid(True)
plt.show()

# Set up figure and axes
fig, axs = plt.subplots(2, 2, figsize=(12, 12))

# Pie chart for "Did you want to pursue that major?"
axs[0, 0].pie(survey_data['Did you want to pursue that major?'].value_counts(), labels=['Yes', 'No'], autopct='%1.1f%%', startangle=90, colors=['#1f77b4', 'red'], textprops = {'fontsize':14})
axs[0, 0].set_title('Did you want to pursue that major?')

# Pie chart for "If no why did you choose it?"
filtered_data = survey_data[survey_data['If your answer was no, why did you choose it?'] != "My answer was yes"]
axs[0, 1].pie(filtered_data['If your answer was no, why did you choose it?'].value_counts(), labels=filtered_data['If your answer was no, why did you choose it?'].value_counts().index, autopct='%1.1f%%', startangle=90, textprops = {'fontsize':14})
axs[0, 1].set_title('If no why did you choose it?')

# Pie chart for "Do you consider pursuing a master's degree?"
axs[1, 0].pie(survey_data['Do you consider pursuing a master\'s degree?'].value_counts(), labels=['Yes', 'No'], autopct='%1.1f%%', startangle=90, colors=['#1f77b4', 'red'], textprops = {'fontsize':14})
axs[1, 0].set_title('Do you consider pursuing a master\'s degree?')

# Pie chart for "Do you believe this major aligns with your goals and interests?"
axs[1, 1].pie(survey_data['Do you believe your chosen major aligns with your interests and career goals?'].value_counts(), labels=['Yes', 'No'], autopct='%1.1f%%', startangle=90, colors=['#1f77b4', 'red'], textprops = {'fontsize':14})
axs[1, 1].set_title('Do you believe your major aligns with your interests/goals?')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

# Plot scatter plots with regression lines for each major
g = sns.FacetGrid(survey_data, col='What is your major?', col_wrap=3, height=4)
g.map_dataframe(sns.regplot, x='What is your CGPA?', y='Passion Score', scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'color': 'red'})

# Calculate and add correlation to the title
for ax, title in zip(g.axes.flat, survey_data['What is your major?'].unique()):
    subset = survey_data[survey_data['What is your major?'] == title]
    correlation = subset['What is your CGPA?'].corr(subset['Passion Score'])
    ax.set_title(f"{title}\nCorrelation: {correlation:.2f}")

plt.tight_layout()
plt.show()
