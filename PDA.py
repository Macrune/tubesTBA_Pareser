import FA

def topStack(stack):
    return stack[len(stack)-1]

def PDA(sentence):
    tokens = FA.cekTypes(sentence)
    #appne = push di stack
    #pop = pop di stack
    #topStack = cek top dari stack

    stack = []
    #State inisiasi
    state = 'q0'
    #Transisi ke q1 dengan append #
    stack.append('#')
    #Masuk state q1
    state = 'q1'
    #Transisi ke q2 dengan append S
    stack.append('S')
    #Masuk state q2
    state = 'q2'

    topS = topStack(stack)
    i = 0
    run = True
    if tokens != []:
            symbol = tokens[i]
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
                    i += 1
                    symbol = tokens[i]
                else:
                    break
            case 'p':
                if symbol == 'p':
                    stack.pop()
                    i += 1
                    symbol = tokens[i]
                else:
                    break
            case 'o':
                if symbol == 'o':
                    stack.pop()
                    i += 1
                    symbol = tokens[i]
                else:
                    break
            case 'k':
                if symbol == 'k':
                    stack.pop()
                    i += 1
                    symbol = tokens[i]
                else:
                    break

        topS = topStack(stack)
    
    
    stack.pop()
    if run and symbol == '$':
        print("Readall")
    else:
        print("Error")

    if len(stack) == 0:
        print("Stack finished")
    else:
        print("Stack not finished")

    state = 'q3'
    print(state)

