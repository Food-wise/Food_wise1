import json

import requests

""" First url takes ingredients as input and gives ID of recipe as output Need to be a function"""

url = "https://webknox-recipes.p.rapidapi.com/recipes/findByIngredients"

querystring = {"ingredients":"Tomato, chilli, mushroom","number":"5"}

headers = {
    'x-rapidapi-host': "webknox-recipes.p.rapidapi.com",
    'x-rapidapi-key': " YOUR OWN KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

k=response.text
output_list= json.loads(k)

k1=list(output_list)
#print(list(output_list))

for i in range(len(k1)):
    x=k1[i].get('id')
    print(x)
    """ Second part takes recipe ID as input and gives description of recipe as output, need to be a function"""
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/{ x }/information"

    headers = {
      'x-rapidapi-host': "webknox-recipes.p.rapidapi.com",
      'x-rapidapi-key': "YOUR OWN KEY"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

