alphabate=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                 'U', 'V', 'W', 'X', 'Y', 'Z']

def encryption(msg,shift):
    encrypt=""
    for letter in msg:
        index=alphabate.index(letter)
        encrypt+=alphabate[index+shift]
    print(encrypt)
def decryption(msg,shift):
    decrypt=''
    for letter in msg:
        index=alphabate.index(letter)
        decrypt+=alphabate[index-shift]
    print(decrypt)
type=input("Write encrypt or decrypt your msg:").lower()

msg=input("Write your msg").upper()
shift=int(input("Enter shift no."))
if type=="decrypt":
  decryption(msg,shift)
else:
    encryption(msg,shift)

