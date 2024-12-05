# Esse programa roda com libs locais, mais facil de entender:

import hmac
import hashlib
import time
import struct
import base64

def generate_totp(secret, time_step=30):         
    # Decodifica a chave secreta (Base32 para bytes)
    key = base64.b32decode(secret, casefold=True)

    # Calcula o timestamp atual
    current_time = int(time.time()) // time_step

    # Codifica o timestamp como bytes
    time_bytes = struct.pack(">Q", current_time)

    # Gera o HMAC usando SHA-1 das variáveis 
    hmac_hash = hmac.new(key, time_bytes, hashlib.sha1).digest()

    # Realiza o dynamic truncation para obter um código de 6 dígitos
    offset = hmac_hash[-1] & 0x0F
    truncated_hash = hmac_hash[offset:offset + 4]
    code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
    return code % 10**6  # Retorna os 6 dígitos

# Bora rodar
print("Hora Certa", time.strftime("%H:%M:%S")) # Mostra o horario atual

print("digite a chave do TOTP: ")
secret = input (" ") # Chave secreta (em Base32)  ||  exemplo M6OIBBU62I5AM4ORZIKDREIYBCESLNAH
print("Sua chave é:", generate_totp(secret))

input("\n Pressione Enter para sair...") # O programa aguardará o usuário pressionar Enter para sair do console

