import sys
import random
from decouple import config
from time import sleep
from service import fleet
from planets import planets, targets

for alias in sys.argv[2:]:
    sleep(round(random.uniform(4, 6), 1))
    fleet(planets[alias], planets[sys.argv[1]])
