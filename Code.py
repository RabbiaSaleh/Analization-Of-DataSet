import pandas as pd
import matplotlib.pyplot as plt

# Set options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# Read the CSV file into a DataFrame
file_path = r'C:/Users/Me/Desktop/data.csv' # Replace 'your_filename' with theactual filename
data = pd.read_csv(file_path)
# Display the entire DataFrame
data
# Create a dictionary to hold the data
data = {
"Year": [2012] * 10,
"Offence": ["Murder", "Attempt to Murder", "Kidnapping /Abduction", "Dacoity", "Robbery",
"Burglary", "Cattle Theft", "Other Theft", "Others", "TOTAL RECORDED CRIME"],
"Punjab": [6128, 7641, 15699, 2715, 12181, 14740, 8115, 34719, 292665, 394603],
"Sindh": [3726, 3732, 3077, 1341, 4320, 1680, 630, 2976, 57206, 78688],
"KP": [2958, 2892, 1052, 60, 134, 500, 118, 717, 139344, 147775],
"Balochistan": [711, 583, 386, 98, 160, 117, 77, 332, 5745, 8209],
"Islamabad": [120, 146, 70, 22, 177, 245, 43, 585, 5699, 7107],
"Railways": [6, 9, 6, 1, 5, 0, 0, 560, 1528, 2115],
"G.B": [102, 163, 32, 8, 26, 101, 23, 71, 1033, 1559],
"AJK": [95, 172, 288, 12, 78, 255, 40, 142, 4509, 5591],
"Pakistan": [13846, 15338, 20610, 4257, 17081, 17638, 9046, 40102, 507729, 645647]
}
# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
# Display the DataFrame
print(df)
# Read the CSV file into a DataFrame

file_path = r'C:/Users/Me/Desktop/data.csv' # Replace 'your_filename' with theactual filename
data = pd.read_csv(file_path)
# Group data by Year and City, then find the offense with the highest rate for each group
grouped_data = data.groupby(['Year', 'Offence']).sum().reset_index()
# Find the offense with the highest rate in each city for each year
highest_offenses = grouped_data.groupby(['Year', 'Offence']).max().reset_index()
# Display the highest offense rate in different cities with respect to the years
for year in highest_offenses['Year'].unique():
            year_data = highest_offenses[highest_offenses['Year'] == year]
            highest_offense = year_data.loc[year_data['Pakistan'].idxmax()] # Offense with highest rate
print(f"Year: {year}, Highest Offense: {highest_offense['Offence']}, Rate:{highest_offense['Pakistan']}")
# Read the CSV file into a DataFrame
file_path = r'C:/Users/Me/Desktop/data.csv' # Replace 'your_filename' with theactual filename
data = pd.read_csv(file_path)
# Filter for the desired offense types
offense_types = ["Murder", "Attempt to Murder", "Kidnapping /Abduction", "Dacoity", "Robbery",

"Burglary", "Cattle Theft", "Other Theft", "Others"]

# Group data by Year and Offence, then find the offense with the highest rate for each group
grouped_data = data.groupby(['Year', 'Offence']).sum().reset_index()
# Filter for the desired offense types
filtered_data = grouped_data[grouped_data['Offence'].isin(offense_types)]
# Find the offense with the highest rate in each city and region for all years
highest_offenses_all_years = filtered_data.groupby(['Offence']).max().reset_index()
# Display the highest offense rate for each offense type across different cities and regions
for offense in offense_types:
    offense_data = highest_offenses_all_years[highest_offenses_all_years['Offence'] == offense]
    highest_offense = offense_data.loc[offense_data['Pakistan'].idxmax()] # Offense with highestrate
print(f"Offence: {offense}")
for region in ["Punjab", "Sindh", "KP", "Balochistan", "Islamabad", "Railways", "G.B", "AJK"]:
    print(f" {region}: {highest_offense[region]}")
