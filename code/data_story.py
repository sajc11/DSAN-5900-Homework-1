import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px

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
sns.countplot(x=df['Decision'], palette="Set2")
plt.title("Overview of Admission Decisions")
plt.xlabel("Decision")
plt.ylabel("Count")
plt.savefig(os.path.join(plots_path, "admission_overview.png"))
plt.close()

# **2. Average GPA by Admission Decision (Bar Chart)**
plt.figure(figsize=(8, 5))
gpa_avg = df.groupby("Decision")["GPA"].mean().reset_index()
sns.barplot(x="Decision", y="GPA", data=gpa_avg, palette="Blues_r")
plt.title("Average GPA by Admission Decision")
plt.xlabel("Admission Decision")
plt.ylabel("Average GPA")
plt.ylim(df["GPA"].min() - 0.1, df["GPA"].max() + 0.1)
plt.savefig(os.path.join(plots_path, "gpa_vs_decision.png"))
plt.close()

# **3. Average Test Score by Admission Decision (Bar Chart)**
plt.figure(figsize=(8, 5))
testscore_avg = df.groupby("Decision")["TestScore"].mean().reset_index()
sns.barplot(x="Decision", y="TestScore", data=testscore_avg, palette="Greens_r")
plt.title("Average Test Score by Admission Decision")
plt.xlabel("Admission Decision")
plt.ylabel("Average Test Score")
plt.ylim(df["TestScore"].min() - 5, df["TestScore"].max() + 5)
plt.savefig(os.path.join(plots_path, "test_score_vs_decision.png"))
plt.close()

# **4. Work Experience vs. Admission**
plt.figure(figsize=(8, 5))
sns.barplot(x=df['Decision'], y=df['WorkExp'], ci=None, palette="Oranges_r")
plt.title("Average Work Experience by Admission Decision")
plt.xlabel("Admission Decision")
plt.ylabel("Average Work Experience (Years)")
plt.savefig(os.path.join(plots_path, "work_exp_vs_admission.png"))
plt.close()

# **5. Volunteer Experience Impact (Heatmap)**
plt.figure(figsize=(8, 5))
volunteer_matrix = df.pivot_table(index='VolunteerLevel', columns='Decision', aggfunc='size', fill_value=0)
sns.heatmap(volunteer_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Volunteer Level and Admission Decision (Matrix View)")
plt.xlabel("Admission Decision")
plt.ylabel("Volunteer Level")
plt.savefig(os.path.join(plots_path, "volunteer_vs_admission_matrix.png"))
plt.close()

# **Interactive Plotly Visualizations**

# **1. Admissions Overview**
fig1 = px.bar(df['Decision'].value_counts().reset_index(), x='index', y='Decision', 
              labels={'index': 'Admission Decision', 'Decision': 'Count'},
              title="Overview of Admission Decisions")
fig1.write_html(os.path.join(plots_path, "admission_overview.html"))

# **2. Average GPA by Admission Decision (Interactive)**
fig2 = px.bar(gpa_avg, x="Decision", y="GPA", color="Decision",
              title="Average GPA by Admission Decision",
              labels={'GPA': 'Average GPA', 'Decision': 'Admission Decision'})
fig2.write_html(os.path.join(plots_path, "gpa_vs_decision.html"))

# **3. Average Test Score by Admission Decision (Interactive)**
fig3 = px.bar(testscore_avg, x="Decision", y="TestScore", color="Decision",
              title="Average Test Score by Admission Decision",
              labels={'TestScore': 'Average Test Score', 'Decision': 'Admission Decision'})
fig3.write_html(os.path.join(plots_path, "test_score_vs_decision.html"))

# **4. Work Experience vs. Admission (Interactive)**
fig4 = px.bar(df.groupby("Decision")["WorkExp"].mean().reset_index(), x="Decision", y="WorkExp",
              title="Average Work Experience by Admission Decision",
              labels={'WorkExp': 'Average Work Experience (Years)', 'Decision': 'Admission Decision'})
fig4.write_html(os.path.join(plots_path, "work_exp_vs_admission.html"))

# **5. Volunteer Experience Impact (Interactive Heatmap)**
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

# **6. Stacked Bar Chart: Volunteer Level vs. Admission Decision**
fig6 = px.bar(
    volunteer_pivot,
    x=volunteer_pivot.index,  # Volunteer Level on X-axis
    y=volunteer_pivot.columns,  # Decision categories on Y-axis
    title="Volunteer Level and Admission Decision",
    labels={'value': 'Number of Students', 'VolunteerLevel': 'Volunteer Level'},
    barmode="stack"  # Stacking bars to show proportions
)
fig6.write_html(os.path.join(plots_path, "volunteer_vs_admission_stacked.html"))

### --- END: Data Story Conclusion --- ###

print("\n📢 **DATA STORY INSIGHTS** 📢\n")

print("🔹 **1. GPA Correlates with Admissions**")
print("   - Accepted students have higher average GPAs than declined students.")

print("\n🔹 **2. Test Scores Show a Pattern**")
print("   - Higher test scores are associated with admissions, but not as strongly as GPA.")

print("\n🔹 **3. Work Experience Gives a Small Advantage**")
print("   - More years of experience slightly increase acceptance rates.")

print("\n🔹 **4. Volunteer Experience Helps Too**")
print("   - Higher volunteer levels tend to correlate with admissions.")

print("\n**Final Takeaway: Strong Academics + Holistic Profile = Best Chance!**")
print("   - GPA + Test Scores + Work/Volunteer Experience = Strong Applicant.\n")