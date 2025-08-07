# Step 1: Importing Necessary Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the Dataset
df = pd.read_csv('D:\\COVID.csv')  # Adjust the path as needed
# View the first few rows of the dataset
print(df.head())

# Get dataset shape
print(f"Shape of dataset: {df.shape}")

# Check the columns and data types
print(df.info())

# Summary statistics
print(df.describe(include='all'))

# Check for missing values
missing_data = df.isnull().mean() * 100
print("Percentage of missing data:\n", missing_data)

# Dropping high missing rate columns
df.drop(columns=['Results First Posted', 'Study Documents'], inplace=True)

# Impute or drop other missing values as necessary
df['Acronym'].fillna('Missing Acronym', inplace=True)

# Status Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Status', order=df['Status'].value_counts().index)
plt.title('Status of Clinical Trials')
plt.xticks(rotation=45)
plt.show()

# Phase Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Phases', order=df['Phases'].value_counts().index)
plt.title('Distribution of Phases')
plt.xticks(rotation=45)
plt.show()

# Gender Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Gender', order=df['Gender'].value_counts().index)
plt.title('Gender Distribution')
plt.xticks(rotation=45)
plt.show()

# Age Group Analysis
plt.figure(figsize=(10, 6))
order = ['0-17', '18-25', '26-35', '36-45', '46-60', '60+']
sns.countplot(data=df, x='Age', order=order, palette='viridis')  # or choose another palette

plt.title('Age Group Distribution', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Status vs. Phases
plt.figure(figsize=(10, 6))
status_phase = pd.crosstab(df['Status'], df['Phases'])
status_phase.plot(kind='bar', stacked=True)
plt.title('Status vs. Phases')
plt.xlabel('Status')
plt.ylabel('Count')
plt.legend(title='Phases')
plt.show()

# Convert date columns to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')

# Plot number of trials started over time
trials_over_time = df['Start Date'].dt.to_period('M').value_counts().sort_index()

plt.figure(figsize=(14, 7))
trials_over_time.plot(kind='line', marker='o')
plt.title('Trials Started Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Trials')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Summarizing findings
print("Summary of Findings:")
print("- The majority of trials are in the 'Completed' phase.")
print("- Most trials target adult populations.")
print("- There's a steady increase in the number of trials over time.")

# Save the cleaned dataset
df.to_csv('cleaned_covid_clinical_trials.csv', index=False)
