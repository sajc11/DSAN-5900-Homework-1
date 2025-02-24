import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
file_path = "../data/raw/SummerStudentAdmissions2.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
df.info(), df.head()

# Step 1: Fix 'Decision' Column
# Remove invalid value 'Banana' and replace NaN with a placeholder
df = df[df['Decision'] != 'Banana']
df['Decision'].fillna('Unknown', inplace=True)

# Step 2: Handle Missing Values
# Fill missing numerical values with the median 
numerical_cols = ['GPA', 'WorkExp', 'TestScore', 'Gender']
for col in numerical_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Step 3: Fix Gender Column
# Assuming 1.0 = Male, 0.0 = Female, and -1.0 is an error; replacing -1.0 with the mode 
df['Gender'].replace(-1.0, df['Gender'].mode()[0], inplace=True)

# Convert categorical columns to category type
df['Decision'] = df['Decision'].astype('category')
df['State'] = df['State'].astype('category')
df['Gender'] = df['Gender'].astype(int)  # Convert back to integer

# Display cleaned dataset
print(df)

# Display basic information about the dataset
df.info(), df.head()

# Save dataset inside data/clean folder
clean_data_path = "../data/clean/"
os.makedirs(clean_data_path, exist_ok=True)  # Ensure directory exists
df.to_csv(os.path.join(clean_data_path, "SummerStudentAdmissions_clean.csv"), index=False)

# Step 4: Exploratory Data Analysis (EDA)

# Set Seaborn style for better visuals
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Distribution of Admission Decisions
plt.figure()
sns.countplot(x=df['Decision'])
plt.title("Distribution of Admission Decisions")
plt.xlabel("Decision")
plt.ylabel("Count")
plt.show()

# GPA Distribution by Admission Decision
plt.figure()
sns.boxplot(x=df['Decision'], y=df['GPA'])
plt.title("GPA Distribution by Admission Decision")
plt.xlabel("Decision")
plt.ylabel("GPA")
plt.show()

# Test Score Distribution
plt.figure()
sns.histplot(df['TestScore'], bins=15, kde=True)
plt.title("Distribution of Test Scores")
plt.xlabel("Test Score")
plt.ylabel("Count")
plt.show()

# Work Experience vs. Admission
plt.figure()
sns.boxplot(x=df['Decision'], y=df['WorkExp'])
plt.title("Work Experience vs. Admission Decision")
plt.xlabel("Decision")
plt.ylabel("Work Experience (Years)")
plt.show()

# Volunteer Level and Admission
plt.figure()
sns.countplot(x=df['VolunteerLevel'], hue=df['Decision'])
plt.title("Volunteer Level and Admission Decision")
plt.xlabel("Volunteer Level")
plt.ylabel("Count")
plt.legend(title="Decision")
plt.show()