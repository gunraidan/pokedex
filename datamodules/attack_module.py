#Key navigation that retrives the names, urls, and levels from attacks that are learned by leveling up
def attack_info(self, dictionary):
    self.attack_names = [bool]
    self.url_list = [bool]
    self.level_list = [0]
    for a in dictionary["moves"]:
        if len(a["move"]["name"].toString()) == 0:
            break
        for b in a["version_group_details"]:
            if len(b["move_learn_method"]["name"].toString()) == 0:
                break
            if b["move_learn_method"]["name"].toString() == "level-up":
                attack_position(self,self.level_list,b["level_learned_at"].toInt(),a["move"]["name"].toString(),a["move"]["url"].toString())
                break 
    attack_pop(self)
    self.key_count = len(self.attack_names)

#Deletes the placeholder elements in the lists 
def attack_pop(self):
    self.level_list.pop()
    self.attack_names.pop()
    self.url_list.pop()
    
#Measures how an attack's level learned matches up to those that are on the list. Adds it in ascending order.    
def attack_position(self,all_levels, comparison_level, attack, url):
    count = 0
    for i in all_levels:
        count +=1
        if comparison_level <= i:
            break
    self.level_list.insert(count-1,comparison_level)
    self.attack_names.insert(count-1,attack)
    self.url_list.insert(count-1,url)
    
#Retrieves the attack summary and cobines it with the attack name
def attack_summary_info(self,dictionary):
        for item in dictionary["flavor_text_entries"]:
            if len(item["language"]["name"].toString()) == 0:
                break
            if item["language"]["name"].toString() == "en":
                self.attack_explaination = item["flavor_text"].toString()
        self.full_attack = f'Level {self.level_learned}\n{self.attack_name}: {self.attack_explaination}'
            