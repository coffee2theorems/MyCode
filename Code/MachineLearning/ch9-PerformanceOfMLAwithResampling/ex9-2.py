# Evaluate using a train and a test set

import pandas
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression

url = "https://goo.gl/vhm1eU"
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pandas.read_csv(url, names = names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,Y,test_size = test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train,  y_train)
result = model.score(X_test, y_test)
print("Accuracy: %.3f%%") %(result*100.0)
