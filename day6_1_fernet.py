from cryptography.fernet import Fernet
message="I'm the best"
PK=Fernet.generate_key()
fernet=Fernet(PK)
encMessage=fernet.encrypt(message.encode())
print(encMessage)
deCrypt=fernet.decrypt(encMessage).decode()
print(deCrypt)