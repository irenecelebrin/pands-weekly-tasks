# week 03 
# author: irene celebrin 
# Task: Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

# ask user to enter the bank account number
account_number = input(f'Please enter your account number: ')

# Part 1 
#mask a static 10-digit account numbers 

## add 6 times 'X' + slice string to get the last 4 digits of account_number 
static_masked_account_number = 'X' * 6 + account_number[6:10]
#print(static_masked_account_number)



# Part 2
## mask account number of any lenght. The easy way is assuming that we want to show the last 4 digits and statically add 6 Xs ahead. However, the best solution is probably to replace n. digits with X and display the last 4. 

# get the lenght of the account number 
digit_number = len(account_number) 

# calculate how many Xs need to be added to mask the account number 
n_of_x = digit_number - 4 

# concatenate the number of X needed + account number sliced to get only the last 4 digits 
any_masked_account_number =  'X' * n_of_x + account_number[-4:]

print(any_masked_account_number)