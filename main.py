import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data.csv")

# Print table
print("\n--- Student Performance Table ---\n")
print(df)

# Calculate Total & Average
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

print("\n--- With Total & Average ---\n")
print(df)

# --- Visualization 1: Bar Chart (Student Wise Total Marks)
plt.figure(figsize=(8,5))
sns.barplot(x=df["Name"], y=df["Total"])
plt.title("Total Marks of Each Student")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.show()

# --- Visualization 2: Subject Wise Comparison
df_plot = df.melt(id_vars="Name", value_vars=["Math", "Science", "English"], 
                  var_name="Subject", value_name="Marks")

plt.figure(figsize=(8,5))
sns.lineplot(data=df_plot, x="Name", y="Marks", hue="Subject", marker="o")
plt.title("Subject-wise Student Comparison")
plt.show()

# --- Visualization 3: Heatmap for Subject Correlation
plt.figure(figsize=(6,4))
sns.heatmap(df[["Math","Science","English"]].corr(), annot=True, cmap="coolwarm")
plt.title("Subject Correlation Heatmap")
plt.show()
