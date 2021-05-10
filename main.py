from random import choice
from pynput import keyboard
from pynput.keyboard import Key
from play_sound import PlaySound
from sounds import *

down_sounds = [alpha_down1, alpha_down2, alpha_down3, alpha_down4, alpha_down5, alpha_down6, alpha_down7, alpha_down8]
up_sounds = [alpha_up1, alpha_up2, alpha_up3, alpha_up4, alpha_up5, alpha_up6, alpha_up7, alpha_up8, alpha_up9]
space_down_sounds = [space_down1, space_down2, space_down3, space_down4, space_down5, space_down6, space_down7, space_down8]
space_up_sounds = [space_up1, space_up2, space_up3, space_up4, space_up5, space_up6, space_up7, space_up8]
alt_down_sounds = [alt_down1, alt_down2, alt_down3, alt_down4]
alt_up_sounds = [alt_up1, alt_up2, alt_up3, alt_up4]
enter_down_sounds = [enter_down1, enter_down2, enter_down3, enter_down4, enter_down5]
enter_up_sounds = [enter_up1, enter_up2, enter_up3, enter_up4, enter_up5]
print("Now ready")

def on_press(key):
	if key == Key.space:
		sound = choice(space_down_sounds)
	elif key == Key.alt:
		sound = choice(alt_down_sounds)
	elif key == Key.enter:
		sound = choice(enter_down_sounds)
	else:
		sound = choice(down_sounds)
	PlaySound(sound, "0.2").start()
def on_release(key):
	if key == Key.space:
		sound = choice(space_up_sounds)
	if key == Key.alt:
		sound = choice(alt_up_sounds)
	elif key == Key.enter:
		sound = choice(enter_up_sounds)
	else:
		sound = choice(up_sounds)
	PlaySound(sound, "0.2").start()

# Collect events until released
with keyboard.Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()
