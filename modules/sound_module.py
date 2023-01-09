#Modules
import os
import time
from pygame import mixer
from playsound import playsound

#Global Variables
path= os.path.dirname(__file__)
start = str(path)
start = start.replace("\\", "/")
directory = "/sounds/"

#Audio Variable
sound_cut = False

#Initializes the PyGame Mixer
mixer.init()
def play_music(mp3):
    song = f"{start}{directory}{mp3}"
    mixer.music.load(song)
    if sound_cut:
        mixer.music.set_volume(0)
    else:
        mixer.music.set_volume(.5)
    mixer.music.play()
    
#Plays main song    
def music():
    time.sleep(.6)
    play_music("pokemonthemestart.mp3")
    time.sleep(47.5)
    while True:
        play_music("pokemonthemeloop.mp3")
        time.sleep(43.1)

#Plays sounds           
def error_sound():
    playsound(f"{start}{directory}pokemonerror.mp3")
    
def confirmed_sound():
    playsound(f"{start}{directory}pokemonconfirmed.mp3")
    
def limit_sound():
    playsound(f"{start}{directory}pokemonlimit.mp3")

#Changes Audio Variable to mute the upon loading song
def mute_on():
    global sound_cut
    sound_cut = True
    
def mute_off():
    global sound_cut
    sound_cut = False
