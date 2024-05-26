import sqlite3
import pandas as pd
import re

conn = sqlite3.connect('device-url.db')

query = "SELECT Device_Type, Stats_Access_Link FROM device"
df = pd.read_sql_query(query, conn)


def extract_url(link):
    match = re.search(r'<url>https?://([a-zA-Z0-9_.]+)</url>', link)
    if match:
        return match.group(1)
    return None


df['Pure_URL'] = df['Stats_Access_Link'].apply(extract_url)

print(df)

conn.close()
