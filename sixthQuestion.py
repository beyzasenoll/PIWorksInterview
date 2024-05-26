import pandas as pd

# File paths
input_file_path = '/Users/beyzasenol/Desktop/country_vaccination_stats.csv'
output_file_path = '/Users/beyzasenol/Desktop/imputed_vaccinations.csv'

def load_data(file_path):
    df = pd.read_csv(file_path, delimiter=';', on_bad_lines='skip')
    return df

df = load_data(input_file_path)

df['daily_vaccinations'] = pd.to_numeric(df['daily_vaccinations'], errors='coerce')

df['daily_vaccinations'] = df.groupby('country')['daily_vaccinations'].transform(
    lambda x: x.fillna(x.min() if not pd.isnull(x.min()) else 0)
)

df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)

df.to_csv(output_file_path, index=False)

median_vaccinations = df.groupby('country')['daily_vaccinations'].median()

top_3_countries = median_vaccinations.nlargest(3)

print("Top-3 countries with the highest median daily vaccination numbers:")
print(top_3_countries)