# Load the dataset
dataset_path = r'C:/Users/Me/Desktop/data.csv'
data = pd.read_csv(dataset_path)
# Select the offense type for analysis (e.g., Murder)
selected_offense = "Murder"
# Filter the data for the selected offense
selected_offense_data = data[data['Offence'] == selected_offense]
# Create a line plot to compare the selected offense across regions
plt.figure(figsize=(12, 8))
selected_offense_data.set_index('Year')[['Punjab', 'Sindh', 'KP', 'Balochistan', 'Islamabad',
'Railways', 'G.B', 'AJK']].plot(marker='o', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Crime Count')
plt.title(f'{selected_offense} Comparison Across Regions Over the Years')
plt.legend(title='Region')
plt.grid(True)
plt.tight_layout()
plt.show()
# Load the dataset
dataset_path = r'C:/Users/Me/Desktop/data.csv'
data = pd.read_csv(dataset_path)
# Select the offense type for analysis (e.g., Murder)
selected_offense = "Murder"
# Filter the data for the selected offense

selected_offense_data = data[data['Offence'] == selected_offense]
# Create a bar plot to visualize the regional distribution of the selected offense
plt.figure(figsize=(10, 6))
selected_offense_data.set_index('Year')[['Punjab', 'Sindh', 'KP', 'Balochistan', 'Islamabad',
'Railways', 'G.B', 'AJK']].plot(kind='bar', stacked=True)
plt.xlabel('Year')
plt.ylabel('Crime Count')
plt.title(f'Regional Distribution of {selected_offense} Over the Years')
plt.xticks(rotation=45)
plt.legend(title='Region')
plt.tight_layout()
plt.show()
# Load the dataset
dataset_path = r'C:/Users/Me/Desktop/data.csv'
data = pd.read_csv(dataset_path)
# Select the offense type for analysis (e.g., "Murder")
selected_offense = "Murder"
# Filter the data for the selected offense
selected_offense_data = data[data['Offence'] == selected_offense]
# Create line plots to visualize the trend of the selected offense over the years for differentregions
regions = ["Punjab", "Sindh", "KP", "Balochistan", "Islamabad", "Railways", "G.B", "AJK"]
plt.figure(figsize=(12, 8))
for region in regions:
    region_data = selected_offense_data[['Year', region]]
plt.plot(region_data['Year'], region_data[region], label=region)
plt.xlabel('Year')
plt.ylabel('Crime Count')
plt.title(f'Trend of {selected_offense} Over the Years by Region')

plt.legend()
plt.grid(True)
plt.show()
data = pd.read_csv(dataset_path)
# Group data by Year and sum up the total recorded crimes
yearly_total_crime = data.groupby('Year')['Pakistan'].sum()
# Create a line plot to visualize the yearly total crime trend
plt.figure(figsize=(10, 6))
plt.plot(yearly_total_crime.index, yearly_total_crime.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Total Recorded Crime')
plt.title('Yearly Total Recorded Crime Trend')
plt.grid(True)
plt.show()
data = pd.read_csv(dataset_path)
# Calculate the total crime count for each offense type
offense_type_counts = data.groupby('Offence')['Pakistan'].sum()
# Create a bar plot to visualize the distribution of offense types
plt.figure(figsize=(10, 6))
offense_type_counts.sort_values().plot(kind='barh')
plt.xlabel('Total Crime Count')
plt.ylabel('Offense Type')
plt.title('Distribution of Offense Types')

plt.grid(True)
plt.show()
data = pd.read_csv(dataset_path)
# Filter out the 'TOTAL RECORDED CRIME' rows
offense_data = data[data['Offence'] != 'TOTAL RECORDED CRIME']
# Pivot the data to get offense type composition for each year
offense_composition = offense_data.pivot_table(index='Year', columns='Offence',
values='Pakistan', aggfunc='sum')
# Create a stacked bar plot to visualize the yearly offense composition
plt.figure(figsize=(12, 8))
offense_composition.plot(kind='bar', stacked=True)
plt.xlabel('Year')
plt.ylabel('Total Crime Count')
plt.title('Yearly Offense Type Composition')
plt.legend(title='Offense Type')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
data = pd.read_csv(dataset_path)
# Filter out the 'TOTAL RECORDED CRIME' rows
offense_data = data[data['Offence'] != 'TOTAL RECORDED CRIME']

# Group data by Offence and Year and calculate the total crime count
offense_type_counts = offense_data.groupby(['Offence', 'Year'])['Pakistan'].sum().unstack()
# Create a line plot to compare offense types over the years with a larger figure size
plt.figure(figsize=(20, 12)) # Adjust the figsize to your desired size
offense_type_counts.plot(marker='o', linewidth=1)
plt.xlabel('Year')
plt.ylabel('Total Crime Count')
plt.title('Offense Type Comparison Over the Years')
plt.legend(title='Offense Type')
plt.grid(True)
plt.show()













