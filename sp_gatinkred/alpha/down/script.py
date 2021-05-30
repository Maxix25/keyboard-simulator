import os
numbers = [11,14,16,1,21,23,25,27,30,32,33,35,37,39,3,40,42,44,5,7,9]
current_number = 1
for number in numbers:
    os.rename(f"alpha({number}).mp3", f"alpha_down{current_number}.mp3")
    current_number += 1

