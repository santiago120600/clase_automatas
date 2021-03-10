

def automata(palabra):
    estado = 0
    enteros = ['0','1','2','3','4','5','6','7','8','9']
    if palabra:
        print('***************************************\ncaracter | representa\n***************************************')
        # estado 0
        if palabra[0] in enteros:
            estado=1
        elif palabra[0] == '*':
            estado=3
        elif palabra[0] == '+':
            estado=2
        # estado 0
        for letra in palabra:
            if(estado==1):
                if letra == '+':
                    print('+ | suma')
                    print('---------------------------------------')
                    estado = 2
                elif letra in enteros:
                    print(letra,'| numero')
                    print('---------------------------------------')
                    estado = 1
                elif letra == '*':
                    print('* | producto')
                    print('---------------------------------------')
                    estado = 3
                else:
                    return False
            elif(estado==2):
                if letra == '+':
                    print('+ | suma')
                    print('---------------------------------------')
                    estado = 4
                elif letra in enteros:
                    print(letra,'| numero')
                    print('---------------------------------------')
                    estado = 1
                elif letra == '*':
                    print('* | producto')
                    print('---------------------------------------')
                    estado = 3
                else:
                    return False
            elif(estado==3):
                if letra == '+':
                    print('+ | suma')
                    print('---------------------------------------')
                    estado = 2
                elif letra in enteros:
                    print(letra,'| numero')
                    print('---------------------------------------')
                    estado = 1
                elif letra == '*':
                    print('* | producto')
                    print('---------------------------------------')
                    estado = 3
                else:
                    return False
            elif(estado==4):
                if letra == '+':
                    print('++ | incremento')
                    print('---------------------------------------')
                    estado = 2
                elif letra in enteros:
                    print(letra,'| numero')
                    print('---------------------------------------')
                    estado = 1
                elif letra == '*':
                    print('* | producto')
                    print('---------------------------------------')
                    estado = 3
                else:
                    return False
            else:
                return False
    else:
        return False


automata('++++0012*')