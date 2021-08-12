import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
sys.path.append(os.path.join(current_path, "shooting"))
sys.path.append(os.path.join(current_path + '/shooting', 'img'))

import shooting_game


# execfile('shooting_game.py')
# os.system('python shooting_game.py')
