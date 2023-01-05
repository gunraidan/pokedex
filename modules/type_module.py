import os

#Global Variables
path= os.path.dirname(__file__)
start = str(path)
start = start.replace("\\", "/")
directory = "/assets/"

#Dictionary containing the assests of the Pokémon type images
types = {"Bug": (f'{start}{directory}bug.png'),"Dark": (f'{start}{directory}dark.png'),"Dragon": (f'{start}{directory}dragon.png'),
            "Electric": (f'{start}{directory}electric.png'),"Fairy": (f'{start}{directory}fairy.png'),"Fighting": (f'{start}{directory}fighting.png'),
            "Flying": (f'{start}{directory}flying.png'),"Fire": (f'{start}{directory}fire.png'),"Ghost": (f'{start}{directory}ghost.png'),
            "Grass": (f'{start}{directory}grass.png'),"Ground": (f'{start}{directory}ground.png'),"Ice": (f'{start}{directory}ice.png'),
            "Normal": (f'{start}{directory}normal.png'),"Not Found": (f'{start}{directory}notfound.png'),"Poison": (f'{start}{directory}poison.png'),
            "Psychic": (f'{start}{directory}psychic.png'),"Rock": (f'{start}{directory}rock.png'),"Steel": (f'{start}{directory}steel.png'),
            "Water": (f'{start}{directory}water.png')}

types_hover = {"Bug": (f'{start}{directory}bugh.png'),"Dark": (f'{start}{directory}darkh.png'),"Dragon": (f'{start}{directory}dragonh.png'),
                "Electric": (f'{start}{directory}electrich.png'),"Fairy": (f'{start}{directory}fairyh.png'), "Fighting": (f'{start}{directory}fightingh.png'),
                "Flying": (f'{start}{directory}flyingh.png'),"Fire": (f'{start}{directory}fireh.png'),"Ghost": (f'{start}{directory}ghosth.png'),
                "Grass": (f'{start}{directory}grassh.png'),"Ground": (f'{start}{directory}groundh.png'),"Ice": (f'{start}{directory}iceh.png'),
                "Normal": (f'{start}{directory}normalh.png'),"Not Found": (f'{start}{directory}notfoundh.png'),"Poison": (f'{start}{directory}poisonh.png'),
                "Psychic": (f'{start}{directory}psychich.png'),"Rock": (f'{start}{directory}rockh.png'),"Steel": (f'{start}{directory}steelh.png'),
                "Water": (f'{start}{directory}waterh.png')}

types_press = {"Bug": (f'{start}{directory}bugp.png'),"Dark": (f'{start}{directory}darkp.png'),"Dragon": (f'{start}{directory}dragonp.png'),
                "Electric": (f'{start}{directory}electricp.png'),"Fairy": (f'{start}{directory}fairyp.png'),"Fighting": (f'{start}{directory}fightingp.png'),
                "Flying": (f'{start}{directory}flyingp.png'),"Fire": (f'{start}{directory}firep.png'),"Ghost": (f'{start}{directory}ghostp.png'),
                "Grass": (f'{start}{directory}grassp.png'),"Ground": (f'{start}{directory}groundp.png'),"Ice": (f'{start}{directory}icep.png'),
                "Normal": (f'{start}{directory}normalp.png'),"Not Found": (f'{start}{directory}notfoundp.png'),"Poison": (f'{start}{directory}poisonp.png'),
                "Psychic": (f'{start}{directory}psychicp.png'),"Rock": (f'{start}{directory}rockp.png'),"Steel": (f'{start}{directory}steelp.png'),
                "Water": (f'{start}{directory}waterp.png')}

#Navigates the Json to count if a Pokémon has one or two types
def type_count(dictionary):
    count = 0
    for item in dictionary["types"]:
        if len(item["type"]["name"].toString()) == 0:
            break
        else:
            count +=1
    return count

#Navigates the Json to get information on what each type is strong and weak against        
def type_info(self, dictionary, number):
    type_names = []
    if number == 0:
        self.damage_measure = "Double Damage From"
        for item in dictionary["damage_relations"]["double_damage_from"]:
            if len(item["name"].toString()) > 0:
                type_names.append(item["name"].toString())
            else:
                break

    if number == 1:
        self.damage_measure = "Double Damage To"
        for item in dictionary["damage_relations"]["double_damage_to"]:
            if len(item["name"].toString()) > 0:
                type_names.append(item["name"].toString())
            else:
                break
            
    if number == 2:
        self.damage_measure = "Half Damage From"
        for item in dictionary["damage_relations"]["half_damage_from"]:
            if len(item["name"].toString()) > 0:
                type_names.append(item["name"].toString())
            else:
                break

    if number == 3:
        self.damage_measure = "Half Damage To"
        for item in dictionary["damage_relations"]["half_damage_to"]:
            if len(item["name"].toString()) > 0:
                type_names.append(item["name"].toString())
            else:
                break
            
    if number == 4:
        self.damage_measure = "No Damage From"
        for item in dictionary["damage_relations"]["no_damage_from"]:
            if len(item["name"].toString()) > 0:
                type_names.append(item["name"].toString())
            else:
                break

    if number == 5:
        self.damage_measure = "No Damage To"
        for item in dictionary["damage_relations"]["no_damage_to"]:
            if len(item["name"].toString()) > 0:
                type_names.append(item["name"].toString())
            else:
                break
            
    if len(type_names) == 0:
        type_names.append("None")
    self.type_name_list = type_names

#Retrieves type's name    
def type_name(dictionary, number):
    return dictionary["types"][number]["type"]["name"]   

#Retrieves type's url that plugs into QNetworkAccessManager
def type_url(dictionary, number):
    return dictionary["types"][number]["type"]["url"]