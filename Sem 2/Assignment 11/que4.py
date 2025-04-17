#QUESTION 4

import pandas as pd

data = []
print("Please enter the schedule for 10 days.")
print("Please answer in yes or no.")
for i in range(10):

    print("\nDay ", i + 1)
    john = input("  Is John visiting? (yes/no): ").strip().lower() == 'yes'
    judy = input("  Is Judy visiting? (yes/no): ").strip().lower() == 'yes'
    data.append({'John': john, 'Judy': judy})

df = pd.DataFrame(data)

df['party'] = df['John'] & df['Judy']


days_til_party = [0] * 10

for i in range(10):
    if df.loc[i, 'party']:
        days_til_party[i] = 0
    else:
        found = False
        for j in range(i + 1, 10):
            if df.loc[j, 'party']:
                days_til_party[i] = j - i
                found = True
                break
        if not found:
            days_til_party[i] = None  

df['days_til_party'] = days_til_party


print("\nSchedule with days_til_party:\n")
print(df[['John', 'Judy', 'days_til_party']])
