import random as rd
import pyttsx3

Subjects = [
    "A man from Kerala ",
    "Aliens disguised as cats ",
    "A group of penguins ",
    "Tech CEO accidentally ",
    "School principal caught ",
    "Time-traveling goat ",
    "Underground TikTok cult ",
    "AI robot built by teenagers ",
    "Mystery man in pajamas ",
    "Monkey wearing a suit "
]

Actions = [
    "declares himself king of ",
    "hijacks subway in ",
    "builds pyramid in ",
    "starts dancing competition in ",
    "eats 100 burgers at ",
    "launches UFO from ",
    "creates portal to another world at ",
    "hosts wedding for crows in ",
    "writes poetry across walls in ",
    "starts fire using only spoons in "
]

Places = [
    "Mumbai",
    "Delhi metro",
    "a local zoo",
    "Times Square",
    "an abandoned temple",
    "school playground",
    "Chennai beach",
    "inside Parliament",
    "a crowded McDonald's",
    "a haunted museum"
]


while True:
    generate=input("To Get The Fake Head Line Enter (y):")
    if "y"==generate.strip().lower():
        subject=rd.choice(Subjects)
        Action=rd.choice(Actions)
        Place=rd.choice(Places)
        HeadLine=subject+Action+Place
        print("Fake News HeadLIne:",HeadLine)
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)     
        engine.setProperty('volume', 0.9)   
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id) 

        engine.say(HeadLine)
        engine.runAndWait()
    else:
        break
    
    
    