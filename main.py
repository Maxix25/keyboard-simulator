import os
from random import choice
from pynput import keyboard
from pynput.keyboard import Key
from play_sound import PlaySound
from sounds import *
sound_path = __file__[:-7] + f"/{sound_name}/"


def on_press(key):
	if key == Key.space or key == Key.backspace:
		sound = choice(space_down_sounds)
		sound_type = "space/down/"
	elif key == Key.alt or key == Key.ctrl or key == Key.esc or key == Key.alt_r or key == Key.tab:
		sound = choice(alt_down_sounds)
		sound_type = "alt/down/"
	elif key == Key.enter:
		sound = choice(enter_down_sounds)
		sound_type = "enter/down/"
	else:
		sound = choice(alpha_down_sounds)
		sound_type = "alpha/down/"
	PlaySound(sound_path + sound_type + sound, volume).start()
def on_release(key):
	if key == Key.space or key == Key.backspace:
		sound = choice(space_up_sounds)
		sound_type = "space/up/"
	if key == Key.alt or key == Key.ctrl:
		sound = choice(alt_up_sounds)
		sound_type = "alt/up/"
	elif key == Key.enter:
		sound = choice(enter_up_sounds)
		sound_type = "enter/up/"
	else:
		sound = choice(alpha_up_sounds)
		sound_type = "alpha/up/"
	PlaySound(sound_path + sound_type + sound, volume).start()
print("Ready!")
# Collect events until released
with keyboard.Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()
