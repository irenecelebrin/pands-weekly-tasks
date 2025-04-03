# week 05 
# author: irene celebrin 
# task: Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

# import datetime module 
import datetime

def is_weekday():   
    # get today's date
    today_date = datetime.datetime.now()

    # get today's day of the week 
    today_day = today_date.strftime("%A")

    # create a list of weekdays
    weekday = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
    ]

    # check if the day today belongs to the list of weekdays. If it does, say that it's a weekday. Otherwise, print a message saying that it's the weekend. 
    if today_day in weekday:
        print('Yes, unfortunately today is a weekday.')
    else:
        print('It is the weekend, yay!')

# I am adding this part (if __name__ == '__main__':) to ensure that the script is executed as main program. 
# In this way, if I later import the module in another script, it will not run automatically but only if executed directly.  
if __name__ == '__main__':
    is_weekday()

    