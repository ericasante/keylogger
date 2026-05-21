"""
Simple keypress printer example for learning purposes.

This script listens for keyboard events and prints the keys pressed
directly to the terminal. It does not save keystrokes to a file.

Important: Use this code only on your own computer for learning.
"""

from pynput import keyboard


def on_press(key):
    """Called when a key is pressed."""
    try:
        # Normal keys like letters and numbers have a char value.
        print(f"Key pressed: {key.char}")
    except AttributeError:
        # Special keys like space, enter, and shift use names.
        print(f"Special key pressed: <{key.name}>")


def on_release(key):
    """Called when a key is released."""
    if key == keyboard.Key.esc:
        print("Escape pressed, stopping listener.")
        return False


if __name__ == "__main__":
    print("Starting terminal-only key listener. Press Esc to stop.")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
