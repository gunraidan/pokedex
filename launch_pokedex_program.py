#Built-in Modules
import os
import sys
import requests
import threading
from random import choice

#User-defined Modules
from modules import*

#Audio Modules
from pygame import mixer
import playsound

#PyQt6 Modules
from PyQt6 import QtNetwork
from PyQt6.QtGui import*
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import*
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QTimer, QUrl

#Global Variables
path= os.path.dirname(__file__)
start = str(path)
start = start.replace("\\", "/")
directory = "/modules/assets/"

#Audio Variable
sound_cut = False

#GUI        
class MainWindow(QWidget):
#Slots/Signals
    ability_get = pyqtSignal(name = 'abilityGet')
    artwork_get = pyqtSignal(name= 'artworkGet')
    attack_get = pyqtSignal(name = 'attackGet')
    gif_get = pyqtSignal(name= 'gifGet')
    type_get = pyqtSignal(name= 'typeGet')

#GUI - Builds GUI
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
        self.next_button()
        self.back_button()
        self.start_button()
        self.summary_button()
        self.type_button_1()
        self.type_button_2()
        self.user_input()
        self.stats()
        self.scrolling()
        self.evolves_from_button()
        self.mute_button()
        self.all_signals()
        self.manager = QtNetwork.QNetworkAccessManager()
        self.show()
    
    def mw_attributes(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top,self.width, self.height)
        self.setFixedSize(self.size())
        self.skin_screen_pixmap = QPixmap(f"{start}{directory}pokedexbgscreenoff.png")
        self.skin_screen_label = QLabel(self)
        self.skin_screen_label.setPixmap(self.skin_screen_pixmap)
        self.skin_screen_label.resize(self.skin_screen_pixmap.width(),self.skin_screen_pixmap.height())
        self.pokemon_image_screen = QLabel(self)
        self.pokemon_image_screen.setPixmap(QPixmap())
        self.pokemon_image_screen.setGeometry(45, -55, 472, 460)
        self.skin_case_pixmap = QPixmap(f"{start}{directory}pokedexbgcase.png")
        self.skin_case_label = QLabel(self)
        self.skin_case_label.setPixmap(self.skin_case_pixmap)
        self.skin_case_label.resize(self.skin_case_pixmap.width(),self.skin_case_pixmap.height())
        self.pokemon_gif_screen = QLabel("Label", self)
        self.movie = QMovie()
        self.movie.setCacheMode(QMovie.CacheMode.CacheAll)
        self.pokemon_gif_screen.setGeometry(320, -110, 472, 460)
        self.pokemon_gif_screen.setMovie(self.movie)
        self.borders_screen = QLabel(self)
        self.borders_screen.setPixmap(QPixmap())
        self.borders_screen.setGeometry(0, 0, 518, 654)
        
    def scaling(self):
        if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

        if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)       
        
    def scrolling(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.summary_screen)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedHeight(108)
        self.scroll_area.setFixedWidth(442)
        self.scroll_area.setStyleSheet("border: 0px" ";" "width:4px;" ";" "background-color: transparent")
        self.scroll_area.move(42, 502)
    
    #GUI - Info Labels
    def stats(self):
        font = "Tahoma"
        text_color = "DodgerBlue3"
        placeholder_text = ""
        
        self.error_screen = QLabel(placeholder_text, self)
        self.error_screen.setGeometry(105, 63, 330, 80)
        self.error_screen.setStyleSheet("color: red")
        self.error_screen.setFont(QFont('Arial',22))
        
        self.evolves_screen = QLabel (placeholder_text, self)
        self.evolves_screen.setGeometry(45, 438, 175, 65)
        self.evolves_screen.setStyleSheet(f"color: {text_color}")
        self.evolves_screen.setFont(QFont(font,13))
        
        self.genus_screen = QLabel (placeholder_text, self)
        self.genus_screen.setGeometry(34, 285, 215, 65)
        self.genus_screen.setStyleSheet(f"color: {text_color}")
        self.genus_screen.setFont(QFont(font,14))
        self.genus_screen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.height_screen = QLabel (placeholder_text, self)
        self.height_screen.setGeometry(45, 378, 125, 65)
        self.height_screen.setStyleSheet(f"color: {text_color}")
        self.height_screen.setFont(QFont(font,14))
        
        self.name_screen = QLabel (placeholder_text, self)
        self.name_screen.setGeometry(55, 238, 165, 65)
        self.name_screen.setStyleSheet(f"color: {text_color}")
        self.name_screen.setFont(QFont(font,14))
        self.name_screen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.number_screen = QLabel (placeholder_text, self)
        self.number_screen.setGeometry(45, 58, 105, 65)
        self.number_screen.setStyleSheet(f"color: {text_color}")
        self.number_screen.setFont(QFont(font,14))
        
        self.summary_screen = QLabel (placeholder_text, self)
        self.summary_screen.setGeometry(45, 463, 455, 180)
        self.summary_screen.setStyleSheet("color: black")
        self.summary_screen.setFont(QFont(font,14))
        self.summary_screen.setWordWrap(True)
        
        self.weight_screen = QLabel (placeholder_text, self)
        self.weight_screen.setGeometry(45, 400, 175, 65)
        self.weight_screen.setStyleSheet(f"color: {text_color}")
        self.weight_screen.setFont(QFont(font,14))    

