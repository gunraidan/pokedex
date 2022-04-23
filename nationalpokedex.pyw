#Essentials
import os
import sys

#Modules
from random import choice
import re
import requests
from string import Template
import threading
import time


#Audio
from pygame import mixer
from playsound import playsound

#GUI
from PyQt6 import QtNetwork
from PyQt6.QtGui import*
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import*
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer, QUrl
from simplejson import JSONDecodeError

#Global Variables
path= os.path.dirname(__file__)
start = str(path)
start = start.replace("\\", "/")
directory = "/assets/"

sound_cut = False

class Audio():
    #Audio
    mixer.init()
    def play_music(mp3):
        song = f"{start}{directory}{mp3}"
        mixer.music.load(song)
        mixer.music.set_volume(.5)
        mixer.music.play()
        
    def music():
        time.sleep(.6)
        Audio.play_music("pokemonthemestart.mp3")
        time.sleep(47.5)
        while True:
            if sound_cut:
                mixer.music.set_volume(0)
            else:
                Audio.play_music("pokemonthemeloop.mp3")
                time.sleep(43.1)

    def error_sound():
        playsound(f"{start}{directory}pokemonerror.mp3")
        
    def confirmed_sound():
        playsound(f"{start}{directory}pokemonconfirmed.mp3")
     

threading.Thread(target=Audio.music, daemon = True).start()

#Text Updater
class Update():
    
    changed_text = ""
    
    def __init__(self, text = None):
        self.text = text
        
    def get_text(self):
        return self.text
    
    def set_text(self, new_text):
       self.text = new_text
       
    def text_update(entered):
        pull = Update()
        pull.set_text(entered)
        result = pull.text
        template = Template("$text")
        text_string = template.safe_substitute(text = result)
        Update.changed_text = text_string

