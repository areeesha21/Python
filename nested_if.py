username=input("enter the username:")
email=input("enter your email:")
pwd=input("enter the passcode")
cpwd=input("confirm your password")

if len(username)>0 and username.isalnum(): #len funjction is used here to check the length of the username and isalnum to check if the username is alphanumeric
    if len(email)>0 and"@" in email:
        print("email and username is valid ")
    else:
        print("invalid email")
else:
     print("username is invalid ")