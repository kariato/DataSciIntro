import pandas

baseball_data=pandas.read_csv("Master.csv")
baseball_data['full name']=baseball_data['nameFirst'] + ' ' + baseball_data['nameLast']
baseball_data.to_csv('Master_withfull_name.csv')