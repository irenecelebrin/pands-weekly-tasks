# week 06
# author: irene celebrin
# task: 
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.

# Using Newton's method: give a number N, the square root of N can be given by the formula:  
# root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1. 
# In the above formula, X is any assumed square root of N and root is the correct square root of N.
# 0.5 is the tolerance limit, which is the max difference allowed between X and root. 
# Source: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# using the function 
# The function requires two parameters: the number to calculate the root, and a tolerance limit. To be honest I understand it only to some extent. I get the computing part, but can't fully graps the mathematics. 

# tolerance limit
l = 0.0001

def sqrt(number, l) :
 
    # Assuming the sqrt of nnmber as number only 
    x = number
 
    # To count the number of iterations 
    count = 0
 
    while (1) :
        count += 1

        # Calculate more closed x 
        root = 0.5 * (x + (number / x)) 
 
        # Check for closeness 
        if (abs(root - x) < l) :
            break
 
        # Update root 
        x = root
 
    return root 
 

#ask user for input number 
number = input('Enter a number (blank to exit): ')

#create loop to prompt for a number and return square root until the anser is blank
while number != '':
    # turn string into float 
    number = float(number)
    # call the function sqrt and print square root of input number 
    print(sqrt(number,l))
    number = input('Enter a number (blank to exit): ')

