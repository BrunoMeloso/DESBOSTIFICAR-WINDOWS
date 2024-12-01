# Mais facil que isso não tem, esse roda igual o totp-root
# Esse usa a lib https://pypi.org/project/pyotp 

import pyotp
import time

print("Hora Certa", time.strftime("%H:%M:%S")) # Mostra o horario atual

chave = input("digite a chave do TOTP: ")
totp = pyotp.TOTP("chave")
print("Sua chave é:", totp.now()) # Chave secreta ||  exemplo M6OIBBU62I5AM4ORZIKDREIYBCESLNAH

input("\n Pressione Enter para sair...") # O programa aguardará o usuário pressionar Enter
