'''
********************************IT ASSIGNMENT************************************************88
***** GROUP MEMBERS::*****

---> PRASHU CHAUDHRY 
---> PRABHU TIWARI



'''
#Question 2: Write a program that can encrypt  and decrypt using the AFFINE Cipher.

'''
SAMPLE OUTPUT:

RUN1:

********** Welcome to AFFINE cipher program ***************
Enter value of a: 7
Enter value of b: 6
choose your option:
1.encryption
2.decryption
1
Enter your Plain text: hello
 Desired cipher text is : diffa

RUN2:

********** Welcome to AFFINE cipher program ***************
Enter value of a: 7
Enter value of b: 6
choose your option:
1.encryption
2.decryption
2
Enter your cipher text: diffa
Your required plain text is: hello

'''

class Inverse:
    def modularInverse(self, a, m):
        if m == 1:
            return -1
        x, gcd, y = self.euclideanAlgo(a, m)  # finding values of eqn using extended euclideanAlgo
        if gcd != 1:
            return None  # modular inverse does not exist
        return x + m if x < 0 else x

    def euclideanAlgo(self, a, b):
        if b == 0:
            return 1, a, 0
        temp_ans = self.euclideanAlgo(b, a % b)
        return temp_ans[2], temp_ans[1], temp_ans[0] - (a // b) * temp_ans[2]


class AffineCipher:
    # encrypting function
    #     C = (a*P + b) % 26 -->> formula for calculating cipher text
    def encrypt(self, text, key):
        cipherText = ''
        # traversing the plain text
        for char in text:
            # Insert whitespaces as it is
            if char == " ":
                cipherText += " "
                # Encrypt uppercase characters
            elif char.isupper():
                cipherText += chr(((key[0] * (ord(char)-ord('A')) + key[1]) % 26) + ord('A'))
                # Encrypt lowercase characters
            else:
                cipherText += chr(((key[0] * (ord(char) - ord('a')) + key[1]) % 26) + ord('a'))
        return cipherText

    # decrypting function
    #     P = (a^-1 * (C - b)) % 26 -->> formula for calculating plain text from cipher text
    def decrypt(self, cipherText, key):
        mv = Inverse()
        plainText = ''
        # traversing the cipherText text
        for char in cipherText:
            # Insert whitespaces as it is
            if char == " ":
                plainText += " "
                # Decrypt uppercase characters
            elif char.isupper():
                plainText += chr(((mv.modularInverse(key[0], 26) * (ord(char) - ord('A') - key[1])) % 26) + ord('A'))
                # Decrypt lowercase characters
            else:
                plainText += chr(((mv.modularInverse(key[0], 26) * (ord(char) - ord('a') - key[1])) % 26) + ord('a'))
        return plainText


# driver code
if __name__ == '__main__':
    cipher = AffineCipher()
    print("********** Welcome to AFFINE cipher program ***************")
    a = int(input("Enter value of a: "))  # user input for first key value i.e. 'a'
    b = int(input("Enter value of b: "))   # user input for second key value i.e. 'b'
    key = [a, b]
    c=int(input("choose your option:\n1.encryption\n2.decryption\n"))
    if c==1:
        text = input("Enter your Plain text: ")  # user input of plain text
        ans = cipher.encrypt(text, key)
        print(" Desired cipher text is :", ans)
    #  printing both plain and cipher text
    elif c==2:
        ans = input("Enter your cipher text: ")
        print("Your required plain text is:", cipher.decrypt(ans, key))
    else:
        print("Wrong choice !!")

