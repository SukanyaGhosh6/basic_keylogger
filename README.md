# basic_keylogger

Hey there!  
So, this little project was born purely out of my curiosity — I always wondered *how keyloggers actually work* behind all the scary cybersecurity talk.  
And here we are: **basic_keylogger** — a super simple Python script that quietly listens to your keystrokes and saves them into a local file.

No evil plans, just a mini hands-on adventure into how things happen under the hood!

---

## What is this?

In plain words:  
It’s a basic keylogger that records everything you type — letters, numbers, special keys — and writes it all into a neat little `keylog.txt` file sitting right beside the script.  
No pop-ups, no noise. Just simple, quiet logging.

---

## Why I built it?

Honestly?  
I wanted to *get my hands a little dirty* and really understand:
- How keylogging works at its core
- How keyboard events can be captured in Python
- What happens behind some of those cybersecurity tools (and threats) we hear about

Also, mini projects like this make learning feel way more real and exciting!

---

## How it works:

- Listens for every key you press.
- If it's a normal character (like `a`, `1`, or `z`), it logs it directly.
- If it's a special key (like `Space`, `Enter`, `Shift`), it wraps it in square brackets like `[Key.space]`.
- All your keypresses get stored in `keylog.txt`.

---

## How to run it

1. First, make sure you have Python installed on your system.
2. Open your terminal in VS Code (or wherever you're comfy).
3. Install the one and only package we need:
   ```bash
   pip install pynput
   ```
4. Then simply run:
   ```bash
   python basic_keylogger.py
   ```
5. Start typing... anywhere!  
   Meanwhile, your keystrokes are silently being recorded into `keylog.txt`.

(If you want to stop the script, just hit the STOP button in VS Code or press `Ctrl + C` in the terminal.)

---

## Important Note

This project is **strictly for educational and ethical purposes only**.  
Please don’t use this script on anyone else’s device or network without permission.  
The goal is to **learn** and **understand**, not to sneak around!

---

## Author

Made with curiosity by [SukanyaGhosh6](https://github.com/SukanyaGhosh6)  
Always learning, always exploring.

---

## Final Thoughts

Mini projects like this make me appreciate how simple ideas can grow into serious real-world tools — for better or worse.  
This was just one step into the fascinating world of cybersecurity.  
Many more steps (and many more curious nights) to come!

