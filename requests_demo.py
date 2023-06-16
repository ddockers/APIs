import requests
import json

# get request

post_codes_req = requests.get("https://api.postcodes.io/postcodes/wv69ej") # in Python, go to this URI and store it in the variable

print(post_codes_req) # <Response [200]>

# All of the data isn't printed. The variable does contain all the data. There are methods to get the full data.

print(post_codes_req.status_code) # 200
print(type(post_codes_req.status_code))
print(post_codes_req.content) # return content as bytes (b tag). We need it to be in json, not bytes.
print(post_codes_req.json())

# post request - sending data to the API

json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())

# Pokemon api

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print(pokemon_req.json())

# BBC webpages

bbc_request = requests.get("https://www.bbc.co.uk")
print(bbc_request.content) # .content for sites that aren't apis