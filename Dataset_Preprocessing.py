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
data_with_location['X'] = data_with_location['Location'].apply(lambda x: float(x.split(' ')[1][1:]))
data_with_location['Y'] = data_with_location['Location'].apply(lambda x: float(x.split(' ')[2][:-1]))

print(data_with_location.head())
# Town            Address   Location         X         Y
# Vernon     27 TRACY DRIVE POINT (-72.47857 41.84938) -72.47857  41.84938
#Actual 41°50'58"N 72°28'42"W

#data.to_csv("", index=False)