import pywhatkit
import pyautogui
import time

# 2-second delay before opening WhatsApp
time.sleep(2)

pywhatkit.sendwhatmsg_instantly("+91 86023 60225", "hello scripted msg",tab_close=True, close_time=3)

# WhatsApp Web ko type karne ka time dene ke liye thoda wait
time.sleep(4)

# Auto-enter to send the message
pyautogui.press("enter")
print("Message sent successfully!")