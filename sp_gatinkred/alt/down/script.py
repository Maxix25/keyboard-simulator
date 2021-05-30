import os
numbers = [10,12,14,16,17,18,20,2,4,6,8]
current_number = 1
for number in numbers:
    os.rename(f"alt({number}).mp3", f"alt_down{current_number}.mp3")
    current_number += 1
