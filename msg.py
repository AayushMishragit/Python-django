import pywhatkit
import pyautogui
import time

# 2-second delay before opening WhatsApp
time.sleep(1)

pywhatkit.sendwhatmsg_instantly("+91 90393 02613", "hello scripted msg",tab_close=False,)

# WhatsApp Web ko type karne ka time dene ke liye thoda wait
time.sleep(4)

# Auto-enter to send the message and you done🤍
pyautogui.press("enter")
print("Message sent successfully!")
#final project completed

