#Removed unecesary while loop for stuart
def minion_game(string):
   
    Vowels="AEIOU"
    kevin=0
    stuart=0
    
    i=0
    while i <len(string):
        k=i
        score=0
        while k<len(string):
                score+=1
                k+=1
        if string[i] in Vowels:
            kevin+=score
        else: 
            stuart+=score
        i+=1
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
minion_game('BANANA')
#old code
# def minion_game(string):
   
#     Vowels="AEIOU"
#     kevin=0
#     stuart=0
#     i=0
#     while i <len(string):
#         if string[i] in Vowels:
#             k=i
#             while k<len(string):
#                 kevin+=1
#                 k+=1
#         else: 
#             k=i
#             while k<len(string):
#                 stuart+=1
#                 k+=1
#         i+=1
#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif stuart > kevin:
#         print("Stuart", stuart)
#     else:
#         print("Draw")
# minion_game('BANANA')