import re

def aradia(input):
    lower_text = input.lower()
    zero_text = re.sub("o","0",lower_text)
    return zero_text
def tavros(input):
    input = input[0].lower() + input[1:].upper()
    input = re.sub(r"[!.?]",",",input)
    return input
def sollux(input):
    input = input.lower()
    input = re.sub("s","2",input)
    input = re.sub("i","ii",input)
    return input
def karkat(input):
    input = input.upper()
    return input
def nepeta(input):
    input = ":33 < " + input.lower()
    input = re.sub("ee","33",input)
    input = re.sub(r"\.","",input)
    return input
def kanaya(input):
    input = input.lower()
    input = re.sub(r"[.!?,]","",input)
    new_input = ""
    for word in input.split():
        word = word[0].upper() + word[1:].lower()
        new_input = new_input + word + " "
    return new_input
def terezi(input):
    input = input.upper()
    input = re.sub(r"\.","",input)
    input = re.sub("A","4",input)
    input = re.sub("I","1",input)
    input = re.sub("E","3",input)
    return input
def vriska(input):
    input = re.sub(r"[Bb]","8",input)
    input = re.sub("ate","8",input)
    input = re.sub("ait","8",input)
    input = re.sub("eight","8",input)
    return input
def equius(input):
    input = "D--> " + input
    input = re.sub(r"[.!?]","",input)
    input = re.sub("r[Xx]","%",input)
    input = re.sub("cks","%",input)
    ahundred = re.compile("loo",re.IGNORECASE)
    onehundred = re.compile("lew",re.IGNORECASE)
    backhundred = re.compile("ool",re.IGNORECASE)
    wardshundred = re.compile("uel",re.IGNORECASE)
    input = re.sub(ahundred,"100",input)
    input = re.sub(onehundred,"100",input)
    input = re.sub(backhundred,"001",input)
    input = re.sub(wardshundred,"001",input)
    return input
def gamzee(input):
    text = ""
    for x in range(len(input)):
        if x % 2 == 0:
            text = text + input[x].lower()
        else:
            text = text + input[x].upper()
    return text
def eridan(input):
    input = input.lower()
    input = re.sub(r"[.,!?]","",input)
    input = re.sub("v","vv",input)
    input = re.sub("w","ww",input)
    input = re.sub("ing","in",input)
    return input
def feferi(input):
    input = re.sub(r"[Hh]",")(",input)
    input = re.sub("E","-E",input)
    return input

troll_name = input("Type in the name of the character you want to talk like: ").lower()
text = input("Now type in the text: ")
if troll_name == "aradia":
    print(aradia(text))
if troll_name == "tavros":
    print(tavros(text))
if troll_name == "sollux":
    print(sollux(text))
if troll_name == "karkat":
    print(karkat(text))
if troll_name == "nepeta":
    print(nepeta(text))
if troll_name == "kanaya":
    print(kanaya(text))
if troll_name == "terezi":
    print(terezi(text))
if troll_name == "vriska":
    print(vriska(text))
if troll_name == "equius":
    print(equius(text))
if troll_name == "gamzee":
    print(gamzee(text))
if troll_name == "eridan":
    print(eridan(text))
if troll_name == "feferi":
    print(feferi(text))
else:
    print("You used an invalid name.")
