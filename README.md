![upl](https://user-images.githubusercontent.com/82133365/211179823-4cc45781-a49c-4dfa-8868-784662c04a66.png)


## Contents
* [Description](#description)
* [Requirements](#requirements)
* [Initialization](#initialization)
* [Instructions](#instructions)

## Description:
Unofficial Pokédex is a Pokédex app that is coded in Python with a GUI powered by PyQt. It uses <a href="https://pokeapi.co">PokeApi</a> to retrieve all of the desired information about any specific Pokémon.
<br><br>
Below is how the program looks in action:
<br>
<img src="https://github.com/nkocodes/media/blob/main/unofficialpokedex/pokemonexample.gif" height="479">

## Requirements:
python 3.6+
<br>
playsound v1.2.2
<br>
pygame v2.1.2
<br>
PyQt6
<br>
requests v2.28.1

## Initialization:
To use the program, type the Pokémon's name or national number on the green screen by any method shown:
<br>
<img src="https://github.com/nkocodes/media/blob/main/unofficialpokedex/pokemoninputexample1.gif" height="80">
<br><br>
Once you are finished filling out the entry screen click on the yellow play button right beside it:
<br>
<img src="https://github.com/nkocodes/media/blob/main/unofficialpokedex/pokemoninputexample2.gif" height="86">
<br>
Be sure to only use letters and numbers and no special characters. Also be sure that the Pokémon's name is spelt correctly. Failure to adhere to these rules will result in the database not being able to find the Pokémon:
<br>
<img src="https://github.com/nkocodes/media/blob/main/unofficialpokedex/pokemoninputexample3.gif" height="210">

## Instructions:
<img src="https://github.com/nkocodes/media/blob/main/unofficialpokedex/pokedexinfo.png" height="620">
<br>
1. Clicking the "Start Button" retrieves the data of the desired Pokémon entered in the input screen and updates the entire screen.
<br><br>
2. The "Abilities Button" retrieves the ability name and explanation of the Pokémon and displays it on the bottom white screen. You can scroll back and forth through each abilitiy with the "Back" and "Next" buttons located to at the ends of the screen.
<br>
<img src="https://github.com/nkocodes/media/blob/main/unofficialpokedex/pokemonnextback.gif" height="102"> 
<br>
3. The "Attacks Button" retrieves the attack name and explanation of the Pokémon and displays it on the bottom white screen. Like the Abilities Button, you can scroll back and forth through each abilitiy with the "Back" and "Next" buttons located to at the ends of the screen.
<br>
<img src="https://github.com/nkocodes/media/blob/main/unofficialpokedex/pokemonnextback2.gif" height="102">
<br>
4. The home icon is the "Summary Button". It displays the summary of each Pokémon randomly selected from each game.
<br><br>
5. If a Pokémon's name appears here, it means that the "Evolves From Button" is active. Click on the Pokémon name to load and change the screen to information about the Pokémon listed.
<br><br>
6. The "Type Button" retrieves all of the strengths and weaknesses of the Pokémon's type. Similar to the Abilities and Attacks buttons, it is possible to scroll through the information with the next and back buttons on the screen the text is presented on. Each Pokémon has one or two types. So up to two Type buttons will be shown at a time.
<br><br>
7. If you don't want to hear the music, click the "Mute Button" to turn it off. If you would like the music back on, simply click the button again.
