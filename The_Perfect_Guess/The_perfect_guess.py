import random 
n=random.randint(1,100)
a=-1
b=0
while (a!=n):
    a=int(input('Guess the number:'))
    if(a>n):
        print('Guess lower:')
        
    else:
        print('Guess higher:')
    
    b+=1
print(f'Congratulations you guess the Correct Number in {b} attempts!!!!')