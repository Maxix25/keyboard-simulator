import os
numbers = [11,13,15,17,19,1,21,23,3,5,7]
current_number = 1
for number in numbers:
    os.rename(f"enter({number}).mp3", f"enter_up{current_number}.mp3")
    current_number += 1
