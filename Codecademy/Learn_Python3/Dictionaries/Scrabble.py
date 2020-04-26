letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters_to_points = {key:value for key,value in zip(letters,points)}
print(letters_to_points,'\n')
letters_to_points[' '] = 0
print(letters_to_points,'\n')

def score_word(word):
#   global letters_to_points
  sum = 0
  for letter in word:
    sum += letters_to_points.get(letter,0)
  return sum

player_to_words = {'player1':['BLUE', 'TENNIS', 'EXIT'], 'wordNerd':['EARTH', 'EYES', 'MACHINE'], 'Lexi Con':['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader':['ZAP', 'COMA', 'PERIOD']}
player_to_point = {}
for player,words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_point[player] = player_points
  print("{gamer} has {num} points.".format(gamer = player , num = player_points),'\n')
print(player_to_point)

def play_word(player,word):
    value = player_to_words.get(player,'NA')
    value.append(word)
     