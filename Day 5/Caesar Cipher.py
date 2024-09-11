logo = """           
,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,  
a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8  
8b          ,adPPPPP88  8PP           `"Y8ba*  ,adPPPPP88  88          
"8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88          
 `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88   

                             88                                   
            88               88                                   
            ""               88                                   
 ,adPPYba,  88  8b,dPPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,  
a8"     ""  88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
8b          88  88       d8  88       88  8PP"""""""  88          
"8a,   ,aa  88  88b,   ,a8"  88       88  "8b,   ,aa  88          
 `"Ybbd8"'  88  88`YbbdP"'   88       88   `"Ybbd8"'  88          
                88                                                
                88            
"""
print(logo)
start = True
while start == True :

    to_do = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while to_do != 'encode' and to_do != 'decode' :
        to_do = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    word = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
# To rule out the possibility of indexerror due to index out of range 
    while 0<shift<=26 :
        alphabets ="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        alphabets_list = list(alphabets)

        def Encrypt():
            encrypted_letter_list = []
            for letter in word :
                if letter in alphabets_list:
                    encrypted_letter_list.append(alphabets_list[alphabets_list.index(letter) + shift])
                else :
                    encrypted_letter_list.append(letter)
            #global encrypt_word
            encrypt_word = "".join(encrypted_letter_list)
            print("Here's the encoded result:\n",encrypt_word,sep = "")
            

        def Decrypt():
            decrypted_letter_list = []
            for letter in word:
                if letter in alphabets_list:
                    decrypted_letter_list.append(alphabets_list[alphabets_list.index(letter)-shift])
                else :
                    decrypted_letter_list.append(letter)
            decrypt_word = "".join(decrypted_letter_list)
            print("Here's the decoded result:\n",decrypt_word,sep = "")

        if to_do == "encode" :
            Encrypt()
        elif to_do == "decode" :
            Decrypt()
        break
    if shift > 26 or shift <= 0 :
        print("Either your shift was too large or negative or zero.\nTry Again")
    switch = input("Type 'yes' if you want to go again. Else type 'no' :\n")
    while switch != 'yes' and switch != 'no':
        switch = input("Type 'yes' if you want to go again. Else type 'no' :\n")
    if switch == "yes":
        start == True 
    elif switch == "no" :
        start == False
        
