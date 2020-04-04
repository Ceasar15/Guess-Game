code= """*********************************
            Made By Ceasar Agbekuadzi
        *********************************"""        
print(code)


password_List=[]

while True:
        user_Name=input("\n Please enter your username: ")
        password= input("\n Please enter your password: ")
        searchFile=open("accounts.txt","r")
        for line in searchFile:
            password_List.append(line.strip())
            if user_Name and password in password_List:
                print("\n Please Wait, Loading...")
                print("\n Access has been granted")
                while True:
                    userGuess= int(input("\n Please guess your number: "))
                    import random
                    computer_rand = (1,2,3,4,5,6)
                    computer_rand = random.choice(computer_rand)
                    

                        #Guess_Implementation

                    if userGuess == 0:
                        print("Your Username: ")
                        print(user_Name)
                        print("Your password: ")
                        print(password)
                       
                    if userGuess == 9:
                        print("Thanks for playing!!!")
                        break    

                    if userGuess == computer_rand:
                        print("The computer chose: ", computer_rand)
                        print("*******")
                        print("You won")
                        print("*******")
                    else:
                        print("The computer chose: ", computer_rand)
                        print("*******")
                        print("You lost")
                        print("*******")
                            
                        
                        #GuideLines
                        
 
                break
            else:
                print("**************************")
                print("Your Password is incorrect")
                print("**************************")

               
               
               
               
               
               
               
               
               
               
                












    









