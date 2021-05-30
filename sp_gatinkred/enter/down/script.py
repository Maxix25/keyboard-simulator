import os
numbers = [10,12,14,16,18,20,22,24,2,4,6,8]
current_number = 1
for number in numbers:
    os.rename(f"enter({number}).mp3", f"enter_down{current_number}.mp3")
    current_number += 1
