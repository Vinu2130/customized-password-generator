import string
import random

def generate_password(str_length,use_lwcase,use_upcase,use_nums,use_spchars):
    lowercase = string.ascii_lowercase if use_lwcase else ""
    uppercase = string.ascii_uppercase if use_upcase else ""
    numbers = string.digits if use_nums else ""
    special_characters = string.punctuation if use_spchars else ""

    

    charString = lowercase+uppercase+numbers+special_characters
    if not charString:
        print("give atleast one character type...")
        ask_user()
        return ""
        

    password=[]

    for i in range(str_length):
        password.append(random.choice(charString))

    return "".join(password)

def ask_user():
    str_length = int(input("Specify the length of the string: "))
    use_lwcase = input("use lowercase letters? (y/n) : ").lower()=="y" 
    use_upcase = input("use uppercase letters? (y/n) : ").lower()=="y" 
    use_nums = input("use numbers? (y/n) : ").lower()=="y" 
    use_spchars = input("use special characters ? (y/n) : ").lower()=="y" 

    random_password= generate_password(str_length,use_lwcase,use_upcase,use_nums,use_spchars)
    print(random_password)
ask_user()