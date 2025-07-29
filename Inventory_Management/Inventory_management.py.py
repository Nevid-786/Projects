#inventory management using counter
from collections import Counter 

Inventory=Counter({'Apple':4,'Banana':5})

print(f'Inventory:{dict(Inventory)}')

#sales input
a=int(input('Enter sales of Apple:'))

b=int(input('Enter sales of Banana:'))

#create a new counter dict of sales
if Inventory['Apple']>=a and Inventory['Banana']>=b: #check if the sales are equal or less than items Available in Inventory
    
    Sales=Counter(Apple=a,Banana=b)
    print(f'Sales:{dict(Sales)}')
    
else:
    print('Inventory do not have this Much items to sell')
    
#update the inventory

Inventory=Inventory-Sales

print(f'updated Inventory:{dict(Inventory)}')

restock=input('For Restocking press Enter')

if restock=="":    
    #input for restock:
    a=int(input('Enter Restock of Apple:'))

    b=int(input('Enter Restock of Banana:'))
    #update the inventory
    Inventory+=Counter(Apple=a,Banana=b)
    print(f'Rstocked Inventory:{dict(Inventory)}')