import csv
def create_master_turnstile_file(filenames, output_file):
    '''
    Write a function that takes the files in the list filenames, which all have the
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file. The input files do not have column header
    rows of their own.

    For example, if file_1 has:
    line 1 ...
    line 2 ...

    and another file, file_2 has:
    line 3 ...
    line 4 ...
    line 5 ...

    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''
    '''filestoprint=[]
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        for filename in filenames:
            fileInput=open(filename,'r')
            inputRows = csv.reader(fileInput, delimiter=',')
            index = 0
            for row in inputRows:
                index=index+1
                if index > len(filestoprint):
                    filestoprint.append(row)
                else:
                    filestoprint[index-1] = filestoprint[index-1] + row
        writeit = csv.writer(master_file, delimiter=',')
        writeit.writerows(filestoprint)#'''
    with open(output_file, 'wb') as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        writeit = csv.writer(master_file, delimiter=',')
        for filename in filenames:
            fileInput=open(filename,'r')
            inputRows = csv.reader(fileInput, delimiter=',')
            for row in inputRows:
                writeit.writerow(row)

files=['C:\\Users\\Administrator\\PycharmProjects\\dataSciIntro\\inp1.txt','C:\\Users\\Administrator\\PycharmProjects\\dataSciIntro\\inp1.txt']
outfile = 'C:\\Users\\Administrator\\PycharmProjects\\dataSciIntro\\output.txt'
create_master_turnstile_file(files,outfile)