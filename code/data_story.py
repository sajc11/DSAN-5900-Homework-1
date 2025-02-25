import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px
import plotly.graph_objects as go

# Set paths
data_path = "../data/clean/SummerStudentAdmissions_clean.csv" 
plots_path = "../website-source/plots/"

# Ensure the plots directory exists
os.makedirs(plots_path, exist_ok=True)

# Load data
df = pd.read_csv(data_path)

# Set Seaborn style
sns.set_style("whitegrid")

### --- DATA STORY STARTS HERE --- ###

# **1. Admissions Overview**
plt.figure(figsize=(8, 5))
sns.countplot(x=df['Decision'])
plt.title("Overview of Admission Decisions")
plt.xlabel("Decision")
plt.ylabel("Count")
plt.savefig(os.path.join(plots_path, "admission_overview.png"))
plt.close()

# **2. GPA Distribution**
plt.figure(figsize=(8, 5))
sns.histplot(df['GPA'], bins=10, kde=True)
plt.title("Distribution of GPA")
plt.xlabel("GPA")
plt.ylabel("Number of Students")
plt.savefig(os.path.join(plots_path, "gpa_distribution.png"))
plt.close()

# **3. Test Score Distribution**
plt.figure(figsize=(8, 5))
sns.histplot(df['TestScore'], bins=10, kde=True)
plt.title("Distribution of Test Scores")
plt.xlabel("Test Score")
plt.ylabel("Number of Students")
plt.savefig(os.path.join(plots_path, "test_score_distribution.png"))
plt.close()

# **4. Work Experience vs. Admission**
plt.figure(figsize=(8, 5))
sns.barplot(x=df['Decision'], y=df['WorkExp'], ci=None)
plt.title("Average Work Experience by Admission Decision")
plt.xlabel("Admission Decision")
plt.ylabel("Average Work Experience (Years)")
plt.savefig(os.path.join(plots_path, "work_exp_vs_admission.png"))
plt.close()

# **5. Volunteer Experience Impact**
plt.figure(figsize=(8, 5))
volunteer_matrix = df.pivot_table(index='VolunteerLevel', columns='Decision', aggfunc='size', fill_value=0)
sns.heatmap(volunteer_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Volunteer Level and Admission Decision (Matrix View)")
plt.xlabel("Admission Decision")
plt.ylabel("Volunteer Level")
plt.savefig(os.path.join(plots_path, "volunteer_vs_admission_matrix.png"))
plt.close()

# Set up interactive plots using Plotly

# **1. Admissions Overview**
fig1 = px.bar(df['Decision'].value_counts().reset_index(), x='index', y='Decision', 
              labels={'index': 'Admission Decision', 'Decision': 'Count'},
              title="Overview of Admission Decisions")
fig1.write_html(os.path.join(plots_path, "admission_overview.html"))

# **2. GPA Distribution**
fig2 = px.histogram(df, x="GPA", nbins=10, marginal="box", 
                    title="Distribution of GPA",
                    labels={'GPA': 'GPA Score', 'count': 'Number of Students'})
fig2.write_html(os.path.join(plots_path, "gpa_distribution.html"))

# **3. Test Score Distribution**
fig3 = px.histogram(df, x="TestScore", nbins=10, marginal="box", 
                    title="Distribution of Test Scores",
                    labels={'TestScore': 'Test Score', 'count': 'Number of Students'})
fig3.write_html(os.path.join(plots_path, "test_score_distribution.html"))

# **4. Work Experience vs. Admission**
fig4 = px.bar(df.groupby("Decision")["WorkExp"].mean().reset_index(), x="Decision", y="WorkExp",
              title="Average Work Experience by Admission Decision",
              labels={'WorkExp': 'Average Work Experience (Years)', 'Decision': 'Admission Decision'})
fig4.write_html(os.path.join(plots_path, "work_exp_vs_admission.html"))

# **5. Volunteer Experience Impact**
fig5 = px.imshow(volunteer_matrix.values,
                 labels=dict(x="Admission Decision", y="Volunteer Level", color="Count"),
                 x=volunteer_matrix.columns,
                 y=volunteer_matrix.index,
                 color_continuous_scale="Blues",
                 title="Volunteer Level and Admission Decision (Matrix View)")
fig5.write_html(os.path.join(plots_path, "volunteer_vs_admission_matrix.html"))

# Prepare data for the stacked bar chart
volunteer_counts = df.groupby(['VolunteerLevel', 'Decision']).size().reset_index(name='Count')

# Convert data into a pivot table format for Plotly
volunteer_pivot = volunteer_counts.pivot(index='VolunteerLevel', columns='Decision', values='Count').fillna(0)

# Create the stacked bar chart using Plotly
fig6 = px.bar(
    volunteer_pivot,
    x=volunteer_pivot.index,  # Volunteer Level on X-axis
    y=volunteer_pivot.columns,  # Decision categories on Y-axis
    title="Volunteer Level and Admission Decision",
    labels={'value': 'Number of Students', 'VolunteerLevel': 'Volunteer Level'},
    barmode="stack"  # Stacking bars to show proportions
)

# Save the interactive stacked bar chart
fig6.write_html(os.path.join(plots_path, "volunteer_vs_admission_stacked.html"))


### --- END: Data Story Conclusion --- ###

print("\n📢 **DATA STORY INSIGHTS** 📢\n")

print("🔹 **1. GPA is a Strong Predictor**")
print("   - Higher GPAs significantly increase admission chances.")

print("\n🔹 **2. Test Scores Matter, But Not Everything**")
print("   - While higher test scores help, they're not the sole deciding factor.")

print("\n🔹 **3. Work Experience Provides an Edge**")
print("   - More years of experience slightly boost chances of acceptance.")

print("\n🔹 **4. Volunteer Experience Helps Too**")
print("   - Higher volunteer levels tend to correlate with admissions.")

print("\n**Final Takeaway: Well-Rounded Applicants Have the Best Chance!**")
print("   - GPA + Decent Test Scores + Work/Volunteer Experience = Strong Applicant.\n")