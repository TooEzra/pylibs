import pandas as pd  # We give the elder a short, respectful nickname 'pd'

# The scribe creates a table from a dictionary
data = {'Name': ['Lebo', 'Thando', 'Sipho'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Display the beautiful table
print(df)

# Calculate the average age of the village
print(f"\nThe average age is: {df['Age'].mean()} winters")

# Add a new column for occupation
df['Occupation'] = ['Farmer', 'Weaver', 'Hunter']
print("\nUpdated Table with Occupation:")
print(df)

#filter vilagers older than 28
Adults = df[df['Age'] > 28]
print("\nVillage Adults:")
print(Adults)

#sort villagers by age
Sorted_by_Age = df.sort_values(by='Age')
print("\nVillagers sorted by Age:")
print(Sorted_by_Age)

#save the table to a CSV file
df.to_csv('village_data.csv', index=False)
print("\nThe village data has been saved to 'village_data.csv'")
