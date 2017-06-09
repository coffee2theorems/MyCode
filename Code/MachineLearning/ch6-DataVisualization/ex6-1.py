# Univariate Histograms
import matplotlib.pyplot as plt
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names = names)

# # univariate histogram
# data.hist()
# plt.show()
#
# # Univariate Density Plots
# data.plot(kind = 'density', subplots = True, layout= (3,3), sharex = False)
# plt.show()

# # Box and Whisker Plots
# data.plot(kind = 'box', subplots = True, layout=(3,3), sharex=False, sharey=False)
# plt.show()