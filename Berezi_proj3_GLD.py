import string
def rotate(plain_text, rotate_num):
    """shifts letters in string passe down in the alphabetical order by some number passed into the function,
    wrapping around back to a. """
    encrypt = [] 

    for i in list("".join(plain_text)):
        dec_value = int(rotate_num) + ord(i)
        if i in string.punctuation: #checks for punctuation symbols in the list  
            encrypt.append(i) #adds back to the list without encrypting
            continue
        if dec_value in range (65,91) or dec_value in range(97,122):# checks if its in range
            encrypt.append(chr(dec_value))
            continue
        if dec_value in range(91, 97) or dec_value in range(123, 128): #checks if its in range
            encrypt.append(chr(dec_value - 26))
        else:
            encrypt.append(i)
        
    return "".join(encrypt)

def file(file_name, cipher):
    """Encrypts text using the cipher passed in the file passed into the function and save it into another text file """
    cipher_split = cipher.split() # splits the elements of cipher
    org_file = open(file_name, "r") #opens the file passed into the function
    read_lines = org_file.read() #reads the lines in the text
    encrypt = open("encrypted_" + file_name, "w")
    
    if cipher[0] == "Shift":
        #if it satisfies  the condition above it encrpts file using the rotate function
        encrypt.write(rotate(read_lines, 1))
        
    elif cipher[0] == "Rotate":
        #if it satisfies  the condition above it encrpts file using the rotate function

        encrypt.write(rotate(read_lines, int(cipher_split[1])))
        #if it satisfies  the condition above it encrpts file using the rotate function
   
    elif cipher[0] == "Substitute":
        #if it satisfies  the condition above it encrpts file using the substitution function
        for i in read_lines:
            encrypt.write(substitution(cipher_split[1], i))
            
        
    org_file.close()
    encrypt.close()
    print("File encrypted and saved as encrypted_" + file_name)
    
def substitution(letter_change, plain_text):
    """Replaces letters in the text passed into the function with letters in the key passed into the function"""
    mpty = [] 
    clone_text = plain_text[:]#clones the text passed in as a list
    clone_text_1 = plain_text[:] #clones the text passed in as a list
    char_list = list(letter_change)
    for i, v in enumerate(list(letter_change)):
        if v not in string.punctuation and i < len(list(letter_change)) - 1 and char_list[i+1] not in string.punctuation:
            #removes punctuation symbols form the list
            mpty.append(v+char_list[i+1])
#             print(mpty)
    for i in mpty:
        character = list(i)
        if character[0] or character[0].swapcase() in plain_text:
            for k, v in enumerate(plain_text):
                if v.lower() == character[0] and v != character[0]: # checks if its lower case or upper case
                    d = clone_text_1.index(v) # finds the first occurence
                    clone_text.insert(d, character[1].swapcase()) #nserts the swapped letter 
                    clone_text_1.insert(d, "") #inserts an empty string into the position of the former letter 
                    del clone_text[d+1] #del the former letter out of the list
                    del clone_text_1[d+1] #del the former letter out the list
                elif v == character[0]:
                    d = clone_text_1.index(v)#nserts the swapped letter
                    clone_text.insert(d, character[1])
                    clone_text_1.insert(d, "")
                    del clone_text[d+1]
                    del clone_text_1[d+1]
    return "".join(clone_text)

def main():
    while True:
        cipher = input("Cipher (or Quit) :")
        split = cipher.split()
        
        good_cipher = ["Shift", "Rotate", "Substitute", "Quit"]
        if split[0] not in good_cipher or len(split) >2: #error handling
            print("Invalid Cipher")
            continue
        if cipher == "Quit":
            print("Goodbye")
            break
        plain_text = input("Plain text:")
        split_text = plain_text.split()
        
        if split_text[0] == "File":
            try: # error handling
                open_file = open(split_text[1], "r")
                open_file.close()
            except:
                print(split_text[1] + " not found")
                continue
            file(split_text[1], cipher)
            
        elif "Rotate" in cipher:
            print("cipher text: " + rotate(plain_text, split[1]))
        
        elif "Substitute" in cipher:
            print("cipher text:" + substitution(split[1], "".join(plain_text) ))
                
main()
    

        
    
        