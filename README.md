# Keyboard Simulator
This is a keyboard simulator built with python, every keystroke will play a key sound

### How to execute
  ### Linux and MacOS
  - Download the source code on the <a href="https://github.com/Maxix25/keyboard-simulator/releases/" target="_blank">releases</a> page
  - Unzip the file and execute the main.py using ```python3 main.py```
  - Enjoy your app!
  ### Windows
  - On windows it's a bit different, download the source code on the <a href="https://github.com/Maxix25/keyboard-simulator/releases/" target="_blank">releases</a> page
  - Unzip the file
  - Edit the play_sound.py file line 16 ```cmd = 'play -v ' + self.volume + ' ' + self.filename``` and change it to ```cmd = 'play -v ' + self.volume + ' ' + self.filename + " -t waveaudio"```
  - Run the main.py file using ```python main.py```
  - Enjoy your app!
### Dependencies
  - The only dependency is <a href="https://pypi.org/project/pynput/" target="_blank">pynput</a>, which you can install it by using ```pip install -r requirements.txt``` or ```pip install pynput```
