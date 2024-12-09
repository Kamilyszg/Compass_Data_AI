import hashlib

while True:
    entrada = input("Digite uma string para gerar o hash: ")

    conversao_hash = hashlib.sha1(entrada.encode())
    hash_hex = conversao_hash.hexdigest()

    print(f"Hash SHA-1: {hash_hex}")