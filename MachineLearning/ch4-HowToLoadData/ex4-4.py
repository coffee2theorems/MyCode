# Load CSV
import numpy
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rb')
data = numpy.loadtxt(raw_data, delimiter=",")
print(data.shape)

# # Load CSV from URL using Numpy
# import numpy
# import urllib
# url = "https://goo.gl/vhm1eU"
# raw_data = urllib.urlopen(url)
# dataset = numpy.loadtxt(raw_data, delimiter = ",")
# print(dataset.shape)