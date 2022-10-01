import re
import sys
import random
global rand_Key
rand_Key=0
id=0
class Infor:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.userkey=0
    def __str__(self):
        return f"My_account:{self.username} and {self.password}"
    @classmethod
    def modify():
        ...
    def delet():
        ...
def Validate(U,P):
    Pr=''
    try:
        if re.search(r"^@.+.+",U) and re.search("^[0-9][0-9][0-9][0-9][0-9][0-9]$",P):
            Pr=Show_account(U,P)
            if Pr==True:
                return True
            else:
                return False
    except:
        sys.exit("Account_Error")


def regeist(user_name,user_pass,user_email,user_number,user_key):
    global rand_Key
    rand_Key=user_key
    if re.search(r"^@.+.+",user_name) and re.search("^[0-9][0-9][0-9][0-9][0-9][0-9]$",user_pass):
        if re.search(r".+@qq\.com$",user_email) and re.search(r"^[1][3-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$",user_number):
            if str(user_key)==str(rand_Key):
                return "Register pass"
            else:
                return "Key_invalid"
        else:
            return "you e-mail or you phone-number invalid"
    else:
        return "Username or Password invalid"

def Sys():
    print("🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")
    print("🚀🚀.   Account Infor search    🚀")
    print("🚀🚀    Input:sea(Search_infor) 🚀")
    print("🚀🚀    Input:del(Delete_infor) 🚀")
    print("🚀🚀    Input:quit(Exit_sys)    🚀")
    print("🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")
    while True:
        i=input("Input you order: ")
        if i=='sea':
            se=input("Input search-Key:")
            ley=Search(se)
            print(ley)
        elif i=='del':
            de=input("Input delete_infor:")
            re_de=de
            print(re_de)
        elif i=='sho':
            ik=Infor()
            print(ik)
        elif i=='quit':
            sys.exit("Exit Sys")

def Output_password():
    while True:
        print("Automate you password ? [y/n]")
        c=input(": ").lower()
        if c=='y':
            Re=Random_password()
            print(f"Remember you password:{Re}")
            return Re
        elif c=='n':
            b=input("Password: ")
            if not b:
                continue
            else:
                return b

def Datebase(Name,Pass,Email,Number,U_Key):
    global id
    id+=1
    with open('account.txt','a') as file:
        user_infor=f"Id-{str(id)}-User_Key-{str(U_Key)}-User_name-{Name}-User_Password-{Pass}-Email-{Email}-User_Number-{Number}"
        file.write(user_infor+'\n')
    return "Storage Success"


def Random_password():
    Int=random.randint(100000,999999)
    return Int

def Search(n):
    with open('account.txt','r') as v:
        o=v.readlines()
        for i in o:
            scc=i.split('-')
            if n in scc:
                return scc
        return "Search_infor does't exist"

def Delete(n):
    with open('account.txt','r') as h:
        f=h.readlines()
        for i in f:
            fg=i.split('-')
            if n in fg:
                for k in fg:
                    fg.remove(k)
                return "Delete Success"
        return "Delete_infor does't exist"

def Show_account(X,Y):
    same=0
    with open('account.txt','r') as t:
        p=t.readlines()
        for i in p:
            acc=i.split('-')
            for j in acc:
                if j==X or j==Y:
                    same+=1
        if same==2:
            return True
        else:
            return False

def getaccount():
    if len(sys.argv)>2:
        return (sys.argv[1],sys.argv[2])
    else:
        x=input("Username: ")
        y=input("Password: ")
    return (x,y)
def frist_register():
    username=input("what's you nickname: ")
    userpassword=input("what's you init_password: ")
    useremail=input("what's you email_address: ")
    usernumber=input("what's you phone_number: ")
    user_key=random.randint(1000,9999)
    global rand_Key
    rand_key=user_key
    print(f"you key is {user_key}")
    userkey=input("what's you user_key: ")
    if userpassword=='':
        userpassword=Output_password()
    userpassword=str(userpassword)
    result=regeist(username,userpassword,useremail,usernumber,userkey)
    print(result)
    if result=='Register pass':
        strong=Datebase(username,userpassword,useremail,usernumber,user_key)
        return strong
    return "Register_falid"

def is_None(n,m):
    if n=='' and m=='':
        return True
    return False

def main():
    su=getaccount()
    x2=su[0]
    y2=su[1]
    if is_None(x2,y2):
        Result=frist_register()
        print(Result)
        Sys()
    if Validate(x2,y2):
        infor=Infor(x2,y2)
        Sys()
    else:
        sys.exit("Invalid account")


if __name__ == "__main__":
    main()