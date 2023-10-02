import pyautogui
import time
import pandas as pd


pyautogui.PAUSE = 0.3   #Set pause time for "pyautogui" tasks

#Opens Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

#Goes to the specified URL
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#Logs in
pyautogui.click(x=508, y=397)       #Positions cursor in email field
pyautogui.write("algumemail@yahoo.com")
pyautogui.press("tab")
pyautogui.write("algumasenha")
pyautogui.press("tab")
pyautogui.press("enter")


#Imports table into variable "table"
table = pd.read_csv("produtos.csv")

# print(table)      #Prints table on terminal

#Reads each record of the table and generates the necessary input in the web portal
for line in table.index:
    time.sleep(3)
    pyautogui.click(x=500, y=280)       #Positions cursor in "codigo" field

    pyautogui.write( str( table.loc[line, "codigo"] ) )
    pyautogui.press("tab")

    pyautogui.write( str( table.loc[line, "marca"] ) )
    pyautogui.press("tab")

    pyautogui.write( str( table.loc[line, "tipo"] ) )
    pyautogui.press("tab")

    pyautogui.write( str( table.loc[line, "categoria"] ) )
    pyautogui.press("tab")

    pyautogui.write( str( table.loc[line, "preco_unitario"] ) )
    pyautogui.press("tab")

    pyautogui.write( str( table.loc[line, "custo"] ) )
    pyautogui.press("tab")

    obs = table.loc[line, "obs"]

    if not pd.isna(obs):
        pyautogui.write( str( obs ) )

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(500)       #Scrolls up the page