#GUI - User Input
    def user_input(self):
        self.line = QLineEdit(self)
        self.line.setPlaceholderText("Enter Pokémon name/#...")
        self.line.setStyleSheet("QLineEdit" "{" "background:dark green""}" "QLineEdit" "{" "color:limegreen""}")
        self.line.setFont(QFont('Consolas',11))
        self.line.resize(182,32)
        self.line.move (280,22)           

#GUI - Buttons and Button actions
    def start_button(self):
        self.button_s = QPushButton(self)
        self.button_s.clicked.connect(self.start_button_click)        
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
        self.extract()

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
        self.next_button.setHidden(True)
        self.back_button.setHidden(True)
        self.get_summary_info()
        
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
        self.info_order = 0
        self.topic = "abilities"
        self.key_count = ability_module.abilities_count(self.pokemon_dict)
        self.ability_name = self.pokemon_dict["abilities"][0]['ability']['name'].toString()
        effects_url = self.pokemon_dict["abilities"][0]['ability']['url'].toString()
        self.ab_at_ty_site_request("abilities", effects_url)
        self.next_button.setHidden(False)
        self.back_button.setHidden(False)

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
        self.info_order = 0
        self.topic = "attacks"
        attack_module.attack_info(self,self.pokemon_dict)
        self.attack_name = self.attack_names[0]
        self.attack_url = self.url_list[0]
        self.level_learned = self.level_list[0]
        self.ab_at_ty_site_request("attacks", self.attack_url)
        self.next_button.setHidden(False)
        self.back_button.setHidden(False)
        
    def evolves_from_button(self):
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
        self.next_button.setHidden(True)
        self.back_button.setHidden(True)
        self.pokemon = self.evolves_name.lower()
        self.first_site_request()
        
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
        self.back_button.setHidden(False)
        self.info_order +=1
        if self.info_order == self.key_count:
            self.info_order = 0
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
        self.next_button.setHidden(False)
        self.info_order -=1
        if self.info_order == -1:
            self.info_order = self.key_count - 1
        self.button_click_action()
                    
    def button_click_action(self):
        if self.topic == "abilities":
            self.ability_name = self.pokemon_dict["abilities"][self.info_order]['ability']['name'].toString()
            effects_url = self.pokemon_dict["abilities"][self.info_order]['ability']['url'].toString() 
            self.ab_at_ty_site_request("abilities", effects_url)
        if self.topic == "attacks":
            self.attack_name = self.attack_names[self.info_order]
            self.attack_url = self.url_list[self.info_order]
            self.level_learned = self.level_list[self.info_order]
            self.ab_at_ty_site_request("attacks", self.attack_url)
        if self.topic == "types":
            type_module.type_info(self,self.types_dict,self.info_order)
            self.type_get.emit()
            
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
            sound_module.mute_off()
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
            sound_module.mute_on()
            sound_cut = True
            self.mute_button.setStyleSheet("QPushButton"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}mute_on.png)"
                               "}"
                               "QPushButton:pressed"
                               "{"
                               "background:transparent;"f"background-image : url({start}{directory}mute_off_p.png)"
                               "}")
            
    def type_button_1(self):
        self.type_button_first = QPushButton(self)
        self.type_button_first.clicked.connect(self.type_button_1_click)
        self.type_button_first.setStyleSheet("QPushButton""{""background:transparent;}")
        self.type_button_first.resize(48,48)
        self.type_button_first.move(80,332)        
        self.type_button_first.setHidden(True)    
            
    def type_button_2(self):
        self.type_button_second = QPushButton(self)
        self.type_button_second.clicked.connect(self.type_button_2_click)
        self.type_button_second.setStyleSheet("QPushButton""{""background:transparent;}")
        self.type_button_second.resize(48,48)
        self.type_button_second.move(136,332)   
        self.type_button_second.setHidden(True)         

    def type_button_1_click(self):
        self.key_count = 6
        self.info_order = 0
        self.topic = "types"
        self.ab_at_ty_site_request("types",type_module.type_url(self.pokemon_dict, 0).toString())
        self.next_button.setHidden(False)
        self.back_button.setHidden(False)

    def type_button_2_click(self):
        if self.type_2:
            self.key_count = 6
            self.info_order = 0
            self.topic = "types"
            self.ab_at_ty_site_request("types",type_module.type_url(self.pokemon_dict, 1).toString())
            self.next_button.setHidden(False)
            self.back_button.setHidden(False)

