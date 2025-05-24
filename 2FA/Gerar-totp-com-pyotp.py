# pegue a ca=have secreta que o app lhe deu e cole nesse gerador baseado em tempo
# Mais facil que isso não tem, esse roda igual o GERADOR totp-root.py 
# Esse usa a lib https://pypi.org/project/pyotp 
# joge no chat GPT caso não tenha entendido.

import pyotp
import time

print("Hora Certa", time.strftime("%H:%M:%S")) # Mostra o horario atual

chave = input("digite a chave do TOTP: ")
totp = pyotp.TOTP("chave")
print("Sua chave é:", totp.now()) # Chave secreta ||  exemplo M6OIBBU62I5AM4ORZIKDREIYBCESLNAH

input("\n Pressione Enter para sair...") # O programa aguardará o usuário pressionar Enter
