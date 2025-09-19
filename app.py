import random
import string


def only_numbers(digit):
    digit=input("Digit numbers:")
    chance=int(digit)
    a=random.randint(0,9)
    password=str(a)
    while True:
        if chance==1:
            return password
        b=random.randint(0,9)
        password+=str(b)
        chance-=1
def only_letters(digit):
    letters=["Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]
    digit=input("Digit numbers:")
    chance=int(digit)
    a=random.choice(letters)
    password=str(a)
    while True:
        if chance==1:
            return password
        b=random.choice(letters)
        password+=str(b)
        chance-=1
def letters_numbers(digit):
    letters=["Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]
    lettersandnumbers=["1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    digit=input("Digit numbers:")
    chance=int(digit)
    a=random.choice(lettersandnumbers)
    c=random.choice(letters)
    d=random.choice(numbers)
    password=str(a)
    password2="Password:"
    list1=[c,d,a]
    while True:
        if str(digit)=="3":
            random.shuffle(list1)
            for i in list1:
                password2+=i
            return password2
        if chance==4 :
            random.shuffle(list1)
            for i in list1:
                password += i
            return password
        b=random.choice(lettersandnumbers)
        list1.append(b)
        chance-=1

def letters_numbers_symbols(digit):
    symbols=["!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~"]
    letters=["Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]
    lettersandnumbersandsymbols=["!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    digit=input("Digit numbers:")
    chance=int(digit)
    a=random.choice(lettersandnumbersandsymbols)
    c=random.choice(letters)
    d=random.choice(numbers)
    e=random.choice(symbols)
    password=str(a)
    password2="Şifre:"
    list1=[c,d,a,e]
    if int(digit)>4:
        while True:
            if chance==5 :
                random.shuffle(list1)
                for i in list1:
                    password += i
                return password
            b=random.choice(lettersandnumbersandsymbols)
            list1.append(b)
            chance-=1
    else:
        if int(digit)==3:
            list3=[c,d,e]
            random.shuffle(list3)
            for i in list3:
                password2 += i
            return password2
        elif int(digit)==4:
            random.shuffle(list1)
            for i in list1:
                password2 += i
            return password2
print(""" 
1.Random password only letters
2.Random password only numbers
3.Random password numbers and letters
4.Random password numbers,letters and symbols
""")

while True:
    process=input("Which process do you want?")
    digit=0
    if process=="1":
        print(only_letters(digit))
        continue
    elif process=="2":
        print(only_numbers(digit))
        continue
    elif process=="3":
        print(letters_numbers(digit))
        continue
    elif process=="4":
        print(letters_numbers_symbols(digit))
        continue