#GUI        
class MainWindow(QWidget):
    
    def __init__ (self):
        super().__init__()
        self.title = "National Pokédex"
        self.left = 200
        self.top = 300
        self.width = 518
        self.height = 654
        self.scaling()
        self.mw_attributes()
        self.abilities_button()
        self.attacks_button()
        self.back_button()
        self.next_button()
        self.start_button()
        self.summary_button()
        self.type_button_1()
        self.type_button_2()
        self.user_input()
        self.stats()
        self.scrolling()
        self.evolves_from_button()
        self.mute_button()
        self.show() 
        
        
      
    
    def mw_attributes(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top,self.width, self.height)
        self.setFixedSize(self.size())
        self.pixmap = QPixmap(f"{start}{directory}pokedexbgnew.png")
        self.skin_label = QLabel(self)
        self.skin_label.setPixmap(self.pixmap)
        self.skin_label.resize(self.pixmap.width(),self.pixmap.height())
        self.pokemon_image_screen = QLabel(self)
        self.pokemon_image_screen.setPixmap(QPixmap())
        self.pokemon_image_screen.setGeometry(45, -55, 472, 460)
        self.pokemon_gif_screen = QLabel("Label", self)
        self.movie = QMovie()
        self.movie.setCacheMode(QMovie.CacheMode.CacheAll)
        self.pokemon_gif_screen.setGeometry(320, -110, 472, 460)
        self.pokemon_gif_screen.setMovie(self.movie)
        self.borders_screen = QLabel(self)
        self.borders_screen.setPixmap(QPixmap())
        self.borders_screen.setGeometry(0, 0, 518, 654)
        self.button_lights = QLabel(self)
        self.pixmap_buttons = QPixmap(f"{start}{directory}lights_default.png")
        self.button_lights.setPixmap(self.pixmap_buttons)
        self.button_lights.setGeometry(4,264,23,92)
        
    def scrolling(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.summary_screen)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedHeight(108)
        self.scroll_area.setFixedWidth(442)
        self.scroll_area.setStyleSheet("border: 0px" ";" "width:3px;" ";" "background-color: transparent")
        self.scroll_area.move(42, 502)

    def stats(self):
        font = "Tahoma"
        text_color = "DodgerBlue3"
        placeholder_text = ""        
        
        self.evolves_screen = QLabel (placeholder_text, self)
        self.evolves_screen.setGeometry(45, 438, 175, 65)
        self.evolves_screen.setStyleSheet(f"color: {text_color}")
        self.evolves_screen.setFont(QFont(font,13))
        
        self.name_screen = QLabel (placeholder_text, self)
        self.name_screen.setGeometry(55, 238, 165, 65)
        self.name_screen.setStyleSheet(f"color: {text_color}")
        self.name_screen.setFont(QFont(font,14))
        self.name_screen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.number_screen = QLabel (placeholder_text, self)
        self.number_screen.setGeometry(45, 58, 105, 65)
        self.number_screen.setStyleSheet(f"color: {text_color}")
        self.number_screen.setFont(QFont(font,14))
        
        self.genus_screen = QLabel (placeholder_text, self)
        self.genus_screen.setGeometry(34, 285, 215, 65)
        self.genus_screen.setStyleSheet(f"color: {text_color}")
        self.genus_screen.setFont(QFont(font,14))
        self.genus_screen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.height_screen = QLabel (placeholder_text, self)
        self.height_screen.setGeometry(45, 378, 125, 65)
        self.height_screen.setStyleSheet(f"color: {text_color}")
        self.height_screen.setFont(QFont(font,14))
        
        self.weight_screen = QLabel (placeholder_text, self)
        self.weight_screen.setGeometry(45, 400, 175, 65)
        self.weight_screen.setStyleSheet(f"color: {text_color}")
        self.weight_screen.setFont(QFont(font,14))
      
        self.summary_screen = QLabel (placeholder_text, self)
        self.summary_screen.setGeometry(45, 463, 455, 180)
        self.summary_screen.setStyleSheet("color: black")
        self.summary_screen.setFont(QFont(font,14))
        self.summary_screen.setWordWrap(True)
        
        self.error_screen = QLabel(placeholder_text, self)
        self.error_screen.setGeometry(105, 63, 330, 80)
        self.error_screen.setStyleSheet("color: red")
        self.error_screen.setFont(QFont('Arial',22))
         
    
    def scaling(self):
        if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

        if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
            
    def abilities_button(self):
        self.abilities_button = QPushButton(self)
        self.abilities_button.setHidden(True)
        self.abilities_button.clicked.connect(self.abilities_button_click)
        self.abilities_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}abilities.png)"
                               "}"
                               "QPushButton:hover"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}abilitiesh.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}abilitiesp.png)"
                               "}"
                               )
                               
        self.abilities_button.resize(152,112)
        self.abilities_button.move(298,202)
    
    def abilities_button_click(self):  
        self.ability_summary = f"{self.abilities[0]}: {self.short_effects[0]}"
        Data.transform(self.ability_summary)
        Data.paste_info(self, "", self.summary_screen.setText)
        self.back_button.setHidden(False)
        self.next_button.setHidden(False)
        self.topic = "abilities"
        self.ability_info_order = 0
        
    def attacks_button(self):
        self.attacks_button = QPushButton(self)
        self.attacks_button.setHidden(True)
        self.attacks_button.clicked.connect(self.attacks_button_click)
        self.attacks_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}attacks.png)"
                               "}"
                               "QPushButton:hover"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}attacksh.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}attacksp.png)"
                               "}"
                               )
                               

        self.attacks_button.resize(152,112)
        self.attacks_button.move(298,332)
        
    def attacks_button_click(self):  
        Data.transform(self.attack_summary[0])
        Data.paste_info(self, "", self.summary_screen.setText)
        self.back_button.setHidden(False)
        self.next_button.setHidden(False)
        self.topic = "attacks"
        self.attack_info_order = 0
        
    def evolves_from_button(self):
        self.previous_evolution_flag = False
        self.efb_text = ""
        self.evolves_button = QPushButton(self.efb_text, self)
        self.evolves_button.setHidden(True)
        self.evolves_button.clicked.connect(self.evolves_button_click)
        self.evolves_button.setStyleSheet("QPushButton"
                                "{"
                                "background:transparent;"f"background-image : url()"
                                "}"
                                "QPushButton:hover"
                                "{"
                                "background:transparent; color : white"
                                "}"
                                )
        self.evolves_button.setFont(QFont('Tahoma', 14))
        self.evolves_button.resize(185,70)
        self.evolves_button.move(60, 440)
        
    def evolves_button_click(self):
        self.previous_evolution_flag = True
        Data.extract(self)
    

    def summary_button(self):
        self.summary_button = QPushButton(self)
        self.summary_button.setHidden(True)
        self.summary_button.clicked.connect(self.summary_button_click)
        self.summary_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}summary.png)"
                               "}"
                               "QPushButton:hover"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}summaryh.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}summaryp.png)"
                               "}"
                               )
        self.summary_button.resize(57,32)
        self.summary_button.move(445,465)

    def summary_button_click(self):
        Data.transform(self.summary)
        Data.paste_info(self, "", self.summary_screen.setText)
        self.next_button.setHidden(True)
        self.back_button.setHidden(True)
        
    def type_button_1(self):
        self.type_button = QPushButton(self)
        self.type_button.clicked.connect(self.type_button_1_click)
        self.type_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;""background-image : url()"
                               "}"
                               )
        self.type_button.resize(48,48)
        self.type_button.move(80,332)
        

    def type_button_1_click(self):
        self.damage_summary = f"Double Damage From: {self.ddf[0]}"
        Data.transform(self.damage_summary)
        Data.paste_info(self, "", self.summary_screen.setText)
        self.next_button.setHidden(False)
        self.back_button.setHidden(False)
        self.topic = "types"
        self.type_order = 0
        self.type_info_order = 0
        

    def type_button_2(self):
        self.type_button_second = QPushButton(self)
        self.type_button_second.clicked.connect(self.type_button_2_click)
        self.type_button_second.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;""background-image : url()"
                               "}"
                               )
        self.type_button_second.resize(48,48)
        self.type_button_second.move(136,332)
        
        
        
    def type_button_2_click(self):  
        self.damage_summary_2 = f"Double Damage From: {self.ddf[1]}"
        Data.transform(self.damage_summary_2)
        Data.paste_info(self, "", self.summary_screen.setText)
        self.next_button.setHidden(False)
        self.back_button.setHidden(False)
        self.topic = "types"
        self.type_order = 1
        self.type_info_order = 0
        
    def next_button(self):
        self.next_button = QPushButton(self)
        self.next_button.setHidden(True)
        self.next_button.clicked.connect(self.next_button_click)
        self.next_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}back.png)"
                               "}"
                               "QPushButton:hover"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}backh.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}backp.png)"
                               "}"
                               )
        self.next_button.resize(12,85)
        self.next_button.move(486,513)
        
    def next_button_click(self):
        try:             
            if self.type_info_order > 4:
                self.type_info_order = 0
            else:
                self.type_info_order +=1
        except: AttributeError
           
        try:
            if self.ability_info_order > len(self.abilities) - 2:
                self.ability_info_order = 0
            else:
                self.ability_info_order +=1
        except: AttributeError
        
        try:
            if self.attack_info_order > len(self.attack_summary) - 2:
                self.attack_info_order = 0
            else:
                self.attack_info_order +=1
        except: AttributeError
        self.button_click_action()
            
    def back_button(self):
        self.back_button = QPushButton(self)
        self.back_button.setHidden(True)
        self.back_button.clicked.connect(self.back_button_click)
        self.back_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}back.png)"
                               "}"
                               "QPushButton:hover"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}backh.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}backp.png)"
                               "}"
                               )
        self.back_button.resize(12,85)
        self.back_button.move(26,513)
        
    
    def back_button_click(self):
        try:
            if self.type_info_order ==0:
                self.type_info_order =5 
            else:
                self.type_info_order -=1
        except: AttributeError
        try: 
            if self.ability_info_order ==0:
                self.ability_info_order = len(self.abilities) - 1
            else:
                self.ability_info_order -=1
        except: AttributeError
        try:
            if self.attack_info_order ==0:
                self.attack_info_order = len(self.attack_summary) - 1
            else:
                self.attack_info_order -=1
        except: AttributeError
        self.button_click_action()
        
        
    def button_click_action(self):
        if self.topic == "types":    
            type_info = {0: f"Double Damage From: {self.ddf[self.type_order]}", 1: f"Double Damage To: {self.ddt[self.type_order]}", 2: f"Half Damage From: {self.hdf[self.type_order]}", 3: f"Half Damage To: {self.hdt[self.type_order]}", 4: f"No Damage From: {self.ndf[self.type_order]}", 5: f"No Damage To: {self.ndt[self.type_order]}"}                    
            self.damage_summary = type_info[self.type_info_order]
            Data.transform(self.damage_summary)
            Data.paste_info(self, "", self.summary_screen.setText)
            
        elif self.topic == "abilities":     
            self.ability_summary = f"{self.abilities[self.ability_info_order]}: {self.short_effects[self.ability_info_order]}"
            Data.transform(self.ability_summary)
            Data.paste_info(self, "", self.summary_screen.setText)
            
        elif self.topic == "attacks":
            self.attack_shown = f"{self.attack_summary[self.attack_info_order]}"
            Data.transform(self.attack_shown)
            Data.paste_info(self, "", self.summary_screen.setText)
            
            
    def mute_button(self):
        self.mute_button = QPushButton(self)
        self.mute_button.clicked.connect(self.mute_button_click)
        self.mute_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}mute_off.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}mute_on_p.png)"
                               "}"
                               )
                               

        self.mute_button.resize(24,31)
        self.mute_button.move(233,11)
        
    def mute_button_click(self):
        global sound_cut 
        if sound_cut:
            mixer.music.set_volume(.5)
            sound_cut = False
            self.mute_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}mute_off.png);"
                               "}"
                                "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}mute_on_p.png)"
                               "}")  
        else:
            mixer.music.set_volume(0)
            sound_cut = True
            self.mute_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}mute_on.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}mute_off_p.png)"
                               "}")
            
    def user_input(self):
        self.line = QLineEdit(self)
        self.line.setPlaceholderText("Enter Pokémon name/#...")
        self.line.setStyleSheet("QLineEdit" "{" "background:dark green""}" "QLineEdit" "{" "color:limegreen""}")
        self.line.setFont(QFont('Consolas',11))
        self.line.resize(182,32)
        self.line.move (280,22)
        
    def button_activation(self):
        self.abilities_button.setHidden(False)
        self.attacks_button.setHidden(False)
        self.summary_button.setHidden(False)
        self.evolves_button.setHidden(False)
        self.error_screen.setText("")
        
        
    def start_button(self):
        self.button_s = QPushButton(self)
        self.button_s.clicked.connect(self.start_button_click)
        self.manager = QtNetwork.QNetworkAccessManager()
        self.button_s.setEnabled(True)
        self.button_s.setText("")
        self.button_s.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}button.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}button_pressed.png)"
                               "}"
                               )                 
        self.button_s.resize (48,48)
        self.button_s.move(460,12)

            
    def start_button_click(self):
        try:
            Data.extract(self)
        except JSONDecodeError:
            self.error_screen.setHidden(False)
            self.error_screen.setText("No Pokémon in Database")
            Data.error_light_on(self)
            QTimer.singleShot(4500, lambda: self.error_screen.setHidden(True))
            threading.Thread(target=Audio.error_sound).start()
            x = 0
            for i in range(5):
                x+=500
                QTimer.singleShot(x, lambda: Data.error_light_on(self))
                x+=500
                QTimer.singleShot(x, lambda: Data.lights_off(self))
                    
              
