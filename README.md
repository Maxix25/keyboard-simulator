# Keyboard Simulator

### What is this?
- This is a keyboard simulator built with python, every keystroke will play a cherry mx blue key sound
- This is based on the <a href="https://mechakeys.robolab.io/">MechaKeys</a> app sounds, but it doesn't contain a GUI, it's just a python executable file

### How to execute
  ### Linux
  - Download the source code on the <a href="https://github.com/Maxix25/keyboard-simulator/releases/" target="_blank">releases</a> page
  - Unzip the file and execute the main.py using ```python3 main.py -s [sp_namehere] -v [volume]```
  - Enjoy your app!
  ### Windows
  - On windows it's a bit different, download the source code on the <a href="https://github.com/Maxix25/keyboard-simulator/releases/" target="_blank">releases</a> page
  - Unzip the file
  - Edit the play_sound.py file line 16 ```cmd = 'play -v ' + self.volume + ' ' + self.filename``` and change it to ```cmd = 'play -v ' + self.volume + ' ' + self.filename + " -t waveaudio"```
  - Run the main.py file using ```python main.py -s [sp_namehere] -v [volume]```
  - Enjoy your app!

# Dependencies
### Pynput
  - To install pynput use ```pip3 install -r requirements.txt``` or ```pip3 install pynput```
### SOX
  - To install SOX on Linux use ```sudo pacman -S sox``` on Arch Linux, ```sudo apt install sox``` on Ubuntu, ```sudo dnf install sox``` on Fedora
### Credits
  - The sounds were grabbed from the <a href="https://mechakeys.robolab.io/">MechaKeys</a> app
  - The play_sound.py was grabbed from <a href="https://github.com/skkeeper/linux-clicky/blob/master/linux_clicky/play_sound.py">Linux Clicky</a>
