'''

********************************IT ASSIGNMENT************************************************88
***** GROUP MEMBERS::*****

---> PRASHU CHAUDHRY 
---> PRABHU TIWARI



'''

'''
QUES3:: Write a program that can perform a letter frequency attack on an addtive cipher
without human intervention. Your software should produce possible plain text in rough order
of likelihood. It would be good if your user interface allows user to specify
Give me top 10 possible plain texts


SAMPLE OUTPUT:

-------------letter frequency attack on an addtive cipher----------------
NOTE:PLEASE ENTER CIPHER TEXT IN UPPERCASE LETTERS
Enter you chipher-text :LIPPS
---------------------------------------------------------
Possible plain-text: LIPPS
Possible plain-text: KHOOR
Possible plain-text: JGNNQ
Possible plain-text: IFMMP
Possible plain-text: HELLO
Possible plain-text: GDKKN
Possible plain-text: FCJJM
Possible plain-text: EBIIL
Possible plain-text: DAHHK
Possible plain-text: CZGGJ
Possible plain-text: BYFFI
Possible plain-text: AXEEH
Possible plain-text: ZWDDG
Possible plain-text: YVCCF
Possible plain-text: XUBBE
Possible plain-text: WTAAD
Possible plain-text: VSZZC
Possible plain-text: URYYB
Possible plain-text: TQXXA
Possible plain-text: SPWWZ
Possible plain-text: ROVVY
Possible plain-text: QNUUX
Possible plain-text: PMTTW
Possible plain-text: OLSSV
Possible plain-text: NKRRU
Possible plain-text: MJQQT

'''
class thod():

    def ad_thod(self):

        
        print("-------------letter frequency attack on an addtive cipher----------------")
        print("NOTE:PLEASE ENTER CIPHER TEXT IN UPPERCASE LETTERS")
        k = input("Enter you chipher-text :")
        print("---------------------------------------------------------")

        for j in range(0, 26):
             plain = []
             text = " "
             for i in range(0 , len(k)):
                 if k[i] == ' ':
                     y = ' '
                     plain.append(y)
                     continue
                 b = (ord(k[i])-65)
                 z = (b-j)%26
                 y = (chr(z + 65))
                 plain.append(y)

             for x in plain:
                 text += x

             print(f'Possible plain-text:{text}')

ad = thod()
ad.ad_thod()
