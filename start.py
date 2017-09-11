import json
import sys
import datetime

args = sys.argv[1]
xmlitem = '<item arg="{arg}" valid="{valid}"><title>{title}</title><subtitle>{subtitle}</subtitle><icon type="icon.png"></icon></item>'


if len(args) > 0:
    newitem = xmlitem.format(arg=args, valid="YES", title=args, subtitle="Start working for "+ args)
print('<items>'+newitem+'</items>')
