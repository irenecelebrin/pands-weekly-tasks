# week 04
# created by: irene celebrin
# task: Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.



# ask user to input an integer 
current_value = int(input('Please enter an integer number : '))
while current_value != 1: 
    # check if value is even, and in that case divide by 2 -- the result of this is a float, apparently, so I made it an int. 
    if current_value % 2 == 0:
        next_value = int(current_value / 2)
    # if next value is odd, multiply by 3 and add 1 
    else:
        next_value = (current_value * 3) + 1
    # print the result 
    print(next_value)
    # use the result as current value to start the operation again. I have arbitrarly decided to make the result a int, to avoid ending in an infinite loop
    current_value = next_value



 