class Data():
    
    pokemon_dict = {}
    
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
    
       
#Running the API
    def run_api(self,directory, subdirectory):
        self.directory = directory
        self.subdirectory = subdirectory
        contact = {'User-Agent': '("Accept: application/json", "Cache-Control: max-age=360",)'}
        response = requests.get (f'https://pokeapi.co/api/v2/{self.directory}/{self.subdirectory}', headers = contact)
        self.data = response.json()
        
   
#Updating Text
    def transform (entered):
        Update.text_update(entered)
        template = Template("$t_score")
        transformed_score = template.safe_substitute(t_score = Update.changed_text)
        
    def paste_info(self,pre, text_variable):
        template2 = Template("$text")
        label_string = template2.safe_substitute(text = Update.changed_text)
        text_variable(pre + label_string)   

#The "Mother Code" Run        
    def extract(self):
        if self.previous_evolution_flag:
            self.pokemon = self.evolves_from.lower()
        else:
            self.pokemon = self.line.text().lower()
        Data.run_api(self,"pokemon", self.pokemon)
        Data.pokemon_dict.update(self.data)
        MainWindow.button_activation(self)
        self.name = Data.pokemon_dict["name"].title()
        Data.height_weight(self)
        Data.ability_list(self)
        Data.ability_effect(self)
        Data.type(self)
        Data.misc_info(self)
        Data.attacks(self)
        Data.create_attack_summary_list(self)
        threading.Thread(target=Audio.confirmed_sound).start()
        Data.find_sprites(self)
        Data.show_sprites(self)
        self.borders_screen.setPixmap(QPixmap(f"{start}{directory}foreground.png"))
        Data.stat_updates(self)
        Data.type_image_updates(self)
        self.skin_label.setPixmap(QPixmap(f"{start}{directory}pokedexbgnew2.png"))
        Data.complete_light_on(self)
        self.previous_evolution_flag = False
        QTimer.singleShot(2000, lambda: Data.lights_off(self))
        
    def complete_light_on(self):
        self.button_lights.setPixmap(QPixmap(f"{start}{directory}lights_complete.png"))
                     
    def error_light_on(self):
        self.button_lights.setPixmap(QPixmap(f"{start}{directory}lights_error.png"))

    def lights_off(self):
        self.button_lights.setPixmap(QPixmap(f"{start}{directory}lights_default.png"))
            
    
    def stat_updates(self):
        self.evolve_sentence = "Evolves\n from:"
        self.evolves_screen.setText(self.evolve_sentence)
        Data.transform(self.name)
        Data.paste_info(self, "", self.name_screen.setText)
        Data.transform(self.national_number)
        Data.paste_info(self, "#", self.number_screen.setText)
        Data.transform(self.genus[0])
        Data.paste_info(self, "", self.genus_screen.setText)
        Data.transform(self.height_ft)
        Data.paste_info(self, "Height: ", self.height_screen.setText)
        Data.transform(self.weight_lbs)
        Data.paste_info(self, "Weight: ", self.weight_screen.setText)
        Data.transform(self.summary)
        Data.paste_info(self, "", self.summary_screen.setText)
        
        
        
    def type_image_updates(self):
        second_type = False
        try:
            type_1 = self.types[0]
            type_2 = self.types[1]
            second_type = True
        except IndexError:
            self.type_button_second.hide()
        try:
            Data.types[type_1]
        except KeyError:
            type_1 = "Not Found"
            
        self.type_1 = Data.types[type_1]
        self.type_1_h = Data.types_hover[type_1]
        self.type_1_p = Data.types_press[type_1]
        
        if second_type:
            try:
                Data.types[type_2]
            except KeyError:
                type_2 = "Not Found"
            self.type_2 = Data.types[type_2]
            self.type_2_h = Data.types_hover[type_2]
            self.type_2_p = Data.types_press[type_2]
  
        
        self.type_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({self.type_1})"
                               "}"
                               "QPushButton:hover"
                               "{"
                               "background:transparent;"f"background-image : url({self.type_1_h})"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({self.type_1_p})"
                               "}"
                               )
        
        if second_type:
            self.type_button_second.show()
            self.type_button_second.setStyleSheet("QPushButton"
                                "{"
                                "background:transparent;"f"background-image : url({self.type_2})"
                                "}"
                                "QPushButton:hover"
                                "{"
                                "background:transparent;"f"background-image : url({self.type_2_h})"
                                "}"
                                "QPushButton:pressed"
                                "{"
                                "background:transparent;"f"background-image : url({self.type_2_p})"
                                "}"
                                )
        
        
    
