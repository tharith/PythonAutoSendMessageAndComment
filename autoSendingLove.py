import pyautogui
from time import sleep
from random import randint

numberOfMessageSending = 50

def contentMessageSending():
    content_message_list = [
        "I love you.",
        "I wanna go to cinema with you.",
        "I wanna be in your life.",
        "I wanna be in you heart",
        "I wanna take care 4ever",
        "Truth me, i do love you"
    ]
    
    random_content_message = content_message_list[randint(0, len(content_message_list) - 1)]
    return random_content_message

while True:
    pyautogui.typewrite(f"{contentMessageSending()}")
    sleep(.600)
    pyautogui.typewrite("\n")
    sleep(2)
    
    numberOfMessageSending = numberOfMessageSending - 1
    
    if numberOfMessageSending == 0:
        break