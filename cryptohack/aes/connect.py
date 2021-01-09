import requests

decrypt = '/block_cipher_starter/decrypt/<ciphertext>/'
encrypt = '/block_cipher_starter/encrypt_flag/'
url = 'http://aes.cryptohack.org'

#send req for flag 
r = requests.get(url+encrypt)
data = r.json()
ciphertext = data['ciphertext']

#decrypt the flag

r = requests.get(url+decrypt+ciphertext)
data = r.json()
plaintext = data['plaintext']
#decode and print
print(bytes.fromhex(plaintext))