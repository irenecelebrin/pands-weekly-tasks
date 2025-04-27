# week 02
# author: irene celebrin


# Prompt the user and read in two money amounts (in cent). 
# Define 2 variables and ask the user to enter 2 numbers. The numbers are converted to integers. 
amount1 = int(input('Please enter money amount (in cents): '))
amount2 = int(input('Please enter a second money amount (in cents): '))

# Add the two amounts and turn the number from cents to euros
total = (amount1 + amount2)/100

# Print out the answer in a human readable format with a euro sign.  
print(f'The total is €{total}')
