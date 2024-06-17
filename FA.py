dfaP = {0:{'b':1, 'm':4, 't':11, 'l':15}, 
        1:{'a':2}, 2:{'c':3}, 3:{'a':19}, 
        4:{'a':5, 'i':8}, 5:{'k':6}, 6:{'a':7}, 7:{'n':19}, 
        8:{'n':9}, 9:{'u':10}, 10:{'m':19}, 
        11:{'u':12}, 12:{'l':13}, 13:{'i':14}, 14:{'s':19}, 
        15:{'i':16}, 16:{'h':17}, 17:{'a':18}, 18:{'t':19}}

dfaO = {0:{'n':1, 'b':4, 'a':7, 's':9, 'g':13}, 
        1:{'a':2}, 2:{'s':3}, 3:{'i':18}, 
        4:{'u':5}, 5:{'k':6}, 6:{'u':18}, 
        7:{'i':8}, 8:{'r':18}, 
        9:{'u':10}, 10:{'r':11}, 11:{'a':12}, 12:{'t':18}, 
        13:{'a':14}, 14:{'m':15}, 15:{'b':16}, 16:{'a':17}, 17:{'r':18}}

dfaS = {0:{'m':1, 's':6, 'k':9, 'd':12},
        1:{'e':2},
        2:{'r':3},
        3:{'e':4},
        4:{'k':5},
        5:{'a':14},
        6:{'a':7},
        7:{'y':8},
        8:{'a':14},
        9:{'a':10},
        10:{'m':11},
        11:{'u':14, 'i':14},
        12:{'i':13},
        13:{'a':14}}

dfaK = {0:{'d':1,},
        1:{'i':2},
        2:{'k':3, 'p':14, 't':16},
        3:{'a':4},
        4:{'p':5, 'n':7, 'm':10},
        5:{'a':6},
        6:{'l':22},
        7:{'t':8},
        8:{'o':9},
        9:{'r':22},
        10:{'p':11},
        11:{'u':12},
        12:{'n':13},
        13:{'g':22},
        14:{'p':15},
        15:{'s':16},
        16:{'a':17},
        17:{'r':22},
        18:{'e':19},
        19:{'l':20},
        20:{'y':21},
        21:{'u':22}}

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        if state in transitions and c in transitions[state]:
            state = transitions[state][c]
        else:
            return False

    return state in accepting

def cekTypes(sentence):
    #Jadikan semua menjadi lowercase
    sentence.lower()
    #Split semua menjadi per-string
    strings = sentence.split()
    types = []

    for kata in strings:
        if accepts(dfaP, 0, {19}, kata):
            types.append('p')
        elif accepts(dfaS, 0, {14}, kata):
            types.append('s')
        elif accepts(dfaO, 0, {18}, kata):
            types.append('o')
        elif accepts(dfaK, 0, {22}, kata):
            types.append('k')
        else:
            return []
    
    return types

print(cekTypes("saya makan"))