#Show all GUI objects after all info loads
    def show_all(self):
        self.abilities_button.setHidden(False)
        self.attacks_button.setHidden(False)
        self.summary_button.setHidden(False)
        self.type_button_first.setHidden(False)
        self.type_button_second.setHidden(False)
        self.name_screen.setText(self.pokemon_name)
        self.number_screen.setText(f"#{self.pokemon_id}")
        self.height_screen.setText(f"Height: {self.p_height}")
        self.weight_screen.setText(f"Weight: {self.p_weight} lbs")

#API - Initial QNAM request
    def first_site_request(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon}"
        req = QtNetwork.QNetworkRequest(QUrl(url))
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.first_handle_request)
        self.nam.get(req)
        
    def first_handle_request(self, reply):
            json2qt = QtCore.QJsonDocument.fromJson 
            er = reply.error()
            error_message = str(er)
            if er == QtNetwork.QNetworkReply.NetworkError.NoError:
                qbyte = reply.readAll()
                self.pokemon_dict = json2qt(qbyte)
                self.summary_site_request(self.pokemon_dict["species"]["url"].toString())
                self.basic_info_get()
                self.type_button_change()
                self.artwork_get.emit()
                self.gif_get.emit()
                self.skin_screen_label.setPixmap(QPixmap(f"{start}{directory}pokedexbgscreenon.png"))
                self.borders_screen.setPixmap(QPixmap(f"{start}{directory}foreground.png"))
                self.show_all()
                threading.Thread(target=sound_module.confirmed_sound).start()
            else:
                if error_message == "NetworkError.ContentNotFoundError":
                    self.run_not_in_database_error()
                else:
                    self.run_common_error()
                    print(reply.errorString())

#API - QNAM request for abilities, attacks, and types
    def ab_at_ty_site_request(self,which,new_url):
        self.which_aat = which
        req = QtNetwork.QNetworkRequest(QUrl(new_url))
        self.nam_aat = QtNetwork.QNetworkAccessManager()
        self.nam_aat.finished.connect(self.ab_at_ty_handle_request)
        self.nam_aat.get(req)
        
    def ab_at_ty_handle_request(self,reply):
            json2qt = QtCore.QJsonDocument.fromJson 
            er = reply.error()
            if er == QtNetwork.QNetworkReply.NetworkError.NoError:
                if self.which_aat == "abilities":
                    qbyte = reply.readAll()
                    self.abilities_dict = json2qt(qbyte)
                    self.ability_get.emit()                   
                if self.which_aat == "attacks":
                    qbyte = reply.readAll()
                    self.attacks_dict = json2qt(qbyte)
                    self.attack_get.emit()
                if self.which_aat == "types":
                    qbyte = reply.readAll()
                    self.types_dict = json2qt(qbyte)
                    type_module.type_info(self, self.types_dict, self.info_order)
                    self.type_get.emit()
            else:
                self.run_common_error()  
                print(reply.errorString())

#API - QNAM request for summary
    def summary_site_request(self, new_url):
        req = QtNetwork.QNetworkRequest(QUrl(new_url))
        self.nam_sum = QtNetwork.QNetworkAccessManager()
        self.nam_sum.finished.connect(self.summary_handle_request)
        self.nam_sum.get(req)
        
    def summary_handle_request(self, reply):
            json2qt = QtCore.QJsonDocument.fromJson 
            er = reply.error()
            if er == QtNetwork.QNetworkReply.NetworkError.NoError:
                qbyte = reply.readAll()
                self.summary_dict = json2qt(qbyte)
                self.get_summary_info()
                self.genus_print()
                self.evolves_print()
            else:
                self.run_common_error()
                print(reply.errorString())
                
#Type button changes
    def type_button_change(self):
        self.type_1 = type_module.type_name(self.pokemon_dict, 0).toString().title()
        try:
            type_module.types[self.type_1]
        except:
            type_1 = "Not Found"
        self.type_button_update("first",type_module.types[self.type_1], type_module.types_hover[self.type_1], type_module.types_press[self.type_1])
        
        if (type_module.type_count(self.pokemon_dict)) > 1:
            self.type_2 = type_module.type_name(self.pokemon_dict, 1).toString().title()
            try:
                type_module.types[self.type_2]
            except:
                self.type_2 = "Not Found"
            self.type_button_update("second",type_module.types[self.type_2], type_module.types_hover[self.type_2], type_module.types_press[self.type_2])
        else:
            self.type_button_update("second","","","")
            self.type_2 = False
            
    def type_button_update(self, which, default, hover, press):
        if which == "first":
            var_button = self.type_button_first
        else:
            var_button = self.type_button_second
        var_button.setStyleSheet("QPushButton"
                            "{"
                            "background:transparent;"f"background-image : url({default})"
                            "}"
                            "QPushButton:hover"
                            "{"
                            "background:transparent;"f"background-image : url({hover})"
                            "}"
                            "QPushButton:pressed"
                            "{"
                            "background:transparent;"f"background-image : url({press})"
                            "}")

