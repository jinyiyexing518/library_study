"""
read_csv   to_csv
read_excel   to_excel
read_jason   to_jason
"""
import pandas as pd


data = pd.read_csv('student.csv')
print(data)

data.to_pickle('student.pickle')















