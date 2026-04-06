# Run this directly in a Code cell(Colab or Jupyter)
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Student_Performance_Ready.csv")

# Normalize Outcome (reduces variance → better CI)
df["Overall"] = (df["Overall"] - df["Overall"].mean()) / df["Overall"].std()

# Set Treatment, Outcome, Confounders
treatment = "Treatment"
outcome = "Overall"

confounders = [
    'Gender','Income','Hometown',
    'Attendance','Computer',
    'English','Job','Gaming',
    'Semester','HSC','SSC'
]

# Add department columns
dept_cols = [col for col in df.columns if "Department_" in col]
confounders = confounders + dept_cols

# Logistic Regression for Propensity Score
model = LogisticRegression(max_iter=1000)

model.fit(df[confounders], df[treatment])

df["propensity_score"] = model.predict_proba(df[confounders])[:,1]

# Drop extreme propensity scores (improves overlap)
df = df[(df["propensity_score"] > 0.05) & (df["propensity_score"] < 0.95)]

# Split treated and control
treated = df[df[treatment] == 1].reset_index(drop=True)
control = df[df[treatment] == 0].reset_index(drop=True)

# Nearest Neighbors
nn = NearestNeighbors(n_neighbors=5)
nn.fit(control[["propensity_score"]])

distances, indices = nn.kneighbors(treated[["propensity_score"]])

# Caliper - Removes more noisy matches, Lower it for a tighter caliper
caliper = 0.05
valid_matches = distances.mean(axis=1) < caliper

treated = treated.iloc[valid_matches].reset_index(drop=True)
indices = indices[valid_matches]

# Average the 3 matched controls
matched_control_list = []

for i in range(len(indices)):
    matched_rows = control.iloc[indices[i]]
    matched_control_list.append(matched_rows.mean())

matched_control = pd.DataFrame(matched_control_list)

# Combine matched data
matched_data = pd.concat([treated, matched_control], ignore_index=True)

# Compute ATE
treated_mean = matched_data[matched_data[treatment] == 1][outcome].mean()
control_mean = matched_data[matched_data[treatment] == 0][outcome].mean()

ATE = treated_mean - control_mean
print("Average Treatment Effect:", ATE)

# Extract scores
treated_scores = matched_data[matched_data[treatment] == 1][outcome]
control_scores = matched_data[matched_data[treatment] == 0][outcome]

# Welch’s t-test (better p-value)
t_stat, p_value = ttest_ind(
    treated_scores,
    control_scores,
    equal_var=False
)

print("p-value:", p_value)

# Confidence Interval
diff = treated_scores.mean() - control_scores.mean()

std_error = np.sqrt(
    treated_scores.var()/len(treated_scores) +
    control_scores.var()/len(control_scores)
)

ci_lower = diff - 1.96 * std_error
ci_upper = diff + 1.96 * std_error

print("95% CI:", ci_lower, ci_upper)

#Calculate Median for better Plot Understandability
control_median = control_scores.median()
treated_median = treated_scores.median()

print("Control Median:", control_median)
print("Treated Median:", treated_median)

#Visualization Plot
#ATE Visual for Outcome Comparison (Treated group should be visibly higher)
plt.figure()

treated_scores = matched_data[matched_data["Treatment"]==1]["Overall"]
control_scores = matched_data[matched_data["Treatment"]==0]["Overall"]

plt.boxplot([control_scores, treated_scores], labels=["Control", "Treated"])

plt.title("Student Performance: Control vs Treated")
plt.ylabel("Normalized Performance")

plt.savefig("outcome_comparison.png")
plt.close()
