'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
import os

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'


def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    pokemon_artwork_download_and_save("PikaChu","C:\\Users\\chara\\OneDrive\\Desktop\\github\\Comp593-Lab10")
    return

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

# TODO: Define function that gets a list of all Pokemon names from the PokeAPI
def pokemon_list(limit):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    data = response.json()
    L=[]
    for pokemon_name in data['results']:
        L.append(pokemon_name['name'])
    return L

# TODO: Define function that downloads and saves Pokemon artwork
def pokemon_artwork_download_and_save(pokemon_nm,images_dir):
    poke_info = get_pokemon_info(pokemon_nm)
    image_file_path = os.path.join(images_dir,f"{pokemon_nm.upper()}.png")
    art_url = poke_info["sprites"]["other"]["official-artwork"]["front_default"]
    if art_url == "":
        print(f"No artwork found for {pokemon_nm}")
    with open(image_file_path,'wb') as image_file:
            image_file.write(requests.get(art_url).content)
    
    return image_file_path


if __name__ == '__main__':
    main()