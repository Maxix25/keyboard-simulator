import os
numbers = [11,13,15,19,1,3,5,7,9]
current_number = 1
for number in numbers:
    os.rename(f"alt({number}).mp3", f"alt_up{current_number}.mp3")
    current_number += 1
