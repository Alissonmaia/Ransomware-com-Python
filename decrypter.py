
import os
import pyaes

## abrir o arquivo criptografado

file_cripto = 'teste.txt.ransomwaretroll'
file = open (file_cripto, 'rb')
file_data = file.read()
file.close

##Set a chave de descriptografia

##chave de 16 de bits
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)


##remover o arquivo criptografado
os.remove(file_cripto)

##Criar um novo arquivo descriptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()

