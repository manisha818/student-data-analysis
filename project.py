import pandas as pd
import matplotlib.pyplot as plt

# Load file (make sure file is in same folder)
try:
    df = pd.read_excel("input.xlsx")
except Exception as e:
    print("Error loading file:", e)
    exit()

# Show columns (to avoid column name error)
print("Columns in file:", df.columns)

# Clean data
df = df.drop_duplicates()
df = df.dropna()

# Check if Marks column exists
if "Marks" not in df.columns:
    print("Error: 'Marks' column not found. Check column name.")
    exit()

# Convert Marks to numeric
df["Marks"] = pd.to_numeric(df["Marks"], errors='coerce')

# Remove invalid rows again
df = df.dropna()

# Save cleaned file
df.to_excel("cleaned_output.xlsx", index=False)

# Analysis
print("Average Marks:", df["Marks"].mean())

top_student = df.sort_values(by="Marks", ascending=False).head(1)
print("Top Student:\n", top_student)

# Graph
df["Marks"].hist()
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.savefig("graph.png")
plt.show()