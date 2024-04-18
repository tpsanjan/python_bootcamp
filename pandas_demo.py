import pandas as pd

# Load dataset from a url
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataframe = pd.read_csv(url, names = col_names)

print(type(dataframe))
print(len(dataframe))

print("\n First 5 rows in 'class' column:")
print(dataframe["class"][:5])

print('\n Extracting values from last column:')
vals = dataframe["class"][:5].values
print(type(vals))
print(vals)

# Load dataset from a file
print('\n Extracting values from a csv file:')
df = pd.read_csv('iris.csv', names = col_names)
input1 = df[["sepal-length"]].values.astype('float32')
print(type(input1))
print(input1[:5])
