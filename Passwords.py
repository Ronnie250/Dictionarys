pw={"Ronnie25":"Qwerty123","Ronak_Melwani":"RM2012","RM":"123"}
user=input("Enter Username")
if(user in pw):
    pas=input("Enter Password")
    if (pas==pw[user]):
        print("Welcome "+ user +"!")
    else:
        print("Password is incorrect :(")
else:
    print("User not found :(")