import sys
import random
from time import sleep
from service import farm
from coordinates import planets, targets

for k in targets.keys():
    sleep(round(random.uniform(4, 6), 1))
    farm(planets[sys.argv[1]], targets[k])
