#This program is to Count the occurances of all the words used in a string.
from collections import Counter
Text='Nevid is a smart Boy Nevid is a good Boy also'
List_of_Words=Text.split()
print(List_of_Words)   #['Nevid', 'is', 'a', 'smart', 'Boy','Nevid', 'is', 'a', 'good', 'Boy', 'also']
counter=Counter(List_of_Words)
print(counter)         #Counter({'Nevid': 2, 'is': 2, 'a': 2, 'Boy': 2, 'smart': 1, 'good': 1, 'also': 0