#Height & Weight of Pokémon   
    def height_weight(self):      
        #Height
        self.height_cm = (int(Data.pokemon_dict["height"]) * 10)
        self.height_ft = self.height_cm * 0.0328084
        height_raw = str(self.height_ft).split(".")
        feet = height_raw[0]
        inches = (float("." + height_raw[1]) * 1.2)
        inches = float(round(inches,1)) * 10
        inches = str(int(inches))
        if inches == "12":
            feet = int(feet) + 1
            self.height_ft = ("~" + str(feet) + " ft")
        else:
            self.height_ft = feet + "'" + inches + '"'
        
        #Weight
        self.weight_kg = int(Data.pokemon_dict["weight"]) /10
        self.weight_lbs = round((self.weight_kg * 2.20462262),1)
        self.weight_lbs = (str(self.weight_lbs) + " lbs")
        
                
#Abilities & Ability Summarizations        
    def ability_list(self):
        abilities = []
        ability_count = len(Data.pokemon_dict["abilities"])
        for i in range (ability_count):
            names = Data.pokemon_dict["abilities"][i]['ability']['name']
            abilities.append(names.title())
            self.abilities = abilities
        return self.abilities
   
    def ability_effect(self):
        long_effects_list = []
        short_effects_list = []
        effect_urls = []
        effects_count = len(self.abilities)
        for i in range (effects_count):
            urls = Data.pokemon_dict["abilities"][i]['ability']['url']
            effect_urls.append(urls)
        self.effect_urls = effect_urls
        for i in range (len(self.effect_urls)):    
            response = requests.get (self.effect_urls[i])
            self.data = response.json()
            effect_entries = self.data["effect_entries"]
            for i in range (len(effect_entries)):
                effect = effect_entries[i]
                pattern =  r"{'name': 'en',"
                matches = re.findall(pattern, str(effect))
                if len(matches) > 0:
                    long_effects_list.append(effect["effect"])
                    short_effects_list.append(effect["short_effect"])
            self.long_effects = long_effects_list
            self.short_effects = short_effects_list
      
    #Type
    def type(self):
        #What Type is the Pokémon?
        type_list = []
        type_url_list = []
        type_count = len(Data.pokemon_dict["types"])
        for i in range (type_count):
            type_entry = Data.pokemon_dict["types"][i]["type"]["name"]
            type_list.append(type_entry.title())
            url_entry = Data.pokemon_dict["types"][i]["type"]["url"]
            type_url_list.append(url_entry)
        self.types = type_list
        self.type_urls = type_url_list
        
        #Type Advantages and Disadvantages
        self.ddf = []
        self.ddt = []
        self.hdf = []
        self.hdt = []
        self.ndf = []
        self.ndt = []
        for i in range (len(self.type_urls)):
            response = requests.get (self.type_urls[i])
            self.data = response.json()
            double_damage_from_list = []
            double_damage_to_list = []
            half_damage_from_list =[]
            half_damage_to_list = []
            no_damage_from_list = []
            no_damage_to_list = []

            for  i in range (len(self.data["damage_relations"]["double_damage_from"])):
                type_damage_info = self.data["damage_relations"]["double_damage_from"][i]["name"]
                double_damage_from_list.append(type_damage_info)
            if double_damage_from_list:
                self.ddf.append(double_damage_from_list)
            else:
                double_damage_from_list.append("None")
                self.ddf.append(double_damage_from_list)
                    
            for  i in range (len(self.data["damage_relations"]["double_damage_to"])):
                type_damage_info = self.data["damage_relations"]["double_damage_to"][i]["name"]
                double_damage_to_list.append(type_damage_info)
            if double_damage_to_list:
                self.ddt.append(double_damage_to_list)
            else:
                double_damage_to_list.append("None")
                self.ddt.append(double_damage_to_list)  
            for  i in range (len(self.data["damage_relations"]["half_damage_from"])):
                type_damage_info = self.data["damage_relations"]["half_damage_from"][i]["name"]
                half_damage_from_list.append(type_damage_info)
            if half_damage_from_list:
                self.hdf.append(half_damage_from_list)
            else:
                half_damage_from_list.append("None")
                self.hdf.append(half_damage_from_list)
                
            for  i in range (len(self.data["damage_relations"]["half_damage_to"])):
                type_damage_info = self.data["damage_relations"]["half_damage_to"][i]["name"]
                half_damage_to_list.append(type_damage_info)
            if half_damage_to_list:
                self.hdt.append(half_damage_to_list)
            else:
                half_damage_to_list.append("None")
                self.hdt.append(half_damage_to_list)
            
            for i in range (len(self.data["damage_relations"]["no_damage_from"])):
                type_damage_info = self.data["damage_relations"]["no_damage_from"][i]["name"]
                no_damage_from_list.append(type_damage_info)
            if no_damage_from_list:
                self.ndf.append(no_damage_from_list)
            else:
                no_damage_from_list.append("None")
                self.ndf.append(no_damage_from_list)
                        
            for i in range (len(self.data["damage_relations"]["no_damage_to"])):
                    type_damage_info = self.data["damage_relations"]["no_damage_to"][i]["name"]
                    no_damage_to_list.append(type_damage_info)
            if no_damage_to_list:
                self.ndt.append(no_damage_to_list)
            else:
                no_damage_to_list.append("None")
                self.ndt.append(no_damage_to_list)

    
    #Summary, ID, Genus, Evolves From
    def misc_info(self):            
        self.national_number = Data.pokemon_dict["id"]
        Data.run_api(self,"pokemon-species", self.national_number)
        try:
            self.evolves_from = self.data["evolves_from_species"]["name"]
            self.evolves_from = self.data["evolves_from_species"]["name"].title()
            self.evolves_button.setText(self.evolves_from)
            self.evolves_button.setHidden(False)
        except TypeError:
            self.evolves_button.setHidden(True)
            
        self.genus = []
        self.summary = []
        
        genus_entries = self.data["genera"]
        for entry in genus_entries:
            if entry["language"]["name"] == 'en':
                self.genus.append(entry["genus"])
        summary_entries = self.data["flavor_text_entries"]
        for info in summary_entries:
            if info["language"]["name"] == 'en':
                self.summary.append(info["flavor_text"])
        self.summary = choice(self.summary)


    #Pokémon Attacks   
    def attacks (self):
        self.attacks = []
        self.methods = []
        
        #Level Up
        self.method_levelup_count = []
        self.attacks_levelup = []
        self.attacks_levelup_name = []
        self.attacks_levelup_url = []
        self.level_learned = []
        
        self.method_tutor_count = []
        self.method_machine_count = []
        self.method_etc_count = []
        
        all_attacks = Data.pokemon_dict["moves"]
        if all_attacks:
            for name in all_attacks:
                self.attacks.append(name["move"])
        else:
            self.attacks.append("None")

        
        all_methods = Data.pokemon_dict["moves"]
        
        #Determine the learn method of each entry in list
        count = -1
        for method in all_methods:
            self.methods.append(method["version_group_details"][-1])
        for m in self.methods:
            count += 1
            if m["move_learn_method"]["name"] == 'level-up':
                self.method_levelup_count.append(count)
        count = -1

        #Retrieving Level-Up Learned Attacks Info
        for entry in self.method_levelup_count:
            self.attacks_levelup.append(self.attacks[entry])
        for info in self.attacks_levelup:
            self.attacks_levelup_name.append(info["name"].title())
            self.attacks_levelup_url.append(info["url"])
        for level in self.method_levelup_count:
            self.level_learned.append(self.methods[level]["level_learned_at"])
        
        alu_effects_list = []
        alu_overview_list = []
        
        for url in self.attacks_levelup_url:
            response = requests.get(url)
            self.data = response.json()
            effect_entries = self.data["effect_entries"]
            for effect in effect_entries:  # effect is a dict
                if effect["language"]["name"] == 'en':
                    alu_effects_list.append(effect["short_effect"])
                    break                
            self.attack_levelup_effects = alu_effects_list
            overview_entries = self.data["flavor_text_entries"]
            en_overview_entries_2 = []
            for x in overview_entries:
                if x["language"]["name"] == 'en':
                    en_overview_entries_2.append(x)
            alu_overview_list.append(en_overview_entries_2[-1]["flavor_text"])
        self.attacks_levelup_overview_list = alu_overview_list
        if self.attacks[0] == "None":
            self.attacks_levelup = []
            self.attacks_levelup.append("Pokéapi has yet to enter this Pokémon's move list.")

    #Creates attack summary and orders the list
    def create_attack_summary_list(self):
        attack_summary = []
        for i in range (len(self.attacks_levelup_name)):
            attack_summary.append(f"{self.attacks_levelup_name[i]}: {self.attacks_levelup_overview_list[i]} Learned at Level {self.level_learned[i]}.")

        order = []
        self.attack_summary = []


        for i in range (len(attack_summary)): 
            x = i
            sentence = str(attack_summary[i])
            pattern =  r'Learned at Level \d+'
            matches = re.findall(pattern, sentence)
            m = str(matches)
            number = re.findall('[0-9]+', m)
            number = int(number[0])

            if len(order) == 0:
                order.append(number)
                self.attack_summary.append(attack_summary[0])
            else:
                for i in range (len(order)):
                    if number >= order[i]:
                        order.insert(i, number)
                        self.attack_summary.insert(i,attack_summary[x])
                        break
        self.attack_summary.reverse()

    #Pokemon's Sprites 
    def find_sprites(self):
        self.animated_sprites = []
        self.sprite_sheet = []
        sprite_generations = []
        sprite_numbers = []
        all_sprites = []
        games_per_generation = []
        self.animated_sprites = []
        
        self.all_sprites = Data.pokemon_dict["sprites"]
        all_version_sprites = self.all_sprites["versions"]
        for generations in all_version_sprites:
            sprite_generations.append(all_version_sprites[generations])
        for i in range (len(sprite_generations)):
            games_per_generation.append(len(sprite_generations[i]))
            all_sprites.append(sprite_generations[i])
        for x in range (len(games_per_generation)):
            for g in sprite_generations[x]:
                try:
                    self.animated_sprites.append(sprite_generations[x][g]["animated"]["front_default"])
                except:
                    pass
                    
        self.static_sprite = self.all_sprites['other']['official-artwork']['front_default']
                    
    def show_sprites(self):
        if self.animated_sprites[0] == None:
            self.pokemon_gif_screen.hide()
        else:
            self.movie.stop()
            self.request = Data.getRequest(self)
            self.request.setUrl(QUrl(self.animated_sprites[0]))
            reply = self.manager.get(self.request)
            self.movie.setDevice(reply)
            reply.finished.connect(self.movie.start)
            self.pokemon_gif_screen.show()

            
        url_image = requests.get(self.static_sprite)
        image = QImage()
        image.loadFromData(url_image.content)
        image_final = QPixmap(image)
        image_final = image_final.scaledToHeight(190)
        self.pokemon_image_screen.setPixmap(image_final)

        
    def getRequest(self):
        return QtNetwork.QNetworkRequest()   
        
        

app = QApplication(sys.argv) 
ex = MainWindow()        
code = app.exec()
sys.exit(code)


