# # Load CSV using Pandas
# import pandas
# filename = 'pima-indians-diabetes.data.csv'
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# data = pandas.read_csv(filename, names = names)
# print(data.shape)

#Load CSV using Pandas from URL
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names = names)
print(data.shape)