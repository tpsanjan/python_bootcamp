import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('demo5a_iris_dirty.csv')

print('\n\n EDA Phase 1 \n')
# Display the first few rows of the dataset
# -- Can be a great option when dealing with large datasets (>65k rows) that can't be opened in MS Excel
print(" First few rows of the dataset:")
print(df.head())

# Check the structure of the dataset
print("\n Structure of the dataset:")
print(df.info())

''
print('\n\n EDA Phase 2 \n')
# Check for missing values
print('Checking for missing values:')
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()
# Alternatively, one could have imputed the missing values based on domain knowledge and/or average/median of the column

# Remove duplicate rows
df = df.drop_duplicates()

# Display the updated dataset
print('\n\n df.head() after dropping rows with missing vals and duplicate entries:\n')
print(df.head())

# Descriptive statistics for numerical columns
print('\n',df.describe())

''
print('\n\n EDA Phase 3 \n')
# One-Hot Encoding for categorical variables
df = pd.get_dummies(df, columns=['Class'], drop_first=True)    
# Note: drop_first = True ==> first encoded column is dropped out. So, only k-1 vars for k categorical vals.

# Standardizing numerical features
scaler = StandardScaler()       # will set the mean to zero and std_dev to one
                                # can help distance-based and gradient based algos (NN, SVM, LR) to converge faster
df[['Sepal-length', 'Sepal-width']] = scaler.fit_transform(df[['Sepal-length', 'Sepal-width']])

# Display the updated dataset
print(df.head())

# Descriptive statistics for numerical columns
print('\n',df.describe())

'''
## Use this block for salary dataset

# One-Hot Encoding for categorical variables
df = pd.get_dummies(df, columns=['Department'], drop_first=True)    
# Note: drop_first = True ==> first encoded column is dropped out. So, only k-1 vars for k categorical vals.

# Standardizing numerical features
scaler = StandardScaler()       # will set the mean to zero and std_dev to one
                                # can help distance-based and gradient based algos (NN, SVM, LR) to converge faster
df[['Salary', 'Age']] = scaler.fit_transform(df[['Salary', 'Age']])

# Display the updated dataset
print(df.head())

# Descriptive statistics for numerical columns
print(df.describe())

# EDA Phase 4

# Histogram for the 'Salary' column to check the distribution
plt.hist(df['Salary'], bins=10, color='skyblue')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()
'''