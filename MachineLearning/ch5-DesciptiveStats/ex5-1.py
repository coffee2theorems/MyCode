# View first 20 rows
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names = names)
peek = data.head(20)
print(peek)
print "\n"

# Dimensions of your data
shape = data.shape
print(shape)
print "\n"

# Data Types for Each Attribute
types = data.dtypes
print(types)
print "\n"

#Statistical Summary
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = data.describe()
print(description)
print "\n"

# Class Distribution
class_counts = data.groupby('class').size()
print(class_counts)
print "\n"

# Pairwise Pearson correlations
correlations = data.corr(method = 'pearson')
print(correlations)
print "\n"

# Skew for each attribute
skew = data.skew()
print(skew)