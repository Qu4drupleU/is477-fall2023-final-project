import pandas as pd
from ydata_profiling import ProfileReport

# Load the dataset
df = pd.read_csv('data/winequality-red.csv', delimiter=';')

# Generate the profiling report using ydata-profiling
profile = ProfileReport(df, title="Wine Quality Profiling Report")

# Save the report to an HTML file
profile.to_file("profiling/report.html")