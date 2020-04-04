code= """*********************************
            Made By Ceasar Agbekuadzi
        *********************************"""  
print(code)

while True:
        print("\n Welcome to the setup of the Game")
        user_Name=input("\n PLease enter your name: ")
        password=input("\n Please enter your password: ")
        password_confirm= input("\n Please confirm your password: ")
        if password != password_confirm:
            print("\n Your password does not match")
        if password == password_confirm:
            print("\n Your account has been setup!!!")
        textFile= open("accounts.txt","a") 
        textFile.write('\n')
        textFile.write(user_Name)
        textFile.write('\n')
        textFile.write(password)   
        textFile.close()
        break






