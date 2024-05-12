import pandas as pd

# Load the dataset
data = pd.read_excel("C:/Users/Tario/Desktop/UNIC/SM5/COMP-340-1 Big Data/HW6/Real_Estate_HW6/Real_Estate_Sales_2001-2020_GL.xlsx")

columns_to_drop = ["Non Use Code", "Assessor Remarks", "OPM remarks", "Date Recorded"]
data.drop(columns=columns_to_drop, inplace=True)
print("Count of rows after dropping columns:", len(data))

# Splitting the dataframe based on the 'Location' column
data_with_location = data[data['Location'].notna()]
data_without_location = data[data['Location'].isna()]

print("Count of rows in dataframe with Location:", len(data_with_location))
print("Count of rows in dataframe without Location:", len(data_without_location))

# Drop N/A values
data_with_location = data_with_location.dropna()

# Show row count after dropping N/A values
print("Count of rows in dataframe with Location after dropping N/A values:", len(data_with_location))
print("Count of rows in dataframe without Location after dropping N/A values:", len(data_without_location))

#Count of rows after dropping columns: 997213
#Count of rows in dataframe with Location: 197697
#Count of rows in dataframe without Location: 799516
#Count of rows in dataframe with Location after dropping N/A values: 123755
#Count of rows in dataframe without Location after dropping N/A values: 799516

#Extract X and Y coordinates from the 'Location' column eg POINT (-72.8449 41.32326)
data_with_location['Longitude(Value)'] = data_with_location['Location'].apply(lambda x: float(x.split(' ')[1][1:]))
data_with_location['Latitude(Value)'] = data_with_location['Location'].apply(lambda x: float(x.split(' ')[2][:-1]))

# Town            Address   Location                   Longitude(Value)         Latitude(Value)
# Vernon     27 TRACY DRIVE POINT (-72.47857 41.84938) -72.47857  41.84938
#Actual (Approx.) 41°50'58"N 72°28'42"W

# Convert 'X' to Longitude
data_with_location['Longitude'] = data_with_location['Longitude(Value)'].apply(lambda x: f"{abs(x):.5f} {'E' if x >= 0 else 'W'}")

# Convert 'Y' to Latitude
data_with_location['Latitude'] = data_with_location['Latitude(Value)'].apply(lambda y: f"{abs(y):.5f} {'N' if y >= 0 else 'S'}")

# Town            Address   Location                    Longitude    Latitude
#Vernon     27 TRACY DRIVE  POINT (-72.47857 41.84938)  72.47857 W  41.84938 N  

# Print the dataframe with longitude and latitude
#print(data_with_location.head())

# Save the dataframe with location to CSV
data_with_location.to_csv("data_with_location.csv", index=False)

# Save the dataframe without location to CSV
#data_without_location.to_csv("data_without_location.csv", index=False)
