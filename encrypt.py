def encrypt(plaintext,shift):
    # Caesar cipher encryption formula E = (x-n) mod 26 E = (x+n) mod 26
    chipertext = ""
    for char in plaintext:
        #checked whether the alphabet or not
        if char.isalpha():
            #check whether capital letters or not
            if char.isupper():
                chipertext += chr((ord(char)+shift-65)% 26 +65)
            else:
                chipertext += chr((ord(char)+shift-97)% 26 +97)
        #if it is a symbol
        else:
            chipertext += char    
    return chipertext



if __name__ == "__main__":
    print("Enter the plaintext:",end=" ")
    plaintext = input()
    print("enter the shift number:",end=" ")
    shift = int(input())
    print("chipertext with shifted {} is: ".format(str(shift)),end=" ")
    print(encrypt(plaintext,shift))
