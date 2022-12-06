import requests
import json

baseurl = 'http://api.steampowered.com/'
apikey = 'EAB2461948040FB3FD421D19282C63EA'
ISteamUser = 'ISteamUser'
method = 'GetPlayerSummaries'
versie = '0002'
steamid = '76561197960435530'
completeURL = '{}{}/{}/v{}/?key={}&steamids={}'.format(baseurl, ISteamUser, method, versie, apikey, steamid)
response = requests.get(completeURL)

with open("package.json", "w") as outfile:
    json.dump(response.json(), outfile, indent=4)
