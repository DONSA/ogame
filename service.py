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
    availableResources = ogame.get_resources(planetId)

    capacity = 0
    capacity += availableShips['small_cargo'] * 10000
    capacity += availableShips['large_cargo'] * 25000

    resources = {'metal': 0, 'crystal': 0, 'deuterium': 0}

    # Prioritize deuterim, then crystal and then metal
    for type in ['deuterium', 'crystal', 'metal']:
        if (capacity > 0):
            resources[type] = availableResources[type] if availableResources[type] < capacity else capacity
            capacity -= resources[type]

    # Exclude small cargoes that are not necessary
    necessarySmallCargoes = max(0, availableShips['small_cargo'] - int(capacity / 10000))
    capacity -= availableShips['small_cargo'] - necessarySmallCargoes

    # Exclude large cargoes that are not necessary
    necessaryLargeCargoes = max(0, availableShips['large_cargo'] - int(capacity / 25000))
    capacity -= availableShips['large_cargo'] - necessaryLargeCargoes

    ships = [
        (Ships['SmallCargo'], necessarySmallCargoes),
        (Ships['LargeCargo'], necessaryLargeCargoes)
    ]

    ogame.send_fleet(planetId, ships, Speed['100%'], coordinates, Missions['Transport'], resources)

    print(ships, resources, coordinates)
