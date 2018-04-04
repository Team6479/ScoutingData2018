#!/usr/bin/python3

try:
    import gspread
except ImportError:
    print("You need to install gspread on this computer")
    exit(1)
try:
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError:
    print("You need to install oauth2client on this computer")
    exit(1)

import sys
from grab import grabdata, grabrecord

# authroize credentials
scope = ['https://spreadsheets.google.com/feeds']
try:
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
except FileNotFoundError:
    print("Please follow the directions in the README to install client_secret.json")
    exit(1)
client = gspread.authorize(creds)

# if no cmd line args
if(len(sys.argv) == 1):
    print("Invalid call\nProper Usage `./scouting.py <match|pit> [team number]...`")
    exit(1)

# check the second cmd line arg
mode = sys.argv[1]
# if 'match', grab match data
if mode == 'match':
    docid = '1YWW_BiWzqRcWd8Swx6xowu2HCisGTZ1Y_nBUhefpPB4'
elif mode == 'pit':
    docid = '15Agfe1dqCwwauXtZQgBtebTbf3dgh98It7p1PO5yHZQ'
else:
    print("Invalid mode\nProper Usage `./scouting.py <match|pit> [team number]...`")
    exit(1)

# get records 
records = grabrecord(client, docid)
# parse the data
data = grabdata(records, *sys.argv[2:])
print("\n\n-----------------\n\n\n".join(data))
