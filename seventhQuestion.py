import pandas as pd

# Correct file path
file_path ='/Users/beyzasenol/Desktop/imputed_vaccinations.csv'


# Function to load data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Load data
df = load_data(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter data for the specific date
specific_date_data = df[df['date'] == '2021-01-06']

# Calculate the total vaccinations done on 1/6/2021
total_vaccinations = specific_date_data['daily_vaccinations'].sum()

# Output the result

print(total_vaccinations)