#Run functions from modules and display them in GUI
    def abilities_print(self):
        ability_module.ability_effect_info(self,self.abilities_dict)
        text_updates.transform(self.full_ability)
        text_updates.paste_info( "", self.summary_screen.setText)   

    def attacks_print(self):
        attack_module.attack_summary_info(self,self.attacks_dict)
        text_updates.transform(self.full_attack)
        text_updates.paste_info( "", self.summary_screen.setText)

    def basic_info_get(self):
        self.pokemon_name = self.pokemon_dict["forms"][0]["name"].toString().title()
        self.pokemon_id = str(misc_module.basic_info_id(self.pokemon_dict).toInt())
        self.p_height = height_weight_module.get_height(self.pokemon_dict["height"])
        self.p_weight = height_weight_module.get_weight(self.pokemon_dict["weight"])

    def evolves_print(self):
        self.evolves_button.setHidden(True)
        self.evolves_screen.setText("")
        self.evolves_name = misc_module.evolves_name(self.summary_dict)
        self.evolves_button.setText(self.evolves_name.title())
        if len(self.evolves_name) != 0:
            self.evolves_screen.setText("Evolves\n From:")
            self.evolves_button.setHidden(False)

    def genus_print(self):
        genus = misc_module.genus_info(self.summary_dict)
        text_updates.transform(genus)
        text_updates.paste_info( "", self.genus_screen.setText)  

    def type_print(self):
        self.full_type = (f"{self.damage_measure}: {self.type_name_list}")
        text_updates.transform(self.full_type)
        text_updates.paste_info( "", self.summary_screen.setText)
        
    def get_summary_info(self):
        self.summary = misc_module.summary_info(self.summary_dict["flavor_text_entries"], "language","name", "flavor_text")
        text_updates.transform(self.summary)
        text_updates.paste_info( "", self.summary_screen.setText)


#Display images of Pokémon
    def show_artwork(self):           
        url_image = misc_module.sprite_find_official(self.pokemon_dict)
        if len(url_image) == 0:
            self.pokemon_image_screen.hide()
        else:
            image = QImage()
            image.loadFromData(requests.get(url_image).content)
            self.pokemon_image_screen.setPixmap(QPixmap(image.scaledToHeight(190)))
            self.pokemon_image_screen.show()
    
    def show_gif(self):
        url_image = misc_module.sprite_find_animated(self.pokemon_dict)
        if len(url_image) == 0:
            self.pokemon_gif_screen.hide()
        else:
            self.movie.stop()
            self.request = QtNetwork.QNetworkRequest() 
            self.request.setUrl(QUrl(url_image))
            reply = self.manager.get(self.request)
            self.movie.setDevice(reply)
            reply.finished.connect(self.movie.start)        
            self.pokemon_gif_screen.show()       

#Activate all signals
    def all_signals(self):
        self.abilityGet.connect(self.abilities_print)
        self.artworkGet.connect(self.show_artwork)
        self.attackGet.connect(self.attacks_print)
        self.gifGet.connect(self.show_gif)
        self.typeGet.connect(self.type_print)
    
#Error Messages and Sound
    def run_not_in_database_error(self):
        self.error_screen.setHidden(False)
        self.error_screen.setText("No Pokémon in Database. Check Entry.")
        threading.Thread(target=sound_module.error_sound).start()
        QTimer.singleShot(4000, lambda: self.error_screen.setHidden(True))
        
    def run_common_error(self):
        self.error_screen.setHidden(False)
        self.error_screen.setText("Issue with Database. Try Again Later.")
        threading.Thread(target=sound_module.error_sound).start()
        QTimer.singleShot(4000, lambda: self.error_screen.setHidden(True))

#The "Mother Code" Run        
    def extract(self):
        self.next_button.setHidden(True)
        self.back_button.setHidden(True)
        self.pokemon = self.line.text().lower().lstrip('0').strip()
        self.first_site_request()

#Main Thread                
if __name__ == '__main__':  
    threading.Thread(target=sound_module.music, daemon = True).start()
    app = QApplication(sys.argv) 
    ex = MainWindow()        
    code = app.exec()
    sys.exit(code)
