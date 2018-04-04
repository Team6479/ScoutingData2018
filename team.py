#!/usr/bin/python3

# data striucture to hold a team
class Team:
    def __init__(self, team_number):
        self.team_number = team_number
        self.num_matches = 0
        self.auto = []
        self.switch = 0
        self.switch_avg = 0
        self.scale = 0
        self.scale_avg = 0
        self.exchange = 0
        self.exchange_avg = 0
        self.climbs = 0
        self.climb_avg = 0
        self.climb_atmps = 0
        self.climb_atmp_avg = 0
        self.comments = []
        # if there is a formtting issue with a an entry, it is stored here
        self.errors = []
        self.num_errors = 0
    
        # check that the dict is actually valid, return true if valid, false if not
    def check(self, dict):
        
        if type(dict['Switch Delivery']) != int:
            return False
        if type(dict['Scale Delivery']) != int:
            return False
        if type(dict['Exchange Delivery']) != int:
            return False

        return True

    # pass in a new dictioanry containing the data
    def update(self, dict):
        # if valid
        if self.check(dict):
            self.num_matches += 1
            self.auto.append(dict['Autonomous'])
            self.switch += dict['Switch Delivery']
            self.switch_avg = self.switch / self.num_matches
            self.scale += dict['Scale Delivery']
            self.scale_avg = self.scale / self.num_matches
            self.exchange += dict['Exchange Delivery']
            self.exchange_avg = self.exchange / self.num_matches
            self.climbs += 1 if dict['Climbing'] == 'Yes' else 0
            self.climb_avg = self.climbs / self.num_matches
            self.climb_atmps += 1 if dict['Climbing'] == 'Attempted' else 0
            self.climb_atmp_avg = self.climb_atmps / self.num_matches
            self.comments.append(dict['Comments'])
        else:
            # not valid
            self.num_errors += 1
            self.errors.append(dict)

    #expand lists
    def expand_list(self, list):
        total = ""
        for x in list:
            total += x + "\n"
        return total

    # format this class for output
    def info(self):
        format = ("Team: {}\n"
                "Matches: {}\n\n"
                "Auto Notes:\n{}\n\n"
                "Switch Average: {}\n"
                "Scale Average: {}\n"
                "Exchange Average: {}\n\n"
                "Succesful Climb Average: {}\n"
                "Attempted Climb Average: {}\n\n"
                "Comments:\n{}\n\n"
                "Improper record count: {}\n")
        info = format.format(self.team_number, 
                            self.num_matches, 
                            self.expand_list(self.auto),
                            self.switch_avg,
                            self.scale_avg,
                            self.exchange_avg,
                            self.climb_avg,
                            self.climb_atmp_avg,
                            self.expand_list(self.comments),
                            self.num_errors)
        
        return info
