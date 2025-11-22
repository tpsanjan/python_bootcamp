# Build SVM model to make predictions on Iris dataset

from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
''
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
''

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names = col_names)

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size = 0.20, random_state = 1)

# Make predictions on validation dataset
model = SVC(gamma = 'auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print('Accuracy = ', round(accuracy_score(Y_validation, predictions),3))
''
print('\n Confusion matrix: \n', confusion_matrix(Y_validation, predictions))
print('\n Classification report: \n', classification_report(Y_validation, predictions))
''
