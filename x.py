import pandas
import datetime
def time_to_hour(time):
    '''
    Given an input variable time that represents time in the format of:
    "00:00:00" (hour:minutes:seconds)

    Write a function to extract the hour part from the input variable time
    and return it as an integer. For example:
        1) if hour is 00, your code should return 0
        2) if hour is 01, your code should return 1
        3) if hour is 21, your code should return 21

    Please return hour as an integer.
    '''

    hour = time[0:2]
    return hour

def reformat_subway_dates(date):
    adate = datetime.datetime.strptime(date,"%m-%d-%y")
    date_formatted = datetime.datetime.strftime(adate,"%y-%m-%d")
    return date_formatted


print(time_to_hour("12:23:00"))
print reformat_subway_dates("12-31-15")