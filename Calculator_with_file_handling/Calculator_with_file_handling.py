
from os import path

#check if history file exists if not then create it:
if path.isfile("history.txt"):
    print("File Already Exist:")
else:
    with open("history.txt","w") as f:
        f.write("")
#create a Function to check history:
def history():
    with open("history.txt","r") as f:
        lines=f.readlines()
    if len(lines)==0:
        print("No recent History:")
    else:
        for line in reversed(lines): #here we reversed the list so we get the recent calculation first
            print(line.strip())
def save_history(equation,result):
    with open("history.txt","a") as f:
        f.write(equation+"="+str(result)+'\n')
    
#function to clear history:
def clear():
    with open("history.txt","w") as f:
        f.write("")
    print("History Cleared Sucessfully!!!")
#now claculation function
def Calculate(user_input):
    user_input=user_input.split(" ")
    if len(user_input)!=3:
        print("Invalid input:PLease Use format(e.g 2+5,6*9)")
        print(user_input)
    else:
        a=float(user_input[0])
        b=float(user_input[2])
        if user_input[1]=="+":
            
            return a+b
        elif  user_input[1]=="-":
            return a-b
        elif  user_input[1]=="*":
            return a*b
        elif  user_input[1]=="/":
            if b==0:
                print("Invalid Expression!!!")
            else:
                return a/b
#create a main() that integrates all above features:
def main():
    while True:
        user_input=input("Enter Expression(e.g 2+3(+,-,?,*)) or Commands(history,exit,clear):")
        if user_input=="history":
            history()
        elif user_input=="clear":
            clear()
        elif user_input=="exit":
            print("Program Ended sucessfully!!!")
            break
        else:
            result=Calculate(user_input)
            save_history(user_input,result)
            print(result)
main()

    





        
    