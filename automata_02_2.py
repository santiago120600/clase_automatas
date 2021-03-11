

def automata(palabra):
    estado = 0
    enteros = ['0','1','2','3','4','5','6','7','8','9']
    indice = 0
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
            # print("el edo es",estado," ","la letra es",letra," ","el indice es",indice)
            if(estado==1):
                if letra == '+':
                    if(indice+1 < len(palabra)):
                        if(not palabra[indice+1]=='+'):     
                            print('+ | suma')
                            print('---------------------------------------')
                            estado = 2
                        else:
                            estado = 4
                    else:
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
                    print('False')
                    return False
            elif(estado==2):
                if letra == '+':
                    if(indice+1 < len(palabra)):
                        if(not palabra[indice+1]=='+'):     
                            print('+ | suma')
                            print('---------------------------------------')
                            estado = 2
                        else:
                            estado = 4
                    else:
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
                    print('False')
                    return False
            elif(estado==3):
                if letra == '+':
                    if(indice+1 < len(palabra)):
                        if(not palabra[indice+1]=='+'):     
                            print('+ | suma')
                            print('---------------------------------------')
                            estado = 2
                        else:
                            estado = 4
                    else:
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
                    print('False')
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
                    print('False')
                    return False
            else:
                print('False')
                return False
            #aumentar indice
            indice += 1
    else:
        print('False')
        return False


automata('0++')
# automata(input())