#!/usr/bin/env python3
import sys
import requests

# Get the film ID from command line arguments
film_id = sys.argv[1]

# Define the URLs
url_film = 'https://swapi-api.hbtn.io/api/films/'
url_movie = f'{url_film}{film_id}/'

# Make a request to get the film data
response = requests.get(url_movie)

if response.status_code == 200:
    fbody = response.json()
    characters = fbody.get('characters', [])

    if characters:
        limit = len(characters)
        def char_request(idx):
            if idx == limit:
                return
            char_url = characters[idx]
            char_response = requests.get(char_url)
            if char_response.status_code == 200:
                rbody = char_response.json()
                print(rbody['name'])
                char_request(idx + 1)
            else:
                print('error:', char_response.status_code)

        char_request(0)
else:
    print('error:', response.status_code)