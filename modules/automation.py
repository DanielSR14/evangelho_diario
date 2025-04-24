from time import sleep
import pyautogui as pg
import pyperclip

# Função para abrir o navegador e acessar o Canva
def open_browser(url):
    print("\nAbrindo navegador...")
    pg.press('win')
    sleep(4)
    pg.write('Opera')
    sleep(3)
    pg.press('enter')
    sleep(5)
    pg.write(url)
    sleep(1)
    pg.press('enter')
    sleep(10)

# Função para inserir texto no Canva
def insert_text(text, x, y):
    text.capitalize()
    pg.click(x=x, y=y)
    sleep(2)
    pg.click(x=x, y=y)
    sleep(2)
    pg.hotkey('ctrl', 'a')
    sleep(2)
    pyperclip.copy(text)
    pg.hotkey('ctrl', 'v')
    sleep(2)
    pg.click(x=1478, y=308) # propaganda
    

def download_image():
    print("\nBaixando imagem...")
    sleep(2)
    pg.click(x=1871, y=131) 
    sleep(2)
    pg.click(x=1552, y=512)  
    sleep(7)
    pg.click(x=1702, y=574)  
    sleep(25)
    pg.hotkey('alt', 'f4')  

def change_font_size(font_size):
    print("\nAlterando o tamanho da fonte...")
    sleep(2)
    pg.click(x=1010, y=519)
    sleep(2)
    pg.click(x=735, y=189)
    sleep(2)
    pg.hotkey('ctrl', 'a')
    sleep(2)
    pg.write(str(font_size))
    sleep(2)
    pg.press('enter')
    sleep(2)
    pg.click(x=1478, y=308) # propaganda
