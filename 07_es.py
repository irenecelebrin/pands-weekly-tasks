# week 07 
# author: irene celebrin 

# task: Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
# Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

# import os to check if the input file exists 
import os 
# import sys to pass arguments from the command line 
import sys 


# function to read the input file and count the number of times the letter 'e' occurs.
def count_e(input_file): 
    # check if the file name inputted in the console exists
    if not os.path.exists(input_file):
        print('The file does not exist, is misspelled, or you are executing the code from the wrong directory! Please double check.')
    # check if the file has the right format 
    if not input_file.endswith(('.txt')):
        print('This is not a text file. Please provide a .txt file.')
    else:
          print('Counting the e\'s...')  
         
    # read file, count the Es and print the number      
    with open(input_file, 'rt') as f:       
        book = f.read()
        e_number = book.count('e')
        print(f'The number of "es" in {input_file} is {e_number}.')
    

# main 
# check if required args (2) are provided (script, input file). If not, print error message. 
if len(sys.argv) < 2:
    print('Please provide file name')
else: 
    count_e(sys.argv[1])

