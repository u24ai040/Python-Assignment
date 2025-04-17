#QUESTION 5

import pandas as pd

n = int(input("Enter number of concert records: "))
records = []

for i in range(n):
    print(f"\nEnter details for concert {i+1}:")
    date = input("Date (YYYY-MM-DD): ")
    artist = input("Artist name: ")
    venue = input("Venue name: ")
    records.append({'date': date, 'artist': artist, 'venue': venue})

df = pd.DataFrame(records)
df['year'] = ''
df['month'] = ''

for index in range(len(df)):
    date = str(df.loc[index, 'date'])
    i = 0
    year = ''
    while date[i] != '-':
        year += date[i]
        i += 1
    i += 1

    month = ''
    while date[i] != '-':
        month += date[i]
        i += 1

    df.loc[index, 'year'] = year
    df.loc[index, 'month'] = month

df['year_month'] = df['year'] + '-' + df['month']


all_months = sorted(df['year_month'].unique())
all_artists = df['artist'].unique()
all_venues = df['venue'].unique()

data = {}

for ym in all_months:
    row = {}
    df_month = df[df['year_month'] == ym]
    for artist in all_artists:
        for venue in all_venues:
            count = len(df_month[(df_month['artist'] == artist) & (df_month['venue'] == venue)])
            row[(artist, venue)] = count
    data[ym] = row


result = pd.DataFrame.from_dict(data, orient='index')
result.index.name = 'year_month'
result = result.sort_index()


result.columns = [f"({artist},{venue})" for artist, venue in result.columns]


print("\nConcert count table \n")
print(result)