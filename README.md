# Real_Estate_HW6
Real Estate Sales Data Analysis
Dataset Source
The dataset used in this project is obtained from [Data.gov](https://catalog.data.gov/dataset/real-estate-sales-2001-2018). The dataset is maintained by the Office of Policy and Management and includes real estate sales with a sales price of $2,000 or greater that occur between October 1 and September 30 of each year. Each sale record includes information such as town, property address, date of sale, property type (residential, apartment, commercial, industrial, or vacant land), sales price, and property assessment.

Dataset Preprocessing (Dataset_Preprocessing.py)
This script performs data preprocessing tasks on the original dataset. It loads the dataset from an Excel file and drops unnecessary columns such as "Non Use Code", "Assessor Remarks", "OPM remarks", and "Date Recorded". It then splits the dataset into two dataframes based on the presence of location information. After dropping rows with missing values, it extracts longitude and latitude information from the "Location" column and saves the preprocessed dataframes to CSV files.

Spark Version Analysis (Real_Estate_Aanalysis_US_CT.py)
This script uses PySpark to perform data analysis on the preprocessed dataset. It loads the data from the CSV file, preprocesses it further by dropping rows with missing values, and trains a linear regression model to predict the sale amount based on features such as assessed value, list year, and sales ratio. It evaluates the model using root mean squared error (RMSE) and visualizes the actual vs. predicted sale amounts using matplotlib.

Single-threaded Version Analysis (Liner_Regression_Single.py)
This script performs similar data analysis tasks as the Spark version but without using Spark. It loads the preprocessed data from the CSV file, splits it into training and testing sets, trains a linear regression model, evaluates the model using mean squared error (MSE) and R-squared score, and visualizes the actual vs. predicted sale amounts using matplotlib.

.gitignore File
The .gitignore file is used to specify intentionally untracked files that Git should ignore. In this project, it is configured to ignore CSV, XLS, and XLSX files.
