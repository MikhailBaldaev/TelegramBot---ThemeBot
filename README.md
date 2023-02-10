## TelegramBot---ThemeBot

This is a script that uses the Telethon and Pymorphy3 libraries to extract the most common words from a given Telegram channel and returns the top 10 most normolized common words.

The idea of the script: to determine the main theme of the given Telegram channel.
In plans: convert script into a Telegram Bot and add search among comments on the channel.

[![Python](https://img.shields.io/static/v1?label=Python&message=https://www.python.org/&color=9cf&style=social&logo=python)](https://www.python.org/)
[![Telegram API](https://img.shields.io/static/v1?label=Telegram%20API&message=https://telegram.org/&color=9cf&style=social&logo=telegram)](https://telegram.org/)
[![Telethon](https://img.shields.io/static/v1?label=Telethon&message=https://docs.telethon.dev/en/stable/&color=9cf&style=social)](https://docs.telethon.dev/en/stable)
[![Pymorphy3](https://img.shields.io/static/v1?label=Pymorphy3&message=https://pypi.org/project/pymorphy3/&color=9cf&style=social)](https://pypi.org/project/pymorphy3/)

## Usage

### Preparing phase
           
You need to add missing information in config.py in accordance with the following instruction => [Link to docs](https://arabic-telethon.readthedocs.io/en/stable/extra/basic/creating-a-client.html)

### The script

The scripts accepts link to the Telegram channel in the following format: 'https://t.me/bbcrussian'

The result is 10 normalized common words in the channel's last 100 posts:

![image](https://user-images.githubusercontent.com/105664613/218097150-9f1daca9-2d72-42fc-97c4-0826ee42722a.png)
