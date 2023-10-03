# This program will accept a CSV file containing a list of players and assign
# them to three teams. It will then generate a text file with the team roster
# and then generate letters for each of the players' families.

import csv

if __name__ == '__main__':

    player_list = []
    experienced_players = []
    new_players = []
    team_sharks = ['Sharks']
    team_dragons = ['Dragons']
    team_raptors = ['Raptors']
    league_teams = {}

    # Sort players into a list depending on their experience
    def sort_players(players):
        for player in players:
            if 'YES' in player:
                experienced_players.append(player)
            elif 'NO' in player:
                new_players.append(player)
            else:
                continue

    # Evenly assign players to teams
    def assign_players(list_of_players):
        for item in list_of_players:
            if len(team_sharks) > len(team_dragons):
                team_dragons.append(item)
            elif len(team_dragons) > len(team_raptors):
                team_raptors.append(item)
            elif len(team_raptors) > len(team_sharks):
                team_sharks.append(item)
            else:
                team_sharks.append(item)

    # Generate a dictionary with the team name as the key and the players as the value
    def gen_league_dict(team):
        league_teams.update({team[0] : team[1:]})

    # Generate a text file that will display the team rosters
    def gen_team_rosters(league_dictionary):
        with open('teams.txt', 'a') as file:
            for team in league_dictionary:
                file.write(team)
                file.write('\n')
                file.write('=' * 10)
                file.write('\n')
                for player in league_dictionary[team]:
                    file.write(', '.join(player))
                    file.write('\n')
                file.write('\n')

    # Generate a text file containing a letter for each of the players' families
    def generate_letter(league_dictionary):
        for team in league_dictionary:
            for player in league_dictionary[team]:
                new_file = player[0].split(' ')
                file_name = '_'.join(new_file) + '.txt'
                file_lower = file_name.lower()
                with open(file_lower, 'w') as file:
                    file.write(
"Dear {},\n\nYour child, {}, is now one of the {}. \
We look forward to seeing you at practice.\n\n\
Our first practice will be held on July 1st of this year at 3:00pm.\n\n\
Sincerely,\nThe Coach".format(player[3], player[0], team)
)

    # Begin script:
    with open('soccer_players.csv', newline='\n') as csvfile:
        file_reader = csv.reader(csvfile, delimiter = ',')
        for player in file_reader:
            player_list.append(player)
        player_list.remove(player_list[0])

    sort_players(player_list)
    assign_players(experienced_players)
    # Assign players to each team depending on experience
    assign_players(new_players)
    # Build a dictionary of teams and players in the league
    gen_league_dict(team_sharks)
    gen_league_dict(team_dragons)
    gen_league_dict(team_raptors)
    # Generate text files for the roster and a letter for each player's family
    gen_team_rosters(league_teams)
    generate_letter(league_teams)
