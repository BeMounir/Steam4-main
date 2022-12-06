import json
import os

cur_path = os.path.dirname(__file__)
huidige_locatie = os.path.join(cur_path, '..', '01 Basisapplicatie', 'steam.json')

with open(huidige_locatie, 'r') as bestand:
    data = json.load(bestand)
    for i in data:
        print(i)

bestand.close()