import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load patient data
patient_df = pd.read_csv("../data/PatientData.csv")

# seaborn style
sns.set(style="whitegrid")

# histogram plots for sugar readings
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sugar_columns = ['HbA1c', 'FBS', 'RBS']

for i, col in enumerate(sugar_columns):
    sns.histplot(patient_df[col], bins=20, kde=True, ax=axes[i], color='skyblue')
    axes[i].set_title(f'{col} Distribution')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Frequency")

plt.tight_layout()
plt.show()

# Load food data
food_df = pd.read_csv("../data/FoodData.csv")

# Scatter plot of GI vs. Fiber
plt.figure(figsize=(8, 6))
sns.scatterplot(data=food_df, x='Glycemic Index', y='Fiber Content', hue='Suitable for Diabetes', palette='coolwarm')
plt.title("Glycemic Index vs Fiber Content")
plt.xlabel("Glycemic Index")
plt.ylabel("Fiber Content")
plt.legend(title="Suitable for Diabetes")
plt.grid(True)
plt.show()

