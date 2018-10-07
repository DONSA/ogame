from decouple import config
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

ogame = OGame(
    config('UNIVERSE'),
    config('USERNAME'),
    config('PASSWORD')
)

def fleet(planetId, coordinates):
    availableShips = ogame.get_ships(planetId)
    ships = [
        (Ships['SmallCargo'], availableShips['small_cargo']),
        (Ships['LargeCargo'], availableShips['large_cargo'])
    ]

    capacity = 0
    capacity += availableShips['small_cargo'] * 10000
    capacity += availableShips['large_cargo'] * 25000

    speed = Speed['100%']

    mission = Missions['Transport']

    availableResources = ogame.get_resources(planetId)
    resources = {'metal': 0, 'crystal': 0, 'deuterium': 0}

    for type in ['deuterium', 'crystal', 'metal']:
        if (capacity > 0):
            resources[type] = availableResources[type] if availableResources[type] < capacity else capacity
            capacity = capacity - resources[type]

    ogame.send_fleet(planetId, ships, speed, coordinates, mission, resources)
    
    print(ships, resources, coordinates)
