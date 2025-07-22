# Encrypted Keylogger
This project is a Python-based encrypted keylogger built for educational purposes.

## 📌 Project Overview

A **keylogger** is a type of surveillance software or malware designed to record every keystroke made on a system. This project demonstrates how keyloggers work and includes functionality for:

- Logging keystrokes
- Encrypting the logs
- Decrypting the logs for review
- Safely terminating with the `ESC` key

⚠️ **Note:** This project is strictly for learning and ethical use only. Do not use it on any system without explicit permission.

---

## 📊 Functional Flow

1. The script starts and displays a message indicating it is active.
2. Generates a secure encryption key.
3. Listens for user keystrokes using the `pynput` library.
4. Logs:
   - Normal characters as typed.
   - Special keys (e.g. `Enter`, `Space`) with labels.
5. Saves:
   - Encrypted data → `log_encrypted.txt`
   - Decrypted, readable data with timestamps → `log_decrypted.txt`
6. Stops logging on pressing `ESC`.

---

## 🖥️ Output Files

- `log_encrypted.txt` — Contains encrypted keystroke logs.
- `log_decrypted.txt` — Contains human-readable logs with timestamps.

---

## 📁 Project Structure


├── keylogger.py              # Main script
├── key.key                   # AES encryption key
├── log_encrypted.txt         # Encrypted keystrokes
├── log_decrypted.txt         # Readable keystrokes with timestamps
├── README.md                 # This file

---

## 🧰 Dependencies

Make sure to install the required Python packages:

```bash
pip install pynput cryptography
```

---

## ▶️ How to Run

```bash
python keylogger.py
```
To stop the logger, press the ESC key.
