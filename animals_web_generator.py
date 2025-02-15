import requests

ANIMALS_URL = "https://api.api-ninjas.com/v1/animals?name="
HEADERS = {"X-Api-Key": "b4BAh+MXttwkZrqLc6Brvw==6EGeCvbEsT0jSoQG"}


def main():
    '''
    '''
    inp_animal = input("Enter a name of an animal: ")
    print(requests.get(ANIMALS_URL+inp_animal,HEADERS))

if __name__ == "__main__":
    main()