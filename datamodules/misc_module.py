from random import choice

#Retrieves Pokémon ID number
def basic_info_id(dictionary):
    return dictionary["id"]

#Retrieves Pokémon name
def evolves_name(dictionary):
    return dictionary["evolves_from_species"]["name"].toString()

#Retrieves Pokémon genus
def genus_info(dict):
    for item in dict["genera"]:
        if len(item["language"]["name"].toString())==0:
            break
        if item["language"]["name"].toString() =="en":
            return item["genus"].toString()

#Retrieves sprites
def sprite_find_official(dict):
    return dict["sprites"]["other"]["official-artwork"]["front_default"].toString()

def sprite_find_animated(dict):   
    return dict["sprites"]["versions"]["generation-v"]["black-white"]["animated"]["front_default"].toString()

#Retrieves all summaries in Json
def summary_info(f_dict, s_dict_1, s_dict_2, t_dict):
    english_dict = []       
    for item in f_dict:
        if len(item[s_dict_1][s_dict_2].toString()) == 0:
            break
        if item[s_dict_1][s_dict_2].toString() == "en":
            entry = item[t_dict]
            english_dict.append(entry.toString())
    summary = choice(english_dict)
    return summary