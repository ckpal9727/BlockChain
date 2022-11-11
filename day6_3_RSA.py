from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

#genrating key pair
keypair=RSA.generate(1024)
#extracting public key
pubkey=keypair.publickkey()
#exporting pub key
pubkeyExp=pubkey.exportKey()
#Exporting keypair
expPkPubKey=keypair.exportKey()
msg=b'hlo'
#generating encryptor using public kay
encryptor=PKCS1_OEAP.new(pubkey)
#encrytping the message 
encrypted=encryptor.encryp(msg)
#printitng encrypted message using binascii.hexlify
print("Encrypt message ",binascii.hexlify(encrypted))
#Generating decryptor key using keypai
decryptor=PKCS1_OAEP.new(keypair)
decrypted=decryptor.decrypt(encrypted)
print("decrypted message is ",decrypted)