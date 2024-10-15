#passo 0
import pyautogui as auto
import time as tm
import pandas as pd

#passo 1
auto.PAUSE = 0.3
auto.press('win')
auto.write('Opera')
auto.press('enter')
tm.sleep(3)

#passo 2
auto.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
auto.press('enter')
tm.sleep(3)
auto.click(x=544, y=394)
auto.write('williamlira41@gmail.com')
auto.press('tab')
auto.write('senhasenha')
auto.click(x=704, y=551)

#passo 3    SEMP    Televisao   18  500.0   140.0       

dados = pd.read_csv('produtos.csv')
print(dados)

#passo 4
for linha in dados.index:
    auto.click(x=532, y=281)
    codigo = dados.loc[linha, 'codigo']
    auto.write(str(codigo))
    auto.press('tab')
    auto.write(str(dados.loc[linha, 'marca']))
    auto.press('tab')
    auto.write(str(dados.loc[linha, 'tipo']))
    auto.press('tab')
    auto.write(str(dados.loc[linha, 'categoria']))
    auto.press('tab')
    auto.write(str(dados.loc[linha, 'preco_unitario']))
    auto.press('tab')
    auto.write(str(dados.loc[linha, 'custo']))
    auto.press('tab')
    obs = dados.loc[linha, 'obs']
    if not pd.isna(obs):
        auto.write(str(dados.loc[linha, 'obs']))
    auto.press('tab')
    auto.press('enter')

    #passo 5
    auto.scroll(5000)