import json
import sys
import pandas as pd
import datetime

arg = sys.argv[1]
arguments = arg.split("@")
if len(arguments) == 1:
    fields = [datetime.datetime.now(),'','', arguments[0], "None"]
    df = pd.read_csv('/Users/lucasberbesson/codeproject/timetracker.csv', names=['start', 'end','total','client','action'])
    df.loc[len(df)]  = fields
    df.to_csv('/Users/lucasberbesson/codeproject/timetracker.csv', header=False)
elif len(arguments) == 2:
    index = int(arguments[0])
    action = str(arguments[1])
    df = pd.read_csv('/Users/lucasberbesson/codeproject/timetracker.csv', names=['start', 'end','total', 'client','action'])
    df['start'] = pd.to_datetime(df['start'])
    df['action'][index] = action
    df['end'][index] = datetime.datetime.now()
    df['total'][index] = df['end'][index] - df['start'][index]
    df.to_csv('/Users/lucasberbesson/codeproject/timetracker.csv', header=False)

print("hello")
