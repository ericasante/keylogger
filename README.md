# keylogger
A simple Python example that logs key presses to a file.

## How to run
1. Install the required package:
   ```bash
   pip install pynput
   ```
2. Run the script:
   ```bash
   python keylogger.py
   ```
3. Press `Esc` to stop the program.

## What it does
- Listens for keyboard input
- Saves each key press to `key_log.txt`
- Stops when you press `Esc`

## Important notes
- Use this code only for learning and on your own computer.
- Do not capture other people's keystrokes without permission.

## Alternative example
If you want to see the keys printed on the screen instead of saved to a file,
use `keylogger_terminal.py`:
```bash
python keylogger_terminal.py
```
