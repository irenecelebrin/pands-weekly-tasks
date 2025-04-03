# week 03 
# author: irene celebrin 
# task: Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

# ask user to enter a bank account number
account_number = input(f'Please enter your account number: ')

# Part 1 
# mask a static 10-digit account number 

# add 6 times 'X' + slice string to get the last 4 digits of account_number 
masked_account_number_static = 'X' * 6 + account_number[6:10]
# test the result
# print(masked_account_number_static)



# Part 2
# mask an account number of variable length. 
# Calculate the account number length, display the last 4 digits and replace the rest with x

# get the lenght of the account number 
n_of_digits = len(account_number) 

# calculate how many Xs need to be added to mask the account number 
n_of_x = n_of_digits - 4 

# concatenate the number of X needed + account number sliced to get only the last 4 digits 
masked_account_number_variable =  'X' * n_of_x + account_number[-4:]

print(f'The masked account number is {masked_account_number_variable}')