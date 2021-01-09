
import base64
import Crypto.Util.number


flag = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print(bytes(flag).decode())

flag = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

print(bytes.fromhex(flag).decode())


flag='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
flag = bytes.fromhex(flag)
print (base64.b64encode(flag).decode())


flag = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print (Crypto.Util.number.long_to_bytes(flag).decode())