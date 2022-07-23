letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#create dictonary correlating letters to points
letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[" "] = 0

#---- adding lower case letters to dictonary
lower_letters_list = []
for letter in letters:
  lower_letters_list.append(letter.lower())

lower_letters_dict = {key:value for key, value in zip(lower_letters_list, points)}

for key, value in lower_letters_dict.items():
  letter_to_points[key] = value

#---- ends here

#returns point total for each word played
def score_word(word):
  point_total = 0
  for letter in word:
   point_total += letter_to_points[letter]
  return point_total

#dict with players and list of words they played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER","BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

#initial point count
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# take in a player and a word, and add that word to the list of words they’ve played
def play_word(player,word):
  player_to_words[player].append(word)

#updates points when a new word is played.
def update_point_totals(player, word):
  play_word(player,word)
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
