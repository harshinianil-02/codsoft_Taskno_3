import random
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D",
           "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digits=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","@","#","$","%","^","&","*",")","("]
print("Welcome To The Password Generator")
complexity=input("Complexity of your password is Easy or Hard: ")
n_alphabets=int(input("How many no.of alphabets you want in your password ?"))
n_digits=int(input("How many no.of digits you want in your password ?"))
password = ""
if(complexity == "Hard"):
    n_symbols=int(input("How many no.of symbols you want in your password ?"))
    for i in range(1,n_alphabets+1):
        r=random.choice(alphabets)
        password+=r
    for i in range(1,n_digits +1):
        r=random.choice(digits)
        password+=r
    for i in range(1,n_symbols+1):
        r= random.choice(symbols)
        password+=r
    print(f"Your Password is {password}")
else:
    for i in range(1,n_alphabets+1):
        r=random.choice(alphabets)
        password+=r
    for i in range(1,n_digits +1):
        r=random.choice(digits)
        password+=r
    print(f"Your Password is {password}")
user_choice=input("Do You want to shuffle your password order give Yes or No: ")
if(user_choice == "Yes"):
    password_list=list(password)
    random.shuffle(password_list)
    password_new=""
    for i in password_list:
        password_new+=i
    print(f"Your Modified new password is {password_new}")
else:
    print("It's Ok")
    


