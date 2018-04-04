#!/usr/bin/python3

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
from grab import grabdata, grabrecord

# authroize credentials
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
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
