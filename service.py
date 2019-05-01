import sys
from decouple import config
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

ogame = OGame(
    config('UNIVERSE'),
    config('USERNAME'),
    config('PASSWORD')
)

def farm(origin, destination):
    ships = [
        (Ships['SmallCargo'], 100)
    ]

    ogame.send_fleet(origin['id'], ships, Speed['100%'], destination['coordinates'], Missions['Attack'], {})
    print(ships, destination)

def fleet(origin, destination):
    availableShips = ogame.get_ships(origin['id'])
    availableResources = ogame.get_resources(origin['id'])

    smallCargoes = largeCargoes = 0
    resources = {'metal': 0, 'crystal': 0, 'deuterium': 0}

    # Prioritize deuterim, then crystal and then metal
    for resource in ['deuterium', 'crystal', 'metal']:
        for i in range(availableShips['small_cargo']):
            if (availableResources[resource] > 0 and availableShips['small_cargo'] > 0):
                amount = min(10000, availableResources[resource])
                resources[resource] += amount
                availableResources[resource] -= amount
                smallCargoes += 1
                availableShips['small_cargo'] -= 1

        for i in range(availableShips['large_cargo']):
            if (availableResources[resource] > 0 and availableShips['large_cargo'] > 0):
                amount = min(25000, availableResources[resource])
                resources[resource] += amount
                availableResources[resource] -= amount
                largeCargoes += 1
                availableShips['large_cargo'] -= 1

    ships = [
        (Ships['SmallCargo'], smallCargoes),
        (Ships['LargeCargo'], largeCargoes)
    ]

    ogame.send_fleet(origin['id'], ships, Speed['100%'], destination['coordinates'], Missions['Transport'], resources)
    print(ships, resources, origin['coordinates'])
