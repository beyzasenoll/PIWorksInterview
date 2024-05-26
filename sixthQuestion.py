import pandas as pd

file_path = '/Users/beyzasenol/Desktop/country_vaccination_stats.csv'
df = pd.read_csv(file_path)

median_vaccinations = df.groupby('country')['daily_vaccinations'].median()

top_3_countries = median_vaccinations.sort_values(ascending=False).head(3)

print(top_3_countries)
