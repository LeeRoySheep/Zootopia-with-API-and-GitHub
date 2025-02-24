from data_fetcher import fetch_data


def serialize_animal(animal_obj):
    """
    function to create serialized html as string from animal obj
    :param animal_obj:
    :return:
    """
    output = ''
    output += '<li class="cards__item">'
    output += f' <div class="card__title">'
    output += f'{animal_obj["name"]}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul>\n'
    if "diet" in animal_obj["characteristics"]:
        output += f' <li><strong>Diet:</strong> '
        output += f'{animal_obj["characteristics"]["diet"]}</li>\n'
    if "location" in animal_obj:
        output += f' <li><strong>Location:</strong> '
        output += f'{animal_obj["location"][0]}</li>\n'
    if "type" in animal_obj["characteristics"]:
        output += f' <li><strong>Type:</strong> '
        output += f'{animal_obj["characteristics"]["type"]}</li>\n'
    if "skin_type" in animal_obj["characteristics"]:
        output += f' <li><strong>Skin Type:</strong> '
        output += f'{animal_obj["characteristics"]["skin_type"]}</li>\n'
    if "lifespan" in animal_obj["characteristics"]:
        output += f' <li><strong>Lifespan:</strong> '
        output += f'{animal_obj["characteristics"]["lifespan"]}</li>\n'
    if "weight" in animal_obj["characteristics"]:
        output += f' <li><strong>Weight:</strong> '
        output += f'{animal_obj["characteristics"]["weight"]}</li>\n'
    if "top_speed" in animal_obj["characteristics"]:
        output += f' <li><strong>Top Speed:</strong> '
        output += f'{animal_obj["characteristics"]["top_speed"]}</li>\n'
    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'
    return output


def create_data_string(animal_data, animal_selection = None):
    """
    function to create a string with selected data from the json file
    and option to select animals form a selection dict or list
    also an extra option of animal_selection to choose certain types of animals
    :param1 animal_data:
    :param2 animal_selection:
    :return:
    """
    if animal_selection != None:
        animal_data = [
                        animals for animals in animal_data
                        if animals["name"] in animal_selection.keys()
                        ]
    output = ''
    for animal in animal_data:
        output += serialize_animal(animal)
    return output


def html_reader(html_file_path):
    """
    function to read from html file and return input as string
    :param html_file_path:
    :return: html_script_string
    """
    with open(html_file_path, 'r', encoding="utf8") as handler:
        return handler.read()


def html_writer(html_file_path, new_string):
    """
    function to save a html file at html_file_path with new_string as input
    :param1 html_file_path:
    :param2 new_string:
    :return:
    """
    with open(html_file_path, 'w', encoding="utf8") as handler:
        handler.write(new_string)
    print(f'{html_file_path} succesfully created')


def get_skin_types(animals):
    """
    function to create and return a list with all the different skin types
    :param animals:
    :return:
    """
    skin_types_dict = dict()
    for animal in animals:
        if 'skin_type' in animal["characteristics"]:
            skin_types_dict[animal["name"]] = animal["characteristics"]["skin_type"]
    return skin_types_dict


def get_by_skin(skin_type, skin_dict):
    """
    function to return selected skin type dict from a skins type dictionary
    :param skin_type:
    :param skin_dict:
    :return:
    """
    selected_skin_dict = dict()
    for skin in skin_dict.items():
        if skin_type in skin:
            selected_skin_dict[skin[0]] = skin[1]
    return selected_skin_dict


def get_skin_choice(prompt, skins):
    """
    function to get user choice from a skins dictionary
    :param prompt:
    :param skins:
    :return:
    """
    choice = input(prompt)
    while choice not in skins.values():
        print(f'Sorry {choice} is not selectable skin choice!')
        choice = input(prompt)
    return choice


def main():
    """
    main function combining all functionality of this file
    :return:
    """
    chosen_animal = input('Please select an animal: ')
    animals = fetch_data(chosen_animal)
    if len(animals) > 0:
        skin_types = get_skin_types(animals)
        skin_choice = get_skin_choice(
                                    f"Please select one of the "
                                    + f"following skyn types:\n{set(skin_types.values())}"
                                    ,skin_types
                                    )
        animals_left = get_by_skin(skin_choice,skin_types)
        text_input = create_data_string(animals,animals_left)
        replace_text = '__REPLACE_ANIMALS_INFO__'
        html_template = html_reader('animals_template.html').replace(replace_text,text_input)
        html_writer('animals.html',html_template)
    else:
        text_input = f'<h2>The animal {chosen_animal} doesn\'t exist.</h2>'
        replace_text = '__REPLACE_ANIMALS_INFO__'
        html_template = html_reader('animals_template.html').replace(replace_text, text_input)
        html_writer('animals.html', html_template)



if __name__ == '__main__':
    main()
