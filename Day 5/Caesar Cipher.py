from art import logo
def Encrypt():
    encrypted_letter_list = []
    for letter in word :
        if letter in alphabets_list:
            encrypted_letter_list.append(alphabets_list[(alphabets_list.index(letter) + shift)%26])
        else :
            encrypted_letter_list.append(letter)
    #global encrypt_word
    encrypt_word = "".join(encrypted_letter_list)
    print("Here's the encoded result:\n",encrypt_word,sep = "")
    

def Decrypt():
    decrypted_letter_list = []
    for letter in word:
        if letter in alphabets_list:
            decrypted_letter_list.append(alphabets_list[(alphabets_list.index(letter)-shift)%26])
        else :
            decrypted_letter_list.append(letter)
    decrypt_word = "".join(decrypted_letter_list)
    print("Here's the decoded result:\n",decrypt_word,sep = "")

print(logo)
start = True
while start == True :

    to_do = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while to_do != 'encode' and to_do != 'decode' :
        to_do = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    word = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    
    alphabets ="abcdefghijklmnopqrstuvwxyz"
    alphabets_list = list(alphabets)

    if to_do == "encode" :
        Encrypt()
    elif to_do == "decode" :
        Decrypt()

    switch = input("Type 'yes' if you want to go again. Else type 'no' :\n").lower()
    while switch != 'yes' and switch != 'no':
        switch = input("Type 'yes' if you want to go again. Else type 'no' :\n")
        
    if switch == "yes":
        start = True 
    elif switch == "no" :
        start = False
        
