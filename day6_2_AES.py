from Crypto.Cipher import AES
from base64 import b64encode,b64decode
from Crypto import Random

message="I'm the best"
pk='1234567890123456'
# vector Generating
iv=Random.new().read(AES.block_size)
# Key Generating
cipher=AES.new(pk.encode('utf8'),AES.MODE_CFB,iv)
print(cipher)
# Encryption
encrypted=cipher.encrypt(message.encode('utf8'))

# Again Key generation
cipher=AES.new(pk.encode('utf8'),AES.MODE_CFB,iv)
decription=cipher.decrypt(encrypted).decode('utf8')
print(decription)

                         
                         
                         
                        