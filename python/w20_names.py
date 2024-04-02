from functools import reduce

teams = ['Los Angeles Angels', 'Oakland Athletics', 'Los Angeles Dodgers', 'San Diego Padres', 'San Francisco Giants', 'Tampa Bay Rays', 'Miami Marlins', 'Chicago Cubs', 'Chicago White Sox', 'Kansas City Royals', 'St. Louis Cardinals', 'New York Mets', 'New York Yankees', 'Cincinnati Reds', 'Cleveland Guardians', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'Houston Astros', 'Texas Rangers', 'Arizona Diamondbacks', 'Colorado Rockies', 'Washington Nationals', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Detroit Tigers', 'Minnesota Twins', 'Seattle Mariners', 'Milwaukee Brewers']

name_len = list(map(len, teams))
print("length of each team name:")
print(name_len)

short_names = list(filter(lambda s: len(s) < 15, teams))
print("\nteams with short names:")
print(short_names)

num_words = list(map(lambda s: s.count(' ') + 1, teams))
print("\nword count for each team name:")
print(num_words)

two_words = list(filter(lambda n: n == 2, num_words))
print("\nnumber of teams with 2 word names:", len(two_words))

three_words = list(filter(lambda n: n == 3, num_words))
print("number of teams with 3 word names:", len(three_words))

#get all the teams with 2 word names
two_words = list(filter(lambda s: s.count(' ') == 1, teams))
#remove the first word from each 2 word team
second_word = list(map(lambda s: s[s.find(' ')+1:], two_words))
big_name = reduce(lambda s0, s1: s0 + s1, second_word)
print("\nbig name:", big_name)

