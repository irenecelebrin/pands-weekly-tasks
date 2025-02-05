# week02
# some maths 
# created by: irene celebrin


# Prompt the user and read in two money amounts (in cent)
amount1 = int(input('Please enter money amount (in cents): '))
amount2 = int(input('Please enter a second money amount (in cents): '))

# Add the two amounts
total = (amount1 + amount2)/100

# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
print(f'The total is €{total}')
