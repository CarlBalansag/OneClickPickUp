import requests
from bs4 import BeautifulSoup

valid_steamIdIo_url = "https://steamid.io/lookup/76561198380433908"

steam_profile_url = "https://steamcommunity.com/id/carlgbt/"

url = "https://steamid.io/lookup"
response = requests.post(url, data={'input': steam_profile_url})
soup = BeautifulSoup(response.text, features='html.parser')

keys = [keys.text.strip() for key in soup.select('.keys')]
values = [item.text.strip() for item in soup.select('.value')]

data = {keys: values for keys, value in zip(keys, values)}


from pprint import pprint
pprint(data)