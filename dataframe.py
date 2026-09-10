import pandas as pd

game = pd.read_csv("game_award_2025.csv")
game['Rating'] = [94, 83, 87, 90, 94, 83, 90, 76, 92, 92]

bafta_goldenjoystick_award = game[(game['Award Event'] == 'BAFTA') | (game['Award Event'] == 'Golden Joystick Award')]

# print(game.sort_values(by='Rating', ascending=False))
print(bafta_goldenjoystick_award)

