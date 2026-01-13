from cores import(Verde,Reset)
import os
from time import sleep
import pyautogui
import pyperclip
import pandas as pd
import openpyxl

pyautogui.PAUSE = 1.3

os.system("open -a 'Google chrome'")
sleep(3)

drive_sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(drive_sistema)
pyautogui.press("enter")
sleep(4)

sleep(3)
pyautogui.press("tab")
email = "lpp2@cesar.school"
sleep(2)
pyautogui.write(email)
pyautogui.press("tab")
senha = "lucaspaguettilogin"
sleep(2)
pyautogui.write(senha)
sleep(1)
pyautogui.press("enter")
sleep(2)

pyautogui.press("tab")

rota_dados_csv = r"/Users/lucaspaguettipereira/Downloads/Produtos.csv"
tabela_dados = pd.read_csv(rota_dados_csv)

for _, linha in tabela_dados.iterrows():
    pyautogui.write(str(linha["codigo"]))
    pyautogui.press("tab")
    sleep(1)

    pyautogui.write(str(linha["marca"]))
    pyautogui.press("tab")
    sleep(1)

    pyautogui.write(str(linha["tipo"]))
    pyautogui.press("tab")
    sleep(1)

    pyautogui.write(str(linha["categoria"]))
    pyautogui.press("tab")
    sleep(1)

    pyautogui.write(str(linha["preco_unitario"]))
    pyautogui.press("tab")
    sleep(1)

    pyautogui.write(str(linha["custo"]))
    pyautogui.press("tab")
    sleep(1)

    pyautogui.write(""if pd.isna(linha["obs"]) else str(linha["obs"]))
    pyautogui.press("tab")
    sleep(1)
    
    pyautogui.press("enter")
    sleep(2)

    pyautogui.scroll(5000)
    sleep(0.5)
    pyautogui.click(x=600, y=300)
    pyautogui.scroll(7000)
    sleep(3)

print(f"""{Verde}✅ Automação finalizada com sucesso!
Todos os produtos do arquivo CSV foram inseridos no sistema.
{Reset}""")