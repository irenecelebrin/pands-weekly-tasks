# week 08
# author: irene celebrin 

# task Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, 
# on the one set of axes.

# import numpy and matplotlib 
import numpy as np 
import matplotlib.pyplot as plt 

# the histogram
# define parameters for the histogram 
hist_values_no = 1000
hist_std = 2
hist_mean = 5
# seed the random range to ensure the histogram always looks the same 
np.random.seed(1)
# generate array for the historygram with numpy.random.normal, adding the required parameters. Source:https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html
histogram_values =  np.random.normal(loc=hist_mean, scale=hist_std, size=hist_values_no)


# the plot 
# define parameters 
plot_min = 1
plot_max = 11
# create the array of x values with numpy.arange. The max value is not included in the array. Source: https://numpy.org/doc/2.1/reference/generated/numpy.arange.html
x = np.arange(plot_min,plot_max)
# define h values as h(x) = x**3
h = x ** 3

# plot the data 
plt.hist(histogram_values, label = 'Normal distribution')
plt.plot(x,h, marker='.', label = 'x(h) = x**3')

# set title, legend, ax lables, colours ecc
plt.title('Week 08: Plottask')
plt.legend(labelcolor="linecolor")
plt.xlabel('x', color = 'orange', size = 'x-large')
plt.ylabel('y', color = 'orange', size = 'x-large')
plt.grid(linestyle = 'dashdot', linewidth = '0.3')

plt.show()
plt.savefig('08_plottaks')

