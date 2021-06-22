# sound_name = "sp_cmxb_mp3"
import os
from argparse import ArgumentParser
parser = ArgumentParser(description = "Simulate the sounds of a mechanical keyboard using a simple command line interface!")
parser.add_argument("-s", "--sound", help = "Sound to reproduce when a key is pressed")
parser.add_argument("-v", "--volume", help = "Volume to play the sound, default is 0.5")
args = parser.parse_args()
if args.sound:
	sound_name = args.sound
else:
	sound_name = "sp_green"
if args.volume:
	volume = args.volume
else:
	volume = "0.5"
if sound_name == "sp_cmxb_mp3":
	volume = "0.13"
try:
	alpha_down_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/alpha/down")
	alpha_up_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/alpha/up")
	space_down_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/space/down")
	space_up_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/space/up")
	alt_down_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/alt/down")
	alt_up_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/alt/up")
	enter_down_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/enter/down")
	enter_up_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/enter/up")
except FileNotFoundError:
	print("The sound name you specified isn't valid, please double check the name entered")
	exit()
