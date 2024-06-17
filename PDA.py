import FA

def topStack(stack):
    return stack[len(stack)-1]

def PDA(sentence):
    tokens = FA.cekTypes(sentence)
    consider = ''

    for f in tokens:
            consider += f
            consider += ' '
            
    consider = consider.rstrip("$ ")

    tabel = []

    t = 1
    hasil = ''
    content = ''
    
    #appne = push di stack
    #pop = pop di stack
    #topStack = cek top dari stack

    stack = []
    #State inisiasi
    state = 'q0'
    #Transisi ke q1 dengan append #
    stack.append('#')

    for s in stack:
        hasil += s

    for h in tokens:
        content += h

    isi = [t, state, hasil, content]
    t = t+1
    tabel.append(isi)

    #Masuk state q1
    state = 'q1'
    #Transisi ke q2 dengan append S
    stack.append('S')

    hasil = ''
    content = ''
    for s in stack:
        hasil += s

    for h in tokens:
        content += h

    isi = [t, state, hasil, content]
    t = t+1
    tabel.append(isi)

    #Masuk state q2
    state = 'q2'

    topS = topStack(stack)
    run = True
    if tokens != []:
            symbol = tokens[0]
    else:
        run = False

    while topS != '#' and run:
        match topS:
            case 'S':
                if symbol == 's':
                    stack.pop()
                    stack.append('B')
                    stack.append('A')
                    stack.append('p')
                    stack.append('s')
                else:
                    break
            case 'A':
                if symbol == 'o':
                    stack.pop()
                    stack.append('o')
                elif symbol == 'k':
                    stack.pop()
                elif symbol == '$':
                    stack.pop()
                else:
                    break
            case 'B':
                if symbol == 'k':
                    stack.pop()
                    stack.append('k')
                elif symbol == '$':
                    stack.pop()
                else:
                    break
            case 's':
                if symbol == 's':
                    stack.pop()
                    tokens.pop(0)
                    symbol = tokens[0]
                else:
                    break
            case 'p':
                if symbol == 'p':
                    stack.pop()
                    tokens.pop(0)
                    symbol = tokens[0]
                else:
                    break
            case 'o':
                if symbol == 'o':
                    stack.pop()
                    tokens.pop(0)
                    symbol = tokens[0]
                else:
                    break
            case 'k':
                if symbol == 'k':
                    stack.pop()
                    tokens.pop(0)
                    symbol = tokens[0]
                else:
                    break
        
        hasil = ''
        content = ''
        for s in stack:
            hasil += s

        for h in tokens:
            content += h

        isi = [t, state, hasil, content]
        tabel.append(isi)
        t = t+1

        topS = topStack(stack)
    
    #Masuk state q3
    state = 'q3'
    stack.pop()
    tokens.pop(0)
    hasil = ''
    content = ''
    for s in stack:
        hasil += s

    for h in tokens:
        content += h

    isi = [t, state, hasil, content]
    tabel.append(isi)

    if run and symbol == '$':
        print("Readall")
    else:
        print("Error")
    
    print("%2s %15s %15s %15s" %('No', 'Current State', 'Stack Content', 'Remaining Symbol'))

    for s in tabel:
        print("%2d %15s %15s %15s" %(s[0], s[1], s[2], s[3]))

    if len(stack) == 0:
        print("Stack finished")
        print("Grammar: ", consider)
    else:
        print("Stack not finished")