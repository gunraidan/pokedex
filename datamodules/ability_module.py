#Counts the number of abilities a Pokémon has
def abilities_count(dictionary):
    count = 0
    for a in dictionary["abilities"]:
        if len(a["ability"]["name"].toString()) == 0:
            return count
        else:
            count +=1

#Retrieves effect summary and combines it with the ability name
def ability_effect_info(self, dictionary):
        for item in dictionary["effect_entries"]:
            if len(item["language"]["name"].toString()) == 0:
                break
            if item["language"]["name"].toString() == "en":
                effect_explaination = item["short_effect"].toString()
        try:
            self.full_ability = f'{self.ability_name}: {effect_explaination}'
        except UnboundLocalError:
            try:
                for item in dictionary["flavor_text_entries"]:
                    if len(item["language"]["name"].toString()) == 0:
                        break
                    if item["language"]["name"].toString() == "en":
                        effect_explaination = item["flavor_text"].toString()
                        self.full_ability = f'{self.ability_name}: {effect_explaination}'
            except AttributeError:
                self.full_ability = "N/A"            