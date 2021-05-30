import os
numbers = [11,13,15,17,19,1,21,3,5,7,9]
current_number = 1
for number in numbers:
    os.rename(f"space({number}).mp3", f"space_up{current_number}.mp3")
    current_number += 1
