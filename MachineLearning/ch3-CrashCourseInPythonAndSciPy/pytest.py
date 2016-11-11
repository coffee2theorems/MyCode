
#scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
#numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
#scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

#Python Crash Course

#Strings
data = 'hello world'
print(data[0])
print(len(data))
print(data)

#Numbers
value = 123.1
print(value)
value = 10
print(value)

#Boolean
a = True
b = False
print(a,b)

# Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)

# No Value
a = None
print(a)

#Flow Control

#If-Then-Else
value = 99
if value == 99:
    print 'That is fast'
elif value > 200:
    print 'That is too fast'
else:
    print 'That is safe'

# For - loop
for i in range(10):
    print i

# While - Loop
i = 0
while i < 10:
    print i
    i += 1

#Tuple a read only collection of items
a = (1,2,3)
print a

# Lists indexed by array notation
myList = [1,2,3]
print("Zeroth Value: %d") % myList[0]
myList.append(4)
print("List Length: %d") % len(myList)
for value in myList:
    print value

#Dictionary mapping of names to values
mydict = {'a': 1, 'b': 2, 'c': 3}
print("A value: %d") % mydict['a']
mydict['a'] = 11
print("A value: %d") % mydict['a']
print("Keys: %s") % mydict.keys()
print("Valuse: % s") % mydict.values()
for key in mydict.keys():
    print mydict[key]

# Sum function
def mysum(x, y):
    return x + y

#Test sum function
result = mysum(1 ,3)
print(result)

# define an array
mylist = [1, 2, 3]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)

#access values
mylist = [[1, 2, 3],[3, 4, 5]]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)
print("First row: %s") % myarray[0]
print("Last row: %s") % myarray[-1]
print("Specific row and col: %s") % myarray[0,2]
print("Whole col: %s") % myarray[:, 2]

# arithmetic
myarray1 = numpy.array([2,2,2])
myarray2 = numpy.array([3,3,3])
print("Addition: %s") % (myarray1 + myarray2)
print("Multiplication: %s") % (myarray1 * myarray2)



# in pycharm highlight and press Ctrl + /  to comment a block of code
# # basic line plot
# import matplotlib.pyplot as plt
# import numpy
# myarray = numpy.array([1, 2, 3])
# matplotlib.pyplot.plot(myarray)
# plt.xlabel('some x axis')
# plt.ylabel('some y axis')
# plt.show()
#
# # basic scatter plot
# x = numpy.array([1,2,3])
# y = numpy.array([2, 4, 6])
# plt.scatter(x,y)
# plt.xlabel('some x axis')
# plt.ylabel('some y axis')
# plt.show()

# series
import numpy
import pandas
myarray = numpy.array([1,2,3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)
print(myseries[0])
print(myseries['a'])

# Data Frame
myarray = numpy.array([[1,2,3], [4,5,6]])
rownames = ['a','b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns = colnames)
print(mydataframe)
print("method 1:")
print("one column: %s") % mydataframe['one']
print("method 2: ")
print("one column: %s") % mydataframe.one
