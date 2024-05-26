import pandas as pd

file_path ='/Users/beyzasenol/Desktop/imputed_vaccinations.csv'


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

df = load_data(file_path)

df['date'] = pd.to_datetime(df['date'])

specific_date_data = df[df['date'] == '2021-01-06']

total_vaccinations = specific_date_data['daily_vaccinations'].sum()


print(total_vaccinations)
