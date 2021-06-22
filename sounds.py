# sound_name = "sp_cmxb_mp3"
import os
sound_name = "sp_gatblk"
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
