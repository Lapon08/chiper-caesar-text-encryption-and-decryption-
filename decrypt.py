def decrypt(chipertext,shift):
    # Caesar cipher decryption formula E = (x-n) mod 26
    plaintext= ""
    for char in chipertext:
        #check whether the alphabet or not
        if char.isalpha():
            #check whether capital letters or not
            if char.isupper():
                plaintext += chr((ord(char)-shift-65)% 26 +65)
            else:
                plaintext += chr((ord(char)-shift-97)% 26 +97)
        #if it is a symbol
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    print("Enter the ciphertext:",end=" ")
    chipertext = input()
    print("The shift will be in bruteforce from 1 to 26")
    for shift in range(1,27):
        print("plaintext with shifted {} is: ".format(str(shift)),end=" ")
        print(decrypt(chipertext,shift))
