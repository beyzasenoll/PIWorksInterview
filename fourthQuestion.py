import pandas as pd

file_path = '/Users/beyzasenol/Desktop/country_vaccination_stats.csv'


def load_data(file_path):
    df = pd.read_csv(file_path, delimiter=';', on_bad_lines='skip')
    return df


df = load_data(file_path)

print("Original Data")
print(df.head(30))

df['daily_vaccinations'] = pd.to_numeric(df['daily_vaccinations'], errors='coerce')

df['daily_vaccinations'] = df.groupby('country')['daily_vaccinations'].transform(
    lambda x: x.fillna(x.min() if not pd.isnull(x.min()) else 0)
)

df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)

print("\nDataFrame after imputation:")
print(df.head(30))

df.to_csv(df.to_csv(file_path, index=False))