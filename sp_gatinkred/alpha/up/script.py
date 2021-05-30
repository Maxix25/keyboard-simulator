import os
numbers = [10,12,13,15,17,19,20,22,24,26,29,31,34,36,38,43,45,4,6,8]
current_number = 1
for number in numbers:
    os.rename(f"alpha({number}).mp3", f"alpha_up{current_number}.mp3")
    current_number += 1
