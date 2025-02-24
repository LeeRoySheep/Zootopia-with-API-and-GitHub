import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

ANIMALS_URL = "https://api.api-ninjas.com/v1/animals?name="
HEADERS = {"X-Api-Key": API_KEY}


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """
    return requests.get(ANIMALS_URL+animal_name,HEADERS).json()
