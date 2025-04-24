import socket
import win32api
import pyautogui as pg

def check_capslock():
   if win32api.GetKeyState(0x14): # if returns 1, capslock is active
       print('\nCaps Lock ativo, desativando-o...')
       pg.press('capslock')
   else:
       print('\nCaps Lock já está desativado...') 

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def verify_gospel_text_length(text): # Return the font size of the image text
    length = len(text)

    if length <= 783:
        return 32
    if length <= 956: 
        return 30.5  # Default
    elif length <= 1176:
        return 27.5  
    elif length <= 1363:
        return 25.5
    elif length <= 1590:
        return 23.5
    elif length <= 1790:
        return 21.5
    else:
        return 20
    
if __name__ == '__main__':
    check_capslock()
    