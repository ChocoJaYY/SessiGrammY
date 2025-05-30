<p align="center">
  <img src="https://i.imgur.com/x1eVYmP.png" width="800 alt="SessiGrammY logo" />
</p>

# 📱 SessiGrammY - A Powerful Telegram Session String Generator

Effortless session generation for Pyrogram & Telethon  
Securely generate session strings for use in Telegram bots or user automation scripts.


<p align="center">
  <img src="https://img.shields.io/badge/Telethon-Session-blue?style=for-the-badge&logo=telegram" />
  <img src="https://img.shields.io/badge/Pyrogram-Session-green?style=for-the-badge&logo=telegram" />
  <img src="https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python" />
</p>

> ⚠️ **WARNING:** Treat session strings like your **password**. If someone gets access to your session string, they have **full control of your Telegram account**. Keep it **safe and private**.

---

## 🖥️ Features

- Generate **session strings** for **Telethon** and **Pyrogram**.
- Automatically handles login, 2FA, and session saving.
- Saves the session string to a `.txt` file for future use. But I heavily suggest you to delete that file after use.
- Compatible with both libraries for maximum flexibility.

---

## 🚀 Installation

Clone this repository:

```bash
git clone https://github.com/ChocoJaYY/SessiGrammY.git
cd SessiGrammY
```

Create a virtual environment (Optional, but recommended):
 ```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 How to Get API ID & API Hash

1. Visit [https://my.telegram.org](https://my.telegram.org).
2. Log in with your Telegram phone number.
3. Click on **API Development Tools**.
4. Fill in the required fields:
   - **App title**: Choose any name.
   - **Short name**: Choose a short identifier.
5. Click **Create application**.
6. You will now see your **API ID** and **API Hash**. Save them securely.

> ⚠️ **If the app creation fails and a popup appears**, try using a **mobile device**. Telegram sometimes blocks API creation from desktops for unknown reasons. I really dont know why :-( .

---

## ⚙️ Usage

Run the script:

```bash
python SessiGrammY.py
```

You'll see:

```
Choose session type to generate:
1. Telethon
2. Pyrogram
```

1. Select your preferred client.
2. Enter your:
   - API ID
   - API Hash
   - Phone number (with country code)
3. Enter the verification code you receive.
4. If you have 2FA enabled, enter your Telegram password.
5. Your session string will be printed and saved to a text file.

---

## 🔐 Keep Your Session String Safe!

Your session string is **as powerful as your password**. It allows **full access to your account**, including:
- Sending messages
- Reading messages
- Accessing all your groups, channels, and private chats

If you **share your session string**, you are **giving away your full account access**.

### 🔒 Tips to Keep it Safe:
- Never share your session string publicly.
- Do not upload it to GitHub or any cloud storage.
- Regenerate a session string if you suspect it was leaked.

---

## 🙏 Credits
[Telethon](https://github.com/LonamiWebs/Telethon)

[Pyrogram("TelegramPlayground" since original project abandoned)](https://github.com/TelegramPlayground/pyrogram)

Created by [ChocoJaYY](https://github.com/ChocoJaYY)  
Inspired by the need for secure, easy, and multi-library session management.

---

## 📄 License

This project is open-source and free to use under the MIT License.
