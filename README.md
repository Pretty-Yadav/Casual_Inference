# Student Performance Causal Inference

This project investigates whether increased study hours are associated with better student performance. It uses observational student data and propensity-score matching to compare students with similar observed characteristics.

## Problem

Students who study more may also differ from other students in ways that affect their performance. The analysis aims to estimate the average difference in performance between a higher-study-hours group and a lower-study-hours control group while accounting for available student characteristics.

## Dataset

The analysis uses `Student_Performance_Ready.csv`, which contains 493 student records. The dataset includes:

- `Treatment`: identifies the higher-study-hours and control groups
- `Overall`: the student performance outcome
- Student characteristics such as attendance, income, hometown, computer access, employment, gaming, semester, HSC, and SSC
- Department indicator columns

The data is observational, so the results should be interpreted with care. Matching can account only for differences that are measured in the dataset.

## Method

The workflow in `script.py` is:

1. Load the CSV data and standardize the `Overall` performance score.
2. Estimate each student's probability of being in the treated group with logistic regression.
3. Remove observations with extreme propensity scores to improve overlap between groups.
4. Match each treated student with five nearby control students using propensity scores and a 0.05 caliper.
5. Calculate the average treatment effect, Welch's t-test p-value, and a 95% confidence interval.
6. Create a control-versus-treated boxplot saved as `outcome_comparison.png`.

## Results

The recorded analysis produced the following results:

| Measure | Result |
| --- | ---: |
| Average treatment effect | `+0.130` standard deviations |
| p-value | `0.028` |
| 95% confidence interval | `[0.014, 0.246]` standard deviations |
| Control median | `0.530` |
| Treated median | `0.425` |

The matched treated group had a higher average standardized performance, and the confidence interval remained above zero. This provides evidence of a positive average relationship between higher study hours and performance in this dataset. The lower treated median and wider spread show that the improvement was not the same for every student.

## Running the analysis

Install the Python dependencies:

```bash
pip install pandas numpy scikit-learn scipy matplotlib
```

Run the script from the project root:

```bash
python script.py
```

The script prints the effect estimate, p-value, confidence interval, and medians. It also writes `outcome_comparison.png` to the project root.

The script was written to run in a Jupyter or Google Colab code cell. If using a notebook, place the notebook in the project root or update the CSV path as needed.

## Project files

```text
Student_Performance_Ready.csv   Analysis dataset
script.py                        Propensity-score matching analysis
output.txt                       Recorded analysis results and interpretation
technical_description.txt       Technical project description
non_technical_description.txt   Plain-language project description
docs/                            Static website explaining the analysis
```

The website can be opened from `docs/index.html` or published with GitHub Pages using the `docs/` folder as the site source. See `docs/README.md` for deployment details.

## Limitations

- This is observational data, not a randomized experiment.
- The analysis adjusts for measured characteristics only; unmeasured confounding may remain.
- A positive average effect does not mean that studying more improves performance for every student.
- The reported effect is in standardized performance units, not raw score points.
