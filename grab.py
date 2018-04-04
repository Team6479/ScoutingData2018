#!/usr/bin/python3

import gspread
from team import Team

def grabrecord(client, docid):
    # open the sheet
    sheet = client.open_by_key(docid).sheet1
    # get a list of dictionaries, each dict is a record of a match
    records = sheet.get_all_records()
    return records

def grabdata(records, *team_nums):
    # store all of the teams
    teams = {}

    # loop through records
    for r in records:
        team_num = r['Team Number']
        # if the team already exsists in the list, uodate its info
        if team_num in teams:
            teams[team_num].update(r)
        # otherwise add a new team
        else:
            team = Team(team_num)
            team.update(r)
            teams[team_num] = team

    data = []

    # no args, print all teams
    if len(team_nums) == 0:
        for team in teams.values():
            data.append(team.info())
    # for each team in args, print out the info
    else:
        for team_num in team_nums:
            num = int(team_num)
            if num in teams:
                data.append(teams[num].info())
            else:
                data.append("No data for Team {}\n".format(team_num))

    return data