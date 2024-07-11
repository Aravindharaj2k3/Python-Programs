import pandas as pd

# Specify the path to your Excel file
file_path = 'D:\Data Engineering\HealthcareDataset1.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())
