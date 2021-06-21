# sound_name = "sp_cmxb_mp3"
import os
print(__file__)
sound_name = "sp_cmxb_mp3"
if sound_name == "sp_cmxb_mp3":
	volume = "0.13"
else:
	volume = "0.5"
alpha_down_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/alpha/down")
alpha_up_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/alpha/up")
space_down_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/space/down")
space_up_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/space/up")
alt_down_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/alt/down")
alt_up_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/alt/up")
enter_down_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/enter/down")
enter_up_sounds = os.listdir(__file__[:-9] + f"/{sound_name}/enter/up")
# ABSOLUTE PATH LISTS
'''
alpha_down_sounds_abs = []
alpha_up_sounds_abs = []
space_down_sounds_abs = []
space_up_sounds_abs = []
alt_down_sounds_abs = []
alt_up_sounds_abs = []
enter_down_sounds_abs = []
enter_up_sounds_abs = []
for sound in alpha_down_sounds:
	alpha_down_sounds_abs.append(os.path.abspath(sound))
for sound in alpha_up_sounds:
	alpha_up_sounds_abs.append(os.path.abspath(sound))
for sound in space_down_sounds:
	space_down_sounds_abs.append(os.path.abspath(sound))
for sound in space_up_sounds:
	space_up_sounds_abs.append(os.path.abspath(sound))
for sound in alt_down_sounds:
	alt_down_sounds_abs.append(os.path.abspath(sound))
for sound in alt_up_sounds:
	alt_up_sounds_abs.append(os.path.abspath(sound))
for sound in enter_down_sounds:
	enter_down_sounds_abs.append(os.path.abspath(sound))
for sound in enter_up_sounds:
	enter_up_sounds_abs.append(os.path.abspath(sound))
print(alpha_down_sounds_abs)





sound_name = "sp_cmxb_mp3"
sound_extension = "mp3"
if sound_name == "sp_gatinkred":
	volume = "0.3"
elif sound_name == "sp_cmxb_mp3":
	volume = "0.09"
else:
	volume = "1"

alpha_down1 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/down/alpha_down1.{sound_extension}"
alpha_down2 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/down/alpha_down2.{sound_extension}"
alpha_down3 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/down/alpha_down3.{sound_extension}"
alpha_down4 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/down/alpha_down4.{sound_extension}"
alpha_down5 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/down/alpha_down5.{sound_extension}"
alpha_down6 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/down/alpha_down6.{sound_extension}"
alpha_down7 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/down/alpha_down7.{sound_extension}"
alpha_down8 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/down/alpha_down8.{sound_extension}"
# Up sounds
alpha_up1 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up1.{sound_extension}"
alpha_up2 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up2.{sound_extension}"
alpha_up3 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up3.{sound_extension}"
alpha_up4 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up4.{sound_extension}"
alpha_up5 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up5.{sound_extension}"
alpha_up6 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up6.{sound_extension}"
alpha_up7 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up7.{sound_extension}"
alpha_up8 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up8.{sound_extension}"
alpha_up9 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alpha/up/alpha_up9.{sound_extension}"
# Space down
space_down1 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/down/space_down1.{sound_extension}"
space_down2 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/down/space_down2.{sound_extension}"
space_down3 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/down/space_down3.{sound_extension}"
space_down4 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/down/space_down4.{sound_extension}"
space_down5 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/down/space_down5.{sound_extension}"
space_down6 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/down/space_down6.{sound_extension}"
space_down7 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/down/space_down7.{sound_extension}"
space_down8 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/down/space_down8.{sound_extension}"
# Space up
space_up1 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/up/space_up1.{sound_extension}"
space_up2 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/up/space_up2.{sound_extension}"
space_up3 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/up/space_up3.{sound_extension}"
space_up4 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/up/space_up4.{sound_extension}"
space_up5 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/up/space_up5.{sound_extension}"
space_up6 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/up/space_up6.{sound_extension}"
space_up7 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/up/space_up7.{sound_extension}"
space_up8 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/space/up/space_up8.{sound_extension}"
# Alt down
alt_down1 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alt/down/alt_down1.{sound_extension}"
alt_down2 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alt/down/alt_down2.{sound_extension}"
alt_down3 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alt/down/alt_down3.{sound_extension}"
alt_down4 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alt/down/alt_down4.{sound_extension}"
# Alt up
alt_up1 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alt/up/alt_up1.{sound_extension}"
alt_up2 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alt/up/alt_up2.{sound_extension}"
alt_up3 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alt/up/alt_up3.{sound_extension}"
alt_up4 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/alt/up/alt_up4.{sound_extension}"
# Enter down
enter_down1 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/down/enter_down1.{sound_extension}"
enter_down2 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/down/enter_down2.{sound_extension}"
enter_down3 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/down/enter_down3.{sound_extension}"
enter_down4 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/down/enter_down4.{sound_extension}"
enter_down5 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/down/enter_down5.{sound_extension}"
# Enter Up
enter_up1 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/up/enter_up1.{sound_extension}"
enter_up2 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/up/enter_up2.{sound_extension}"
enter_up3 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/up/enter_up3.{sound_extension}"
enter_up4 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/up/enter_up4.{sound_extension}"
enter_up5 = f"/home/maxi/Documents/keyboard-simulator/{sound_name}/enter/up/enter_up5.{sound_extension}"
'''
