import requests
from os import getenv
from dotenv import load_dotenv
from atoma import parse_atom_bytes

load_dotenv()

USER = getenv('username')
LINK = 'https://github.com/'+USER+'.atom'


def format(link):
    temp = (link.split('/'))
    temp = temp[:5]
    link = '/'.join(temp)
    print(link)


response = requests.get(LINK)
feed = parse_atom_bytes(response.content)

for i in range(3):
    projects = feed.entries[i].links[0].href
    format(projects)
