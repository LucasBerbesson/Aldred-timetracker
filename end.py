import json
import sys
import datetime
import pandas as pd

args = sys.argv[1]
result = '<items>'
xmlitem = '<item arg="{arg}" valid="{valid}"><title>{title}</title><subtitle>{subtitle}</subtitle><icon type="icon.png"></icon></item>'
ongoing = []

df = pd.read_csv('/Users/lucasberbesson/codeproject/timetracker.csv', names=['start', 'end','total','client','action'])
df['start'] = pd.to_datetime(df['start'])
not_ended = df[df['action'] == "None"]

for index, row in not_ended.iterrows():
    arg = "{}@{}".format(index,args)
    result += xmlitem.format(arg=arg,valid="YES",subtitle=args, title="End " + row['client']+ " | Started at " + row['start'].strftime('%H:%M:%S'))

print(result+'</items>')
