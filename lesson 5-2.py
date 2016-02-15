import sys
import string
import logging
import re

# from util import mapper_logfile
# logging.basicConfig(filename=mapper_logfile, format='%(message)s',
#                     level=logging.INFO, filemode='w')

def mapper():

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the
    #commas, and emit (i.e. print) a key-value pair containing the
    #district (not state) and Aadhaar generated, separated by a tab.
    #Skip rows without the correct number of tokens and also skip
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug
    #statement will interfere with the operation of the grader. Instead,
    #use the logging module, which we've configured to log to a file printed
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    dataOutput = []
    regex = re.compile('[^a-zA-Z0-9]')
    with open("aadhaar_data.csv") as f:
        aadhaar_data = f.readlines()
    header = True
    headerValues={}
    for line in aadhaar_data:
        if header:
            indexColumn=0
            for aColumn in line.split(','):
                headerValues[aColumn]=indexColumn
                indexColumn+=1
            header=False
            districtColumn=headerValues["District"]
            generatedColumn=headerValues["Aadhaar generated"]
        else:
            aadhaarLineData = line.split(',')
            dataOutput.append("{0}\t{1}".format(aadhaarLineData[districtColumn],aadhaarLineData[generatedColumn]))
    return dataOutput

x=mapper()
x=sorted(x)

def reducer(x):

    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar
    #generated, separated by a tab. Make sure each key-value pair is
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug
    #statement will interfere with the operation of the grader. Instead,
    #use the logging module, which we've configured to log to a file printed
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    lastCount=0
    lastItem=None
    for line in x:
        aadhaarLineData = line.split('\t')
        if aadhaarLineData[0]==lastItem:
            lastCount += eval(aadhaarLineData[1])
        else:
            if lastItem<>None:
                print("{0}\t{1}".format(lastItem,float(lastCount)))
            lastItem = aadhaarLineData[0]
            lastCount = eval(aadhaarLineData[1])

    if lastItem<>None:
        print("{0}\t{1}".format(lastItem,float(lastCount)))

reducer(x)
