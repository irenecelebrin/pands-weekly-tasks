# week 04
# created by: irene celebrin
# task: Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.


# I am not sure if the task is requesting to:
# 1) have the user input a current value, and based on that perform the calculations and ask for a new value until the user inputs 1, or
# 2) have the user inout the value, perform the first calculation and from the result of that continue until the result is 1. not even sure if that's doable at all. 
# So I'll try both


# Interpretation n. 1

# ask user to input an integer 
input_value = int(input('Please enter an integer number (type 1 to quit): '))

# create a while loop that will continue until the input value is 1 
while input_value != 1: 
    # calculate next number 
    next_number = input_value + 1
    # check if next number is even, and in that case divide by 2 -- the result of this is a float, apparently 
    if next_number % 2 == 0:
        output_number = next_number / 2 
    # if next value is odd, multiply by 3 and add 1 
    else:
        output_number = (next_number * 3) + 1
    # print the result 
    print(f'Your output is: {output_number}')
    # ask for input again 
    input_value = int(input('Please enter an integer number (type 1 to quit): '))


# Interpretation n. 2  -- infinite loop, so probably not the right one 

'''
# ask user to input an integer 
current_value = int(input('Please enter an integer number : '))
while current_value != 1: 
    # calculate next number 
    next_number = current_value + 1
    # check if next number is even, and in that case divide by 2 -- the result of this is a float, apparently
    if next_number % 2 == 0:
        output_number = int(next_number / 2)
    # if next value is odd, multiply by 3 and add 1 
    else:
        output_number = (next_number * 3) + 1
    # print the result 
    print(f'Your output is: {output_number}')
    # use the result as current value to start the operation again. I have arbitrarly decided to make the result a int, to avoid ending in an infinite loop
    current_value = output_number
'